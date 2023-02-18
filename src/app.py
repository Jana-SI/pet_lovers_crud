from flask import Flask, request, render_template, redirect
from src.db import *

app = Flask(__name__)

@app.errorhandler(404) 
def not_found(e): 
  return render_template('/public/404.html')