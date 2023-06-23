from flask import Flask 
from creditcard.logger.logs import logging
from creditcard.exception import CustomException
import os ,sys
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])

def index():
    try:
        logging.info("we are testing our logging file")
         #raise Exception ("we are testing our custom exception file")
    except Exception as e :
         customer=CustomException(e,sys)
         logging.info(customer.error_message)
         logging.info("we are testing logggign module")
         return "Hello world"
if __name__ =="__main__":
    app.run(debug=True)

