import os
import requests
from colors import *

import threading

global yo;
yo = 0;

def printit(username):
  threading.Timer(2.0, printit,).start()
  profile = requests.get(f"https://replit.com/@{username}").text
  global yo;
  
  yo = profile[profile.find('followerCount')+15: profile.find('followerCount')+30].lower().replace('a','').replace('b','').replace('c','').replace('d','').replace('e','').replace('f','').replace('g','').replace('h','').replace('i','').replace('j','').replace('k','').replace('l','').replace('m','').replace('n','').replace('o','').replace('p','').replace('q','').replace('r','').replace('s','').replace('t','').replace('u','').replace('v','').replace('w','').replace('x','').replace('y','').replace('z','').replace(',','').replace('"','')

  print(f"{bright_blue}e {Blue}e{bright_blue}:{bright_yellow}",yo,reset,"\n")


from flask import Flask, send_file, redirect, render_template, request

template_dir = os.path.abspath('./')
app = Flask(__name__, template_folder=template_dir)

@app.route("/api/<username>")
def api(username):
    printit(username)
    print(f"REQUEST: {username}")
    with open("log.txt","a") as f:
        f.write(f"\nRequest: {username}")
    global yo;
    return str(yo)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        return redirect(f'/{username}')
    return render_template('first.html')
@app.route("/<username>")
def index(username):
    if username == None:
        return redirect('/CosmicBear')
    #entry = os.path.join('index.html')
    return render_template("index.html",username=username)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

