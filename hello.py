from flask import Flask
app = Flask(__name__)
@app.route("/")#URL leading to method
def hello(): # Name of the method
 return("Hello from Flask App! file stored in git") #indent this line
if __name__ == "__main__":
 app.run(host='0.0.0.0', port='8080') 
