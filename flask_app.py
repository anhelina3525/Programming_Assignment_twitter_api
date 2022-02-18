# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import main_func


app = Flask(__name__)

@app.route('/')
def display_map():
    return render_template('index.html')

@app.route('/going', methods=['POST'])
def going():
    nickname = request.form['name']
    main_func.display_locations(nickname)
    return render_template('friends_locations.html')
