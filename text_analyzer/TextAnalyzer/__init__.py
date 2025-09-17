from .config.settings import Config
from .core.analyzer import TextAnalyzer
from .utils.text_ops import (clean_text, extract_sentences, extract_urls,
                             fetch_web_content, remove_stopwords)

__version__ = "0.1.0"
__all__ = [
    "TextAnalyzer",
    "clean_text",
    "extract_urls",
    "fetch_web_content",
    "remove_stopwords",
    "extract_sentences",
    "Config",
]
