from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'erwinmedina'
app.config['MYSQL_DB'] = 'video_games'

# Initialize MySQL
mysql = MySQL(app)

# ******************************* #
# Creates the game table in MySql #
# ******************************* #
with app.app_context():
    cur = mysql.connection.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS games (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            developer VARCHAR(255) NOT NULL,
            platform VARCHAR(255) NOT NULL,
            genre VARCHAR(255) NOT NULL,
            release_date VARCHAR(255) NOT NULL
        )
    """)
    mysql.connection.commit()

# ************************************* #
# Returns all games within the database #
# ************************************* #
@app.route('/api/games', methods=['GET'])

def get_games():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM games")
    games = cur.fetchall()
    
    games_list = []
    for game in games:
        game_dict = {
            'id': game[0],
            'title': game[1],
            'developer': game[2],
            'platform': game[3],
            'genre': game[4],
            'release_date': game[5]
        }
        games_list.append(game_dict)
    cur.close()
    return jsonify(games_list)

# ********************************** #
# Posts a game to the MySQL Database #
# ********************************** #
@app.route('/api/games', methods=['POST'])
def add_game():

    data = request.json
    title = data.get('title')
    developer = data.get('developer')
    platform = data.get('platform')
    genre = data.get('genre')
    release_date = data.get('release_date')
    
    if title and developer and platform and genre and release_date:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO games(title, developer, platform, genre, release_date) VALUES (%s, %s, %s, %s, %s)", (title, developer, platform, genre, release_date))
        mysql.connection.commit()
        cur.close()
        return jsonify({'Message': 'Video game added successfully'}), 201
    else:
        return jsonify({'Error': 'Missing required fields'}), 400
 
# ********************************* #
# Returns a single game by ID value # 
# ********************************* #
@app.route('/api/games/<int:game_id>', methods=['GET'])
def get_game(game_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM games WHERE id = %s", (game_id,))
    game = cur.fetchone()
    cur.close()
    if game:
        return jsonify(game)
    else:
        return jsonify({'Error': 'Game not found'}), 404


# ********************************* #
# Deletes a single game by ID value #
# ********************************* #
@app.route('/api/games/<int:game_id>', methods=["DELETE"])
def delete_game(game_id):
    cur = mysql.connection.cursor()
    try:
        cur.execute("DELETE FROM games WHERE id = %s", (game_id,))
        mysql.connection.commit()
        return jsonify({'Message': 'Video game deleted successfully'}), 204
    except Exception as e:
        print(e)
        if 'No data' in str(e):
            return jsonify({'Error': 'Game ID is not valid!'}), 404
        else:
            return jsonify({"Error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True)
