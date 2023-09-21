from flask import Flask, render_template, redirect, request, url_for, session
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase


app = Flask(__name__)
app.config["SECRET_KEY"]='1e5a3bd7e61ef7ca7e421333af331d2a'
socketio = SocketIO(app)

@app.route('/',methods=["GET","POST"])
def index():
    return render_template("home.html")


if __name__=="__main__":
    socketio.run(app, debug=True)