import os
import requests
from colors import *

import datetime
import threading

global yo;
yo = 0;

current_version = "2.3.3"

def printit(username):
  threading.Timer(2.0, printit,).start()
  profile = requests.get(f"https://replit.com/@{username}").text
  global yo;
  
  yo = profile[profile.find('followerCount')+15: profile.find('followerCount')+30].lower().replace('a','').replace('b','').replace('c','').replace('d','').replace('e','').replace('f','').replace('g','').replace('h','').replace('i','').replace('j','').replace('k','').replace('l','').replace('m','').replace('n','').replace('o','').replace('p','').replace('q','').replace('r','').replace('s','').replace('t','').replace('u','').replace('v','').replace('w','').replace('x','').replace('y','').replace('z','').replace(',','').replace('"','')

  print(f"{bright_blue}e {Blue}e{bright_blue}:{bright_yellow}",yo,reset,"\n")

def GQLver(username):
    dataLoad = {}
    pass

from flask import Flask, send_file, redirect, render_template, request

template_dir = os.path.abspath('./')
app = Flask(__name__, template_folder=template_dir)

@app.route("/api/<username>")
def api(username):
    dt = datetime.datetime.now()
    printit(username)
    print(f"REQUEST: {username}")
    with open("log.txt","a+") as f:
        dt_string = dt.strftime("%d/%m/%Y | %H:%M:%S")
        logText = f"\nRequest: {username} - {dt_string}"
        f.write(logText)
    global yo;
    return str(yo)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        return redirect(f'/u/{username}')
    return render_template('first.html',version=current_version)
@app.get('/README.md')
def readmePage():
    with open("README.md","r") as f:
        return str(f.read())
@app.get("/about")
def aboutPage():
    return render_template('about.html')
@app.route("/u/<username>")
def index(username):
    '''if use/rname == None:
        return redirect('/CosmicBear')
    #entry = os.path.join('index.html')'''
    return render_template("index.html",username=username)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
