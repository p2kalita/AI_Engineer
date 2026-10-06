
from strands import tool


@tool
def text_count(text: str) -> dict:
    """Count the number of words, sentences, and characters in a text.

    Args:
        text: The text to analyze
    """
    words = len(text.split())
    sentences = text.count(".") + text.count("!") + text.count("?")
    characters = len(text)

    return {
        "words": words,
        "sentences": sentences,
        "characters": characters,
    }