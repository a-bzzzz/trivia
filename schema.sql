CREATE TABLE roles (  
    id SERIAL PRIMARY KEY,
    role_name VARCHAR(10) NOT NULL UNIQUE,
    visible BOOLEAN DEFAULT TRUE
);

INSERT INTO roles(role_name) VALUES ('admin');
INSERT INTO roles(role_name) VALUES ('superuser');
INSERT INTO roles(role_name) VALUES ('user');
INSERT INTO roles(role_name) VALUES ('visitor');

CREATE TABLE users (  
    id SERIAL PRIMARY KEY,
    username VARCHAR(20) NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role_id INTEGER DEFAULT 3 REFERENCES roles (id),
    visible BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW() 
);

CREATE TABLE categories (    
    id SERIAL PRIMARY KEY,
    category_name VARCHAR(30) NOT NULL UNIQUE,
    visible BOOLEAN DEFAULT TRUE
);

INSERT INTO categories(category_name) VALUES ('tiede/maantiede');
INSERT INTO categories(category_name) VALUES ('historia');
INSERT INTO categories(category_name) VALUES ('urheilu/vapaa-aika/ruoka');
INSERT INTO categories(category_name) VALUES ('musiikki/taide//kirjallisuus');
INSERT INTO categories(category_name) VALUES ('elokuvat/TV/viihde');
INSERT INTO categories(category_name) VALUES ('satunnainen aihe');

CREATE TABLE levels (   
    id SERIAL PRIMARY KEY,
    level_name VARCHAR(10) NOT NULL UNIQUE,
    visible BOOLEAN DEFAULT TRUE
);

INSERT INTO levels(level_name) VALUES ('helppo');
INSERT INTO levels(level_name) VALUES ('keskitaso');
INSERT INTO levels(level_name) VALUES ('vaikea');


CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    points INTEGER DEFAULT 0,
    answers_count INTEGER DEFAULT 0,
    session_count INTEGER DEFAULT 0,
    category_id INTEGER REFERENCES categories(id) ON DELETE CASCADE,
    level_id INTEGER REFERENCES levels(id) ON DELETE CASCADE,
    visible BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    answer TEXT NOT NULL,
    correct BOOLEAN DEFAULT FALSE,
    visible BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE questions (    
    id SERIAL PRIMARY KEY,
    question VARCHAR(150) NOT NULL,
    category_id INTEGER REFERENCES categories (id),
    level_id INTEGER REFERENCES levels (id),
    creator INTEGER REFERENCES users (id) DEFAULT 1,
    visible BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE questions_answers (
    question_id INTEGER REFERENCES questions(id) ON DELETE CASCADE,
    answer_id INTEGER REFERENCES answers(id) ON DELETE CASCADE
);

CREATE TABLE games_questions (
    game_id INTEGER REFERENCES games(id) ON DELETE CASCADE,
    question_id INTEGER REFERENCES questions(id) ON DELETE CASCADE
);

INSERT INTO answers (answer) VALUES ('Helsinki');
INSERT INTO answers (answer) VALUES ('Viipuri');
INSERT INTO answers (answer, correct) VALUES ('Turku', True);

INSERT INTO questions (question, category_id, level_id) VALUES ('Suomen ensimmäinen pääkaupunki?', 1, 1);

INSERT INTO questions_answers (question_id, answer_id) VALUES (1, 1);
INSERT INTO questions_answers (question_id, answer_id) VALUES (1, 2);
INSERT INTO questions_answers (question_id, answer_id) VALUES (1, 3);


CREATE TABLE stats (
    game_id INTEGER REFERENCES games(id) ON DELETE CASCADE,
    player_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
