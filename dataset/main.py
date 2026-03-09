from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
#Basemodel -- to define schema
from pydantic import BaseModel
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd 

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)



##to read .csv file

df=pd.read_csv("HouseData.csv")
#print(df)

X=df[["size","bedrooms","age"]]
y=df["price"]


#To train our model
model = LinearRegression()
model.fit(X,y)

# to define schema
class HouseInput(BaseModel):
    size : float
    bedrooms : int 
    age : int

# to creat epost request


# @app.get("/")
# def home():
#     return {"message": "House Price Prediction API is running"}

@app.post("/predict")
def predict_price(input:HouseInput):
    features = np.array([[input.size, input.bedrooms, input.age]])
    price=model.predict(features)

    return {
    "predicted_price" : int(price[0])
    }