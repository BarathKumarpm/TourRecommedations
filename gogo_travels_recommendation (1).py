import requests
from bs4 import BeautifulSoup
import pandas as pd

!pip install requests

!pip install scrapy-poet

r = requests.get("https://www.holidify.com/country/italy/places-to-visit.html")
print(r)

print(r.content)



soup = BeautifulSoup(r.content, "html.parser")
print(soup)

print(soup.prettify())

import random

user_ids = [random.randint(1, 200) for _ in range(1087)]

user_ids_list = list(user_ids)
print(user_ids_list)
print(len(user_ids_list))

has_duplicates = len(user_ids) != len(set(user_ids))

if has_duplicates:
    print("The list contains duplicates.")
else:
    print("The list does not contain duplicates.")

def scrape_page(url2):
    response = requests.get(url2)
    soup = BeautifulSoup(response.content, "html.parser")

    cities = []
    ratings = []
    image_urls = []

    attractions = soup.find_all("div", class_="card content-card")
    for attraction in attractions:
        city = attraction.find("h3", class_="card-heading").text.strip().split(". ")[1]
        image_url = attraction.find("img", class_="card-img-top").get("data-original")

        cities.append(city)
        ratings.append(ratings)
        image_urls.append(image_url)

    return cities, ratings, image_urls

urls2 = [
    "https://www.holidify.com/country/italy/places-to-visit.html?pageNum=0",
    "https://www.holidify.com/country/italy/places-to-visit.html?pageNum=1",
    "https://www.holidify.com/country/italy/places-to-visit.html?pageNum=2",
    "https://www.holidify.com/country/italy/places-to-visit.html?pageNum=3",
    "https://www.holidify.com/country/spain/places-to-visit.html?",
    "https://www.holidify.com/country/spain/places-to-visit.html?pageNum=1",
    "https://www.holidify.com/country/spain/places-to-visit.html?pageNum=2"
    "https://www.holidify.com/country/france/places-to-visit.html",
    "https://www.holidify.com/country/france/places-to-visit.html?pageNum=1",
    "https://www.holidify.com/country/france/places-to-visit.html?pageNum=2"
    "https://www.holidify.com/country/germany/places-to-visit.html?pageNum=0",
    "https://www.holidify.com/country/germany/places-to-visit.html?pageNum=1",
    "https://www.holidify.com/country/germany/places-to-visit.html?pageNum=2",
    "https://www.holidify.com/country/austria/places-to-visit.html",
    "https://www.holidify.com/country/poland/places-to-visit.html",
    "https://www.holidify.com/country/hungary/places-to-visit.html",
    "https://www.holidify.com/country/switzerland/places-to-visit.html",
    "https://www.holidify.com/country/england/places-to-visit.html",
    "https://www.holidify.com/country/england/places-to-visit.html?pageNum=1",
    "https://www.holidify.com/country/england/places-to-visit.html?pageNum=2"
    "https://www.holidify.com/country/scotland/places-to-visit.html",
    "https://www.holidify.com/country/netherlands/places-to-visit.html",
    "https://www.holidify.com/country/norway/places-to-visit.html",
    "https://www.holidify.com/country/sweden/places-to-visit.html",
    "https://www.holidify.com/country/belgium/places-to-visit.html",
    "https://www.holidify.com/country/iceland/places-to-visit.html",
    "https://www.holidify.com/country/turkey/places-to-visit.html",
    "https://www.holidify.com/country/greece/places-to-visit.html",
    "https://www.holidify.com/country/greece/places-to-visit.html?pageNum=1",
    "https://www.holidify.com/country/portugal/places-to-visit.html",
    "https://www.holidify.com/country/india/places-to-visit.html",
    "https://www.holidify.com/country/india/places-to-visit.html?pageNum=1",
    "https://www.holidify.com/country/india/places-to-visit.html?pageNum=1",
    "https://www.holidify.com/country/usa/places-to-visit.html",
    "https://www.holidify.com/country/usa/places-to-visit.html?pageNum=1",
    "https://www.holidify.com/country/usa/places-to-visit.html?pageNum=2",
    "https://www.holidify.com/country/malaysia/places-to-visit.html",
    "https://www.holidify.com/country/malaysia/places-to-visit.html?pageNum=1",
    "https://www.holidify.com/country/thailand/places-to-visit.html",
    "https://www.holidify.com/country/thailand/places-to-visit.html?pageNum=1",
    "https://www.holidify.com/country/vietnam/places-to-visit.html",
    "https://www.holidify.com/country/vietnam/places-to-visit.html?pageNum=1",
    "https://www.holidify.com/country/japan/places-to-visit.html",
    "https://www.holidify.com/country/cambodia/places-to-visit.html",
    "https://www.holidify.com/country/china/places-to-visit.html"
    "https://www.holidify.com/country/south-africa/places-to-visit.html",
    "https://www.holidify.com/country/south-africa/places-to-visit.html?pageNum=1",
    "https://www.holidify.com/country/south-korea/places-to-visit.html"
]

cities2 = []
ratings2 = []
image_urls2 = []

for url in urls2:
    cities, ratings, image_urls = scrape_page(url)
    cities2.extend(cities)
    ratings2.extend(ratings)
    image_urls2.extend(image_urls)

