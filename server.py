from flask import Flask #from flask app import and use the Flask section

app = Flask(__name__) #__name__ this is using the name of the folder

#interface
@app.get("/")
def home():
    return "Hello from flask"


app.run(debug=True) #This applies the code changes to the live server
