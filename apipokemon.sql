CREATE DATABASE IF NOT EXISTS apipokemon;
USE apipokemon;

CREATE TABLE IF NOT EXISTS pokemon_table (
    id INT PRIMARY KEY,
    pokemon_name VARCHAR(255) NOT NULL,
    TYPES VARCHAR(255) NOT NULL,
    abilities VARCHAR(255) NOT NULL
);

SELECT * FROM pokemon_table;
