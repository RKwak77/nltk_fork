import os
import sys
import types

# Path to your local nltk package directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NLTK_DIR = os.path.join(BASE_DIR, "nltk")

# 1) Lightweight 'nltk' shim (only if using a local fork)
nltk = types.ModuleType("nltk")
nltk.__path__ = [NLTK_DIR]
sys.modules["nltk"] = nltk

# 2) Direct import from the casual tokenizer module
from nltk.tokenize.casual import TweetTokenizer

# 3) Create tokenizer instance
tokenizer = TweetTokenizer()

# 4) Emoji test cases
test_cases = [
    "😂🔥💯",
    "Hello 😂🔥💯!!!",
    "Let's grab coffee ☕️ later 😊",
    "I can't believe it!!! 😱😱😱",
    "❤️💔💕💞💖💗💙💚💛💜🖤",
    "Flags are cool 🇺🇸🇬🇧🇳🇬",
    "Family 👨‍👩‍👧‍👦 emojis join together",
    "Custom combo 👍🏽😂🔥",
    "Good morning ☀️🌈🌻",
    "No emoji here at all.",
]

# 5) Run tests
for i, text in enumerate(test_cases, 1):
    tokens = tokenizer.tokenize(text)
    print(f"\nTest {i}: {text}")
    print(tokens)
