\c tasks_db;

CREATE TABLE users (
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    password TEXT NOT NULL,
    email VARCHAR(50) NOT NULL
);

CREATE TABLE tasks (
    id SERIAL NOT NULL PRIMARY KEY,
    user_id INTEGER REFERENCES users (id),
    title VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    finished BOOLEAN NOT NULL DEFAULT FALSE
);