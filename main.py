import os
import requests
from colors import *

import datetime
import threading

import json
import pandas as pd

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
    api_url = "https://replit.com/graphql"
    headers = {'X-Requested-With': 'replit',
               'Origin': 'https://replit.com',
               'Accept': 'application/json',
               'Referrer': 'https://replit.com',
               'Content-Type': 'application/json',
               'Connection': 'keep-alive',
               'Host':"replit.com",
               "x-requested-with": "XMLHttpRequest",
               "User-Agent": "Mozilla/5.0",
               "Cookie": f"connect.sid=${os.environ['gql_token']}"
	}
    query = """query UserByUsername($username: String!) {userByUsername(username: $username) {followerCount, isFollowingCurrentUser}}"""
    variables = {"username":username}
    res = requests.post(api_url,json={'query': query,'variables':variables},headers=headers)
    data = json.loads(res.text)
    data = {"response":{"status":res.status_code},"data":data}
    return data

def logger(username):
    dt = datetime.datetime.now()
    with open("log.txt","a+") as f:
        dt_string = dt.strftime("%d/%m/%Y | %H:%M:%S")
        logText = f"\nRequest: {username} - {dt}"
        f.write(logText)

from flask import Flask, send_file, redirect, render_template, request, jsonify, abort

template_dir = os.path.abspath('./')
app = Flask(__name__, template_folder=template_dir)

@app.route("/api/<username>")
def api(username):
    logger(username)
    printit(username)
    print(f"REQUEST: {username}")
    global yo;
    return str(yo)
@app.route('/api/gql/<username>')
def gqlAPI(username):
    logger(username)
    data = GQLver(username)
    query = request.args.get("q")
    if request.args.get("q"):
        try: data = data["data"]["data"]["userByUsername"][query]
        except KeyError:return abort(404)
    else:pass
    data = jsonify(data)
    return data

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        username = request.form["replituser"]
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
