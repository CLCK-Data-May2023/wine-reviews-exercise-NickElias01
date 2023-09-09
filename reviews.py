import pandas as pd

# Read the CSV file
wine_reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

# Group by 'country' and calculate the count and average points
wine_reviews = wine_reviews.groupby('country')['points'].agg(['count', 'mean'])

# Rename the columns for clarity
wine_reviews = wine_reviews.rename(columns={'count': 'count', 'mean': 'points'})

# Sort the DataFrame by the 'Count' column in descending order
wine_reviews = wine_reviews.sort_values(by='count', ascending=False)

# Round the 'Average Points' column to the tenths place
wine_reviews['points'] = wine_reviews['points'].round(1)

# Display the new DataFrame
print(wine_reviews)
