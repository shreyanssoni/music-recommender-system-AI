README _ AI Project

Group 30 - Shreyans Soni, Dhruv Jain, Tushar Chattopadhyay

This repository contains two music recommendation systems: a Matrix Factorization (Singular Value Decomposition) method and a KNN collaborative filtering method.

Matrix Factorization (Singular Value Decomposition) Method - Content Based
The Matrix Factorization method uses a mathematical technique called Singular Value Decomposition (SVD) to factorize the user-song play count matrix into two matrices representing user features and song features. This allows for identifying latent factors (such as genre, artist, and mood) that are common between users and songs. The system then predicts the play count for a given user and song by multiplying the corresponding feature vectors.

To use this method, the user inputs their user id, and the system suggests songs based on their playlists and identified latent factors.

KNN Collaborative Filtering Method
The KNN collaborative filtering method uses user play count data to determine popular songs and make recommendations based on those songs. Specifically, it uses a KNN algorithm to identify similar songs based on play count data.

To use this method, the user inputs a song, and the system recommends songs based on the song given.

Both methods have been included in this repository, and can be run using the provided Jupyter notebooks.