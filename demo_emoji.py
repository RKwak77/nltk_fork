import os
import sys
import types

# Path to your local nltk package directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NLTK_DIR = os.path.join(BASE_DIR, "nltk")

# 1) Lightweight 'nltk' package pointing at local code
if "nltk" not in sys.modules:
    nltk = types.ModuleType("nltk")
    nltk.__path__ = [NLTK_DIR]
    sys.modules["nltk"] = nltk

# 2) Ensure project root is on sys.path
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# 3) Import directly from the casual tokenizer module
from nltk.tokenize.casual import TweetTokenizer

# ✅ 4) Create the tokenizer instance (you forgot this line)
tokenizer = TweetTokenizer()

# 5) Additional tests for emoji-aware tokenization
test_cases = [
    "😂🔥💯",  # Only emojis
    "Hello 😂🔥💯!!!",  # Mixed with punctuation
    "Let's grab coffee ☕️ later 😊",  # Word + emoji + variation selector
    "I can't believe it!!! 😱😱😱",  # Repeated emojis
    "❤️💔💕💞💖💗💙💚💛💜🖤",  # Different heart emojis
    "Flags are cool 🇺🇸🇬🇧🇳🇬",  # Multi-codepoint flag emojis
    "Family 👨‍👩‍👧‍👦 emojis join together",  # Zero-width joiner sequences
    "Custom combo 👍🏽😂🔥",  # Skin tone + emojis
    "Good morning ☀️🌈🌻",  # Common emoji set
    "No emoji here at all.",  # Control: plain text
]

# 6) Run tests
for i, text in enumerate(test_cases, 1):
    tokens = tokenizer.tokenize(text)
    print(f"\nTest {i}: {text}")
    print(tokens)
