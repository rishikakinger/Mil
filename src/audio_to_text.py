import speech_recognition as sr

def record_and_convert_to_text(audio_filename="audio.wav"):

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recording... Speak now!")
        audio = recognizer.listen(source)
        print("Recording finished.")

        with open(audio_filename, "wb") as f:
            f.write(audio.get_wav_data())

        try:
            text = recognizer.recognize_google(audio)
            print(f"Converted text: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
            return None