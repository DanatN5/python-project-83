CREATE TABLE IF NOT EXISTS urls (
    id int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name text UNIQUE NOT NULL,
    created_at date DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS url_checks (
    id int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    url_id int REFERENCES urls(id) ON DELETE CASCADE,
    status_code int,
    h1 text,
    title text,
    description text,
    created_at date DEFAULT CURRENT_TIMESTAMP
);