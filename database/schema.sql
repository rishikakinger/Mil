CREATE DATABASE safety_toy;


USE safety_toy;


CREATE TABLE incidents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    audio_text TEXT,
    image_path VARCHAR(255),
    severity FLOAT,
    distance FLOAT,
    touch_type ENUM('good', 'bad')
);