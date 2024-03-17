from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample of Video Games
videogames = [
    {'title': "Halo 3", 
     'developer': "Bungie",
     'platform': "Xbox 360",
     'genre': "First-Person Shooter",
     'release_date': "09/25/2007"
     },

     {'title': "The Witcher 3 - Wild Hunt", 
     'developer': "CD Projekt Red",
     'platform': "Multiple",
     'genre': "Role-Playing",
     'release_date': "05/19/2015"
     },
]

# Our route home
@app.route('/')
def home():
    return render_template('home.html', videogames=videogames)

# Our route for adding a video game
@app.route('/add_game', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        title = request.form['title']
        developer = request.form['developer']
        platform = request.form['platform']
        genre = request.form['genre']
        release_date = request.form['release_date']

        # Create a new game dictionary
        new_game = {'title': title, 
                    'developer': developer, 
                    'platform': platform,
                    'genre': genre,
                    'release_date': release_date
                    }
        
        # Add the new video game to the list of video games.
        videogames.append(new_game)

        # Redirect to the home page after adding the game
        return redirect(url_for('home'))
    return render_template('add_game.html')


if __name__ == '__main__':
    app.run(debug=True)
