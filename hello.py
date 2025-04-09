from flask import Flask
app = Flask(__name__)
@app.route("/")#URL leading to method
def hello(): # Name of the method
 return("Hello ! \n Sunil here ... \n from Flask App! \n and python file stored in git") #indent this line
if __name__ == "__main__":
 #app.run(host='0.0.0.0', port='8080') 
    app.run(ssl_context=("cert.pem", "key.pem"), debug=True)
