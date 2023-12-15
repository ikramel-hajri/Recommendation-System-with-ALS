# -*- coding: utf-8 -*-
"""recommendation_system

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j4yFa_-ECpcd1zwDPu9lGz4FPWK6Wior

# Recommendation System with ALS
"""

from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating

from pyspark.sql import SparkSession
from pyspark.mllib.recommendation import ALS, Rating

# Create a Spark session
spark = SparkSession.builder.appName("MovieLensRecommendation").getOrCreate()

# Load and parse the MovieLens 25M Dataset
data = spark.read.option("header", "true").csv("ratings.csv")
ratings = data.rdd.map(lambda l: l.value.split(',')) \
    .map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))

# Extract relevant columns and convert to RDD
ratings = data.select("userId", "movieId", "rating").rdd.map(lambda row: Rating(int(row.userId), int(row.movieId), float(row.rating)))

# Build the recommendation model using ALS
rank = 10
numIterations = 10
model = ALS.train(ratings, rank, numIterations)

# Evaluate the model on training data
testdata = ratings.map(lambda p: (p[0], p[1]))
predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
ratesAndPreds = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
print("Mean Squared Error = " + str(MSE))

# Save and load model
model.save(spark.sparkContext, "target/tmp/myCollaborativeFilter")
sameModel = MatrixFactorizationModel.load(spark.sparkContext, "target/tmp/myCollaborativeFilter")

"""## Build the recommendation model using ALS with implicit feedback

"""

model = ALS.trainImplicit(ratings, rank, numIterations, alpha=0.01)

user_id = 123

# Generate all recommendations for the user
all_recommendations = model.recommendProducts(user_id, 10)  # Adjust the number as needed

# Sort the recommendations by rating in descending order
sorted_recommendations = sorted(all_recommendations, key=lambda x: x.rating, reverse=True)

# Display the top N recommendations
top_n = 10
for recommendation in sorted_recommendations[:top_n]:
    print(f"Item ID: {recommendation.product}, Score: {recommendation.rating}")

