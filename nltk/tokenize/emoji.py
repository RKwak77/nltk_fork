"""
Emoji utilities for NLTK tokenizers.

Provides:
- EMOJI_PATTERN: a regex pattern string that matches individual and combined emoji sequences.
- EMOJI_RE: a compiled regex for direct use.

This uses the 'regex' module, which supports Unicode properties beyond the built-in 're'.
"""

import regex

# Matches emoji characters and common emoji sequences, including:
# - standalone emoji (😀)
# - skin-tone modifiers (👍🏽)
# - zero-width joiner sequences (👨‍👩‍👧‍👦)
# - flags (🇳🇬, 🇺🇸)
# - keycaps (#️⃣, 1️⃣)
EMOJI_PATTERN = r"""
    (?:                           # non-capturing group
        [\p{Emoji_Presentation}\p{Emoji}\u200d]+   # core emoji or joined sequences
        (?:\ufe0f)?               # optional variation selector
    )
"""

# Compile the regex pattern with verbose and Unicode flags
EMOJI_RE = regex.compile(EMOJI_PATTERN, regex.UNICODE | regex.VERBOSE)

def contains_emoji(text: str) -> bool:
    """Return True if the text contains any emoji."""
    return bool(EMOJI_RE.search(text))

def extract_emojis(text: str):
    """Return a list of all emoji sequences found in the text."""
    return EMOJI_RE.findall(text)
