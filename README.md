# Language Detection Project

This project implements a simple language detection tool in Python. Using the `langdetect` and `langcodes` libraries, it detects the language of a given text and maps language codes to their full names. This tool can be useful in multilingual NLP applications, content filtering, and language-aware routing.

## Features
- **Automatic Language Detection**: Detects the language of a given text input.
- **Language Code Mapping**: Converts detected language codes (e.g., `en`) to full language names (e.g., `English`).
- **Error Handling**: Provides an error message if the language cannot be detected (e.g., for very short or ambiguous text).

## Requirements
Make sure to install the following Python libraries before running the project:

```bash
pip install langdetect langcodes

