from flask import Flask,jsonify,request
from flask_cors import CORS
import requests


app=Flask(__name__)

CORS(app)