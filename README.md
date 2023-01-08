
# Restaurant Rating Prediction

# Objective

The main goal of this project is to perform extensive Exploratory Data Analysis(EDA) on 
the Zomato Dataset and build an appropriate Machine Learning Model that will help 
various Zomato Restaurants to predict their respective Ratings based on certain 
features.

[You can reach the application here] 
[https://restaurantratingpredictionapp.herokuapp.com/](https://restaurantratingpredictionapp.herokuapp.com/)


# Problem statement
The basic idea of analyzing the Zomato dataset is to get a fair idea about the factors affecting the establishment
of different types of restaurant at different places in Bengaluru, aggregate rating of each restaurant, Bengaluru
being one such city has more than 12,000 restaurants with restaurants serving dishes from all over the world.
With each day new restaurants opening the industry has’nt been saturated yet and the demand is increasing
day by day. Inspite of increasing demand it however has become difficult for new restaurants to compete with
established restaurants. Most of them serving the same food. Bengaluru being an IT capital of India. Most of
the people here are dependent mainly on the restaurant food as they don’t have time to cook for themselves.
With such an overwhelming demand of restaurants it has therefore become important to study the demography
of a location. What kind of a food is more popular in a locality. Do the entire locality loves vegetarian food.
If yes then is that locality populated by a particular sect of people for eg. Jain, Marwaris, Gujaratis who are
mostly vegetarian. These kind of analysis can be done using the data, by studying the factors such as

- Location of the restaurant
- Approx Price of food
- Theme based restaurant or not
- Which locality of that city serves that cuisines with maximum number of restaurants
- The needs of people who are striving to get the best cuisine of the neighborhood
- Is a particular neighborhood famous for its own kind of food.


# Steps to involved in model building
- Data Loading
- Data transformation
- Data transformation
- New feature Generation
- Feature Engineering
- Model Building
- Evaluting Model
- Flask setup
- Push to Github
- deploying

# Snippets of Project

1)Webapp Home page
![img](https://i.imgur.com/s2tV3Y0.png)

2)API Home page
![img](https://i.imgur.com/ksIMzTe.png)


# Demo

## Demo Video link: [https://youtu.be/3G4nL-3utks](https://youtu.be/3G4nL-3utks)

## API Demo

```python
import requests
parameters={'online_order':"Yes",'book_table':"Yes",'MealType':"Buffet",'votes':775,'costfor2':800}
response = requests.get("https://restaurantratingpredictionapp.herokuapp.com/api/predict", params=parameters)
rating=response.text
print(rating)

```
### Output:
```bash
{"Prediction":{"0":3.6982960449}}
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/Ganesh-Thorat-01/Restaurant-Rating-Prediction
```

Go to the project directory

```bash
  cd Restaurant-Rating-Prediction
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python main.py
```


## Acknowledgements

The data scraped was entirely for educational purposes only. Note that I don’t claim any copyright for the data. All copyrights for the data is owned by Zomato Media Pvt. Ltd..


## Authors

- [@Ganesh-Thorat-01](https://github.com/Ganesh-Thorat-01/)

## Feedback

If you have any feedback, please reach out to us at thorat.ganeshscoe@gmail.com