# Create DataFrame
data = {
    "User_IDs": user_ids_list,
    "City": cities2,
    "User_Rating": ratings2,
    "Image_URL": image_urls2
}

df = pd.DataFrame(data)
df

#df.to_csv('data.csv', index=False)

#df.to_excel('data.xlsx', index=False)

df1 = pd.read_csv('data.csv')
df1

df1.describe()

df.shape

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Example DataFrame obtained from scraping
# Replace this with your actual DataFrame
data = {
    "User_IDs": [1, 2, 3, 4, 5],
    "City": ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'],
    "User_Rating": [5, 4, 3, 2, 1],
    "Image_URL": ['url1', 'url2', 'url3', 'url4', 'url5']
}

df2 = pd.DataFrame(data)

# Convert city names to lowercase for consistency
df2['City'] = df2['City'].str.lower()

# Initialize TfidfVectorizer to convert city names to numerical features
tfidf = TfidfVectorizer(stop_words='english')

# Fit and transform city names to TF-IDF vectors
tfidf_matrix = tfidf.fit_transform(df['City'])

# Compute cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to recommend cities to a user based on user ID
def recommend_cities(user_id, cosine_sim=cosine_sim):
    idx = df[df['User_IDs'] == user_id].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Exclude self and take top 3 similar cities
    city_indices = [i[0] for i in sim_scores]
    return df.iloc[city_indices]

# Example: Recommend cities to User ID 1
recommendations = recommend_cities(1)
print(recommendations)

!pip install gunicorn

!gunicorn -w 4 -b 127.0.0.1:5000 app:app

from flask import Flask, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)

# Example DataFrame obtained from scraping
# Replace this with your actual DataFrame
data = {
    "User_IDs": [1, 2, 3, 4, 5],
    "City": ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'],
    "User_Rating": [5, 4, 3, 2, 1],
    "Image_URL": ['url1', 'url2', 'url3', 'url4', 'url5']
}

df3 = pd.DataFrame(data)

# Convert city names to lowercase for consistency
df3['City'] = df3['City'].str.lower()

# Initialize TfidfVectorizer to convert city names to numerical features
tfidf = TfidfVectorizer(stop_words='english')

# Fit and transform city names to TF-IDF vectors
tfidf_matrix = tfidf.fit_transform(df['City'])

# Compute cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to recommend cities to a user based on user ID
def recommend_cities(user_id, cosine_sim=cosine_sim):
    idx = df[df['User_IDs'] == user_id].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Exclude self and take top 3 similar cities
    city_indices = [i[0] for i in sim_scores]
    return df.iloc[city_indices]

@app.route('/')
def index():
    # Example: Recommend cities to User ID 1
    recommendations = recommend_cities(1)
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)

import pickle

pickle.dump(recommendations,open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))



import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from IPython.display import HTML

# Example DataFrame obtained from scraping
# Replace this with your actual DataFrame
data = {
    "User_IDs": [1, 2, 3, 4, 5],
    "City": ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'],
    "User_Rating": [5, 4, 3, 2, 1],
    "Image_URL": ['url1', 'url2', 'url3', 'url4', 'url5']
}

df4 = pd.DataFrame(data)

# Convert city names to lowercase for consistency
df4['City'] = df4['City'].str.lower()

# Initialize TfidfVectorizer to convert city names to numerical features
tfidf = TfidfVectorizer(stop_words='english')

# Fit and transform city names to TF-IDF vectors
tfidf_matrix = tfidf.fit_transform(df['City'])

# Compute cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to recommend cities to a user based on user ID
def recommend_cities(user_id, cosine_sim=cosine_sim):
    idx = df[df['User_IDs'] == user_id].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Exclude self and take top 3 similar cities
    city_indices = [i[0] for i in sim_scores]
    return df.iloc[city_indices]

recommendations = recommend_cities(2)

html_recommendations = recommendations.to_html()

HTML(html_recommendations)

!pip install modelbit

import modelbit
mb = modelbit.login()

from IPython.display import display, HTML

# Define the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recommendations</title>
    <style>
        body {
            background-color: #fff; /* White background */
        }
        .top-bar {
            background-color: #ff00ff; /* Magenta top bar */
            padding: 10px;
            text-align: center;
            color: #fff; /* White text color */
            margin-bottom: 20px;
        }
        .card-container {xa
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            grid-gap: 20px;
            padding: 20px;
        }
        .card {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            transition: 0.3s;
        }
        .card:hover {
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
        }
        .card-image {
            width: 100%;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="top-bar">
        <h1>Recommendations</h1>
    </div>
    <div class="card">
        <h2>Venice</h2>
        <img class="card-image" src="https://www.holidify.com/images/bgImages/VENICE.jpg" alt="City Image">
        <p>User Rating: 3.2</p>
    </div>
    <div class="card">
        <h2>Rome</h2>
        <img class="card-image" src="https://www.holidify.com/images/bgImages/ROME.jpg" alt="City Image">
        <p>User Rating: 3.2</p>
    </div>
    <div class="card">
        <h2>Milan</h2>
        <img class="card-image" src="https://www.holidify.com/images/bgImages/MILAN.jpg" alt="City Image">
        <p>User Rating: 3.2</p>
    </div>
</body>
</html>
"""

# Display the HTML content
display(HTML(html_content))

