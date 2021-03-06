
# ## Movie Recommendation System

from matplotlib.ft2font import BOLD
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval

credits_df = pd.read_csv("tmdb_5000_credits.csv")
movies_df = pd.read_csv("tmdb_5000_movies.csv")

credits_df.columns = ['id','tittle','cast','crew']
movies_df = movies_df.merge(credits_df, on="id")

# Demographic Filtering
C = movies_df["vote_average"].mean()
m = movies_df["vote_count"].quantile(0.9)

new_movies_df = movies_df.copy().loc[movies_df["vote_count"] >= m]

def weighted_rating(x, C=C, m=m):
    v = x["vote_count"]
    R = x["vote_average"]
    return (v/(v + m) * R) + (m/(v + m) * C)

new_movies_df["score"] = new_movies_df.apply(weighted_rating, axis=1)
new_movies_df = new_movies_df.sort_values('score', ascending=False)

new_movies_df[["title", "vote_count", "vote_average", "score"]].head(10)

# Plot top 10 movies
def plot():
    popularity = movies_df.sort_values("popularity", ascending=False)
    plt.figure(figsize=(12, 6))
    plt.barh(popularity["title"].head(10), popularity["popularity"].head(10), align="center", color="skyblue")
    plt.gca().invert_yaxis()
    plt.title("Top 10 movies")
    plt.xlabel("Popularity")
    plt.show()
    

tfidf = TfidfVectorizer(stop_words="english")
movies_df["overview"] = movies_df["overview"].fillna("")

tfidf_matrix = tfidf.fit_transform(movies_df["overview"])

# Compute similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(movies_df.index, index=movies_df["title"]).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):
    """
    in this function,
        we take the cosine score of given movie
        sort them based on cosine score (movie_id, cosine_score)
        take the next 10 values because the first entry is itself
        get those movie indices
        map those indices to titles
        return title list
    """
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    # (a, b) where a is id of movie, b is sim_score

    movies_indices = [ind[0] for ind in sim_scores]
    movies = movies_df["title"].iloc[movies_indices]
    return movies.values

features = ["cast", "crew", "keywords", "genres"]

for feature in features:
    movies_df[feature] = movies_df[feature].apply(literal_eval)

movies_df[features].head(10)

def get_director(x):
    for i in x:
        if i["job"] == "Director":
            return i["name"]
    return np.nan

def get_list(x):
    if isinstance(x, list):
        names = [i["name"] for i in x]

        if len(names) > 3:
            names = names[:3]

        return names

    return []

movies_df["director"] = movies_df["crew"].apply(get_director)

features = ["cast", "keywords", "genres"]
for feature in features:
    movies_df[feature] = movies_df[feature].apply(get_list)

movies_df[['title', 'cast', 'director', 'keywords', 'genres']].head()

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ""

features = ['cast', 'keywords', 'director', 'genres']
for feature in features:
    movies_df[feature] = movies_df[feature].apply(clean_data)

def create_soup(x):
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])

movies_df["soup"] = movies_df.apply(create_soup, axis=1)

count_vectorizer = CountVectorizer(stop_words="english")
count_matrix = count_vectorizer.fit_transform(movies_df["soup"])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

movies_df = movies_df.reset_index()
indices = pd.Series(movies_df.index, index=movies_df['title'])



#UI
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("350x420")
root.configure(bg="#009f92")
root.resizable(width=False, height=False)
root.title("Movie Recommendation")
 

def Take_input():
    try:
        Output.configure(state='normal')
        Output.delete('1.0', END)
        INPUT = inputtxt.get("1.0", "end-1c")
        answer = "\n".join(get_recommendations(INPUT, cosine_sim2))
        Output.insert(END, answer)
        Display.configure(state = 'active')
        Output.configure(state='disabled')
        
    except:
        messagebox.showerror("Wrong input", "Please enter a valid name!")
        Output.configure(state='disabled')

l4 = Label(text = "",bg="#009f92")
l = Label(text = "Insert Movie Name", bg="#009f92", fg = "black", font  = 'bold')

inputtxt = Text(root, wrap = NONE ,height = 2,
                width = 35,
                bg = "#f7e7be", borderwidth=1, relief="solid")

l1 = Label(text = "",bg="#009f92")

Output = Text(root, height = 10,
              width = 35,
              bg = "#f7e7be" ,borderwidth=1, relief="solid")

Output.configure(state='disabled')

Display = Button(root, height = 2, bg="#005366", fg ="#f7e7be", activebackground="#003E4D",
                 width = 39,
                 text ="Recommend",
                 command = lambda:Take_input())
l2 = Label(text = "",bg="#009f92")

show_plot = Button(root, bg="#005366", height = 2, fg = "#f7e7be", activebackground="#003E4D",
                 width = 39,
                 text ="Show Top 10 Movies",
                 command = lambda:plot())
l3 = Label(text = "",bg="#009f92")

l4.pack()
l.pack()
inputtxt.pack()
l1.pack()
Display.pack()
l2.pack()
Output.pack()
l3.pack()
show_plot.pack()

root.mainloop()
