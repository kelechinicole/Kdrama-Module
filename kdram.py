import pandas as pd

def load_excel(path):
    return pd.read_excel(path)
    ## Load an Excel file and return a DataFrame

def filter_by_column(df, column_name, value):
    return df[df[column_name] == value]
    ## Filter the DataFrame by a specific column and value

def get_rating (df, title):
   row = df[df['NAME'].str.lower() == title.lower()]
   if row.empty:
       return f"No rating found for title: '{title}'."
   return row['RATING'].values[0]
    ## Get the rating of a specific title from the DataFrame

def get_title_by_rating (df, rating):
    titles = df[df['RATING'] == rating]['NAME'].tolist()
    if not titles:
        return f"No titles found with rating: {rating}."
    return titles
    ## Get all titles with a specific rating from the DataFrame

def pull_synopsis(df, title):
    row = df[df['NAME'].str.lower() == title.lower()]
    if row.empty:
        return f"No synopsis found for title: '{title}'."
    return row['SYNOPSIS'].values[0]
    ## Pull the synopsis of a specific title from the DataFrame

def get_title_by_genre(df, genre):
    titles = df[df['GENRE'].str.lower() == genre.lower()]['NAME'].tolist()
    if not titles:
        return f"No titles found with genre: {genre}."
    return titles
    ## Get all titles with a specific genre from the DataFrame