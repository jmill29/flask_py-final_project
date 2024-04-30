import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    def test_joy(self):
        text = "I am glad this happened."
        dominantEmotion = emotion_detector(text)['dominant_emotion']
        self.assertEqual(dominantEmotion, 'joy')

    def test_anger(self):
        text = "I am really mad about this."
        dominantEmotion = emotion_detector(text)['dominant_emotion']
        self.assertEqual(dominantEmotion, 'anger')

    def test_disgust(self):
        text = "I feel disgusted just hearing about this."
        dominantEmotion = emotion_detector(text)['dominant_emotion']
        self.assertEqual(dominantEmotion, 'disgust')

    def test_sadness(self):
        text = "I am so sad about this."
        dominantEmotion = emotion_detector(text)['dominant_emotion']
        self.assertEqual(dominantEmotion, 'sadness')

    def test_fear(self):
        text = "I am really afraid that this will happen."
        dominantEmotion = emotion_detector(text)['dominant_emotion']
        self.assertEqual(dominantEmotion, 'fear')

if (__name__ == "__main__"):
    unittest.main()