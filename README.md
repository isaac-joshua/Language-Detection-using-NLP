Language Detection Project
This project implements a simple language detection tool in Python. Using the langdetect and langcodes libraries, it detects the language of a given text and maps language codes to their full names. This tool can be useful in multilingual NLP applications, content filtering, and language-aware routing.

Features
Automatic Language Detection: Detects the language of a given text input.
Language Code Mapping: Converts detected language codes (e.g., en) to full language names (e.g., English).
Error Handling: Provides an error message if the language cannot be detected (e.g., for very short or ambiguous text).
Requirements
Make sure to install the following Python libraries before running the project:

bash
Copy code
pip install langdetect langcodes
Usage
Clone or download this repository.
Place the language_detection.py script in your working directory.
Running the Script
To detect the language of example sentences, run the script:

bash
Copy code
python language_detection.py
Example Output
plaintext
Copy code
Text: Bonjour tout le monde!
Detected language: French (Code: fr)
----------------------------------------
Text: Hello everyone!
Detected language: English (Code: en)
----------------------------------------
Text: ¡Hola a todos!
Detected language: Spanish (Code: es)
----------------------------------------
Code Explanation
detect_language Function
This function takes a text string as input and returns the detected language.

Parameters: text (str) – The text to analyze.
Returns: A message indicating the detected language name and code.
python
Copy code
def detect_language(text):
    try:
        lang_code = detect(text)
        lang_name = Language.get(lang_code).display_name()
        return f"Detected language: {lang_name} (Code: {lang_code})"
    except LangDetectException:
        return "Could not detect language. Please provide a longer or more distinct text."
Main Script
The main script iterates through a list of sample sentences, calling detect_language on each and printing the results.

python
Copy code
if __name__ == "__main__":
    texts = [
        "Bonjour tout le monde!",
        "Hello everyone!",
        "¡Hola a todos!",
        "Hallo zusammen!",
        "你好，世界！"
    ]
    for text in texts:
        print(f"Text: {text}")
        print(detect_language(text))
        print("-" * 40)
Applications
Content Filtering: Filter text based on language.
Language-Specific Routing: Direct users to language-appropriate content or support.
Pre-Processing for NLP: Pre-process text for multilingual NLP workflows.
Limitations
Text Requirements: Detection accuracy depends on the length and uniqueness of the input text.
Language Coverage: Limited coverage for regional dialects or less common languages.
Future Improvements
Advanced Detection Models: Integrate a transformer-based model for improved accuracy.
Expanded Language Support: Extend support to regional dialects.
License
This project is open-source and available under the MIT License.
