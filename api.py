from flask import Flask, jsonify, request, redirect, url_for

app = Flask(__name__)

# Sample list of games
games = [
     {'title': "The Witcher 3 - Wild Hunt", 
     'developer': "CD Projekt Red",
     'platform': "Multiple",
     'genre': "Role-Playing",
     'release date': "05/19/2015"
     },     
     {'title': "The Witcher 3 - Wild Hunt", 
     'developer': "CD Projekt Red",
     'platform': "Multiple",
     'genre': "Role-Playing",
     'release date': "05/19/2015"
     },
]

' This is the get route '
@app.route('/api/games', methods=['GET'])

def get_games():
    # Get query parameters for developers
    developers = request.args.getlist('developer')
    if developers:
        # Filter games by developers if developers are specified
        result = [game for game in games if game['developer'] in developers]
    else:
        # Return all games if no authors are specified
        result = games

    return jsonify(result)


@app.route('/api/games', methods=['POST'])
def add_game():

    data = request.json
    title = data.get('title')
    developer = data.get('developer')
    platform = data.get('platform')
    genre = data.get('genre')
    release_date = data.get('release date')
    
    if title and developer and platform and genre and release_date:
        new_game = {'title': title, 
                    'developer': developer, 
                    'platform': platform,
                    'genre': genre,
                    'release date': release_date
        }
        games.append(new_game)
        return jsonify({'Message': 'Game added successfully!'}), 201
    else:
        return jsonify({'Error': 'Missing required fields'}), 400


# @app.route('/api/games/<platform>', methods=['GET'])
# def get_game(platform):
#     # Find a list of games 
#     book = None
#     for b in books:
#         if b['isbn'] == isbn:
#             book = b
#             break
#     if book:
#         return jsonify(book)
#     else:
#         return jsonify({'error': 'Book not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
