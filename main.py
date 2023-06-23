from flask import Flask 
from creditcard.logger.logs import logging
logging.info("Flask object is initiated")
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    logging.info("we are testing our logging file")
    return "HelloWorld"

if __name__ =="__main__":
    app.run(debug=True)
