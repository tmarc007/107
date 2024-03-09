from flask import Flask, request #from flask app import and use the Flask section. And from flask import (library) request
import json

app = Flask(__name__) #__name__ this is using the name of the folder

#interface
@app.get("/")
def home():
    return "Hello from flask"
# hello

@app.get("/testing")
def test():
    return "Hello from another page"

# Create 2 more API (About and Blog)
@app.get("/about")
def about():
    me={
    "first_name":"Tom",
    "month":"July",
    "last_name":"Marcello",
    "age":21,
}
    return json.dumps(me)

@app.get("/blog")
def blog():
    return "Welcome to my page"

@app.get("/version")
def version():
    version = {
        "name": "mouse", "version": "2","build": 123456
    }
    return json.dumps(version)

# This time we need to read and write onto the server. Creat a new API. Make a list.
products = []
@app.get("/sampleAPI/products") # This will read.
def get_products():
    return json.dumps(products)

@app.post("/sampleAPI/products") #This will write.
def save_products(): # This will save a new product
    product = request.get_json() # Here we are writing/pushing to the server
    print (product)
    #mock the save
    products.append(product)
    return json.dumps(product)






app.run(debug=True) # Applies code changes to a live server

# API / Endpoint (ie. @app.get("/testing")
# transform JSON / Convert JSON into an object again.
