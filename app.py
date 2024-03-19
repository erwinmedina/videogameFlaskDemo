from flask import Flask, jsonify, render_template, request, redirect, url_for
from db import get_games_route, add_game_route, add_bulkGame, get_game, delete_game, update_game
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'erwinmedina'
app.config['MYSQL_DB'] = 'video_games'

# Initialize MySQL
mysql = MySQL(app)

@app.route('/', methods=["GET"])
def home():
    games = get_games_route()
    return render_template('home.html', games=games)

if __name__ == '__main__':
    app.run(debug=True)
