# Soft Toy Prototype

This project is a prototype for a soft toy designed to protect children by detecting potential instances of sexual and verbal harassment. The toy uses a Raspberry Pi, sensors, and machine learning models to provide real-time alerts to parents.

## Features

- **Distance Calculation**: Uses an ultrasonic sensor to detect when someone is too close to the child.
- **Hate Speech Detection**: Uses a fine-tuned BERT model to detect hate speech in audio input.
- **Touch Sensors**: Detects good and bad touch using sensors and provides feedback via a buzzer.
- **Audio-to-Text Conversion**: Converts recorded audio to text for analysis.
- **Twilio Integration**: Sends SMS alerts to parents when suspicious activity is detected.
- **MySQL Database**: Logs all incidents for future reference.

## Directory Structure

Millie/
│
├── database/
│   └── schema.sql                # SQL script to create the database and tables
│
├── src/
│   ├── db_connection.py          # Database connection logic
│   ├── distance_calculator.py    # Distance calculation using ultrasonic sensor
│   ├── touch_sensors.py          # Touch sensor logic and buzzer feedback
│   ├── hate_speech_detection.py  # Hate speech detection using NLP
│   ├── twilio_integration.py     # Twilio API for sending alerts
│   ├── main.py      
│   ├── finetune.py               # For finetuning the model on a local dataset
│   ├── audio_to_text.py          # For converting an incoming audio stream to text for processing
│
├── requirements.txt              
│
└── README.md


## Setup Instructions

### 1. **Hardware Setup**
- Connect the ultrasonic sensor, touch sensors, buzzer, microphone, and camera to the Raspberry Pi GPIO pins as specified in the code.
- Ensure the Raspberry Pi has internet access for Twilio and Google Web Speech API.

### 2. **Database Setup**
1. Install MySQL on your Raspberry Pi:
   ```bash
   sudo apt-get install mysql-server

2. Create the database and tables:
   ```bash
   mysql -u root -p < database/schema.sql

3. Run pip install -r requirements.txt

4. Twilio Setup
Sign up for a Twilio account at Twilio.
Replace the placeholders in twilio_integration.py with your Twilio account SID, auth token, and phone numbers.

5. cd into the src directory and run main.py





