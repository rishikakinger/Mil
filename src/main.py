import time
from db_connection import get_db_connection

from distance_calculator import setup_distance_sensor, calculate_distance, cleanup as cleanup_distance

from touch_sensors import setup_touch_sensors, check_touch, buzz, cleanup as cleanup_touch

from hate_speech_detection import HateSpeechDetector
from twilio_integration import send_alert
from audio_to_text import record_and_convert_to_text

def log_incident(audio_text, image_path, severity, distance, touch_type):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO incidents (timestamp, audio_text, image_path, severity, distance, touch_type) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (time.strftime('%Y-%m-%d %H:%M:%S'), audio_text, image_path, severity, distance, touch_type)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def main():
    hate_speech_detector = HateSpeechDetector()


    setup_distance_sensor()
    setup_touch_sensors()

    try:
        while True:
            #check distance
            distance = calculate_distance()
            if distance < 50:  #if someone is within 50 cm
                print(f"someone is too close! Distance: {distance} cm")
                send_alert(f"someone is too close to your child! Distance: {distance} cm")

            touch_type = check_touch()
            if touch_type:
                print(f"{touch_type.capitalize()} touch detected!")
                if touch_type == "bad":
                    buzz(1000, 1)  #buzz- bad touch
                    send_alert(f"bad touch detected! Check on your child.")
                log_incident(None, None, 0, distance, touch_type)


            audio_text = record_and_convert_to_text()
            if audio_text:
                result = hate_speech_detector.detect_hate_speech(audio_text)
                if result['label'] == 'HATE' and result['score'] > 0.8:
                    print(f"hate speech detected: {audio_text}")
                    print(f"confidence: {result['score']:.4f}")
                    send_alert(f"hate speech detected: {audio_text}")
                    log_incident(audio_text, None, result['score'], distance, None)

            time.sleep(1)  

    except KeyboardInterrupt:
        print("exiting")
    finally:
        cleanup_distance()
        cleanup_touch()

if __name__ == "__main__":
    main()