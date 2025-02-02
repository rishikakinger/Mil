from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch

class HateSpeechDetector:
    def __init__(self, model_name="Hate-speech-CNERG/dehatebert-mono-english"):

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.classifier = pipeline('text-classification', model=self.model, tokenizer=self.tokenizer)

    def detect_hate_speech(self, text):
        
        try:
            result = self.classifier(text)[0]
            return {
                "label": result['label'],
                "score": result['score']
            }
        
        
        
        except Exception as e:
            print(f"Error during hate speech detection: {e}")
            return {
                "label": "ERROR",
                "score": 0.0
            }

    def analyze_text_batch(self, texts):
        results = []
        for text in texts:
            result = self.detect_hate_speech(text)
            results.append(result)
        return results


if __name__ == "__main__":
    detector = HateSpeechDetector()

    #Test 
    test_texts = [
        "I hate you!",
        "You are a wonderful person.",
        "People like you should not exist.",
        "Let's go out and have fun!"
    ]

    results = detector.analyze_text_batch(test_texts)

    for text, result in zip(test_texts, results):
        print(f"Text: {text}")
        print(f"Label: {result['label']}, Confidence: {result['score']:.4f}")
        print("-" * 50)