# Movie Recommendation System

This repository contains a simple movie recommendation system built in Python. The project utilizes collaborative filtering to recommend movies to users based on their past preferences and the preferences of others.

## How it Works

The system is built using the Pandas library for data manipulation and analysis. Here's a brief overview of each part of the code:

- **Data Import and Cleanup**: Imports the user ratings and movie titles, merging them into a single DataFrame.
- **Pivot Table Creation**: Creates a pivot table for user ratings, setting up the basis for correlation computation.
- **Correlation Matrix**: Generates a Pearson correlation matrix for movie ratings, filtering out movies with less than 100 ratings.
- **User Interaction**: Allows users to input their movie preferences and ratings, which are then used to find similar movies.
- **Recommendation Generation**: Calculates similar movies by weighting the correlation matrix with the user's ratings and sorts them to find the highest recommended movies.
- **Final Output**: Displays the top 10 recommended movies, excluding the ones the user has already rated.

## How to Run

To run the recommendation system:

1. Ensure you have Python and Pandas installed.
2. Download the `u.data` and `u.item` files and place them in the same directory as the script.
3. Run the script in a Python environment.
4. Follow the on-screen prompts to enter movies and ratings.

## Personal Journey and Learning Experience

This project was an incredible learning experience, sparking my interest in Machine Learning and the inner workings of recommendation systems. As a beginner in 2019, building this system from scratch allowed me to understand the foundational concepts of data manipulation and the Pearson correlation, which are pivotal in the field of ML. It was a hands-on project that showcased the practical application of theory and the exciting possibilities that Machine Learning has to offer.

### Extras

I have also left behind the .ipynb (Jupyter Notebook) file behind for anyone who wants to sit and mess around with the code to see how different parameters change the outcomes. Feel free to use it :)
