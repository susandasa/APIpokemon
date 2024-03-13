from flask import Flask, render_template, request
import requests
import mysql.connector

app = Flask(__name__)

# MySQL Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Password for your MySQL database
    database="apipokemon",
    port=3306
)
cursor = db.cursor()

@app.route('/pokemon', methods=['GET', 'POST'])
def page_pokemon():
    if request.method == 'POST':
        pokemon_name = request.form.get('nama_pokemon')
        return get_and_save_pokemon(pokemon_name)
    return render_template('pokemonpage.html')

def fetch_pokemon_data(pokemon_name):
    api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(api_url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return {
            'name': pokemon_data['name'],
            'id': pokemon_data['id'],
            'types': [t['type']['name'] for t in pokemon_data['types']],
            'abilities': [a['ability']['name'] for a in pokemon_data['abilities']]
        }
    else:
        return None

def save_pokemon_to_database(pokemon_data):
    # Insert data into the MySQL database
    query = "INSERT INTO pokemon_table (id, pokemon_name, types, abilities) VALUES (%s, %s, %s, %s)"
    values = (pokemon_data['id'], pokemon_data['name'], ', '.join(pokemon_data['types']), ', '.join(pokemon_data['abilities']))
    cursor.execute(query, values)
    # Commit the changes to the database
    db.commit()

def get_and_save_pokemon(pokemon_name):
    pokemon_data = fetch_pokemon_data(pokemon_name)

    if pokemon_data:
        save_pokemon_to_database(pokemon_data)
        return render_template('index.html', data=pokemon_data)
    else:
        return render_template('error.html', error_message='Pokemon not found'), 404

if __name__ == '__main__':
    app.run(debug=True)
