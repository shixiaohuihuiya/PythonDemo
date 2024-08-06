import datetime
import logging
from flask import Flask, request
from core.mysql import session,User
import json


app = Flask(__name__)

# 返回所有的数据而且是可以进行数据接收
@app.route("/index",methods=["GET"])
def index():
    user = session.query(User).all()
    return user






if __name__ == '__main__':
    app.run(debug=True,port=6789,host="0.0.0.0")