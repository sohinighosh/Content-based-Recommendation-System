import numpy as np #giving alias name as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def title_index(index):
    return df[df.index ==index]["title"].values[0]#takes title from index
def index_title(title):
    return df[df.title ==title]["index"].values[0] #takes index from title
df=pd.read_csv("movie_dataset.csv")#reads the csv file which should be available in your workspace folder
X=['keywords','cast','genres','director']#the key points on which the movie is recommended
for X in X:
    df[X]=df[X].fillna(' ')#if any data containg Null or na value it would be rplaced by blank space
def all_X(row):
    try:
        return row['keywords']+" "+row["cast"]+" "+row["genres"]
    except: print("error", row)
df["all_X"]= df.apply(all_X,axis=1)
cv=CountVectorizer()
count_matrix=cv.fit_transform(df["all_X"])
cosine=cosine_similarity(count_matrix) 
movie_user_likes="Avatar"
movie_index=index_title(movie_user_likes)
similar_movies=list(enumerate(cosine[movie_index]))
sorted_similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)
i=0
for movie in sorted_similar_movies:
    print (title_index(movie[0]))
    i=i+1
    if i>10:
        break
