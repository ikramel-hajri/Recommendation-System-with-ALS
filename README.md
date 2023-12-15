# Movie Recommendation System with ALS

## Overview

This project implements a movie recommendation system using the Alternating Least Squares (ALS) algorithm, a collaborative filtering technique. Recommendation systems play a crucial role in providing personalized content suggestions to users, enhancing user experience, and increasing user engagement on platforms.

## Recommendation Systems

### Introduction

Recommendation systems, also known as recommender systems, are a type of software application that suggests items to users based on their preferences, behaviors, or interactions. These systems are widely used in various domains, including e-commerce, streaming services, social media, and more.

### Types of Recommendation Systems

1. **Collaborative Filtering:**
   - Collaborative filtering methods make automatic predictions (filtering) about the interests of a user by collecting preferences from many users (collaborating).
   - It can be further divided into user-based and item-based collaborative filtering.

2. **Content-Based Filtering:**
   - Content-based filtering recommends items similar to those the user has liked in the past, focusing on the attributes of items and users.

3. **Hybrid Methods:**
   - Hybrid recommendation systems combine multiple recommendation approaches to improve the accuracy and coverage of recommendations.

## ALS Algorithm

### Introduction

The ALS algorithm is a popular collaborative filtering technique used for building recommendation systems. It is particularly effective in handling large-scale sparse datasets.

### How ALS Works

1. **Matrix Factorization:**
   - ALS factorizes the user-item interaction matrix into two lower-rank matrices representing users and items.
   - These matrices capture latent features that explain user-item interactions.

2. **Alternating Least Squares Optimization:**
   - ALS optimizes the factorized matrices through an iterative process, alternating between fixing one matrix and solving for the other.

3. **Implicit Feedback:**
   - ALS can be adapted for implicit feedback data, where user-item interactions are binary (e.g., clicks, views) rather than explicit ratings.

## Dataset

The dataset used in this project is the MovieLens 25M Dataset, which includes 25 million movie ratings.

Dataset: [MovieLens 25M Dataset](link_to_dataset)

## Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ikramel-hajri/Recommendation-System-with-ALS
2. **Install dependencies:**
Ensure you have Apache Spark installed and configured on your system.
   
4. **Run the recommendation system:**
Modify the dataset path in the code to point to your ratings.csv file and execute the Python script.
   ```bash
   python recommendation_system.py

   
