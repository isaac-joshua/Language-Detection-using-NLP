from langdetect import detect, DetectorFactory
from langcodes import Language
from langdetect import LangDetectException

# Setting seed for consistent detection results 
DetectorFactory.seed = 0

def detect_language(text):
    """
    Detect the language of a given text.

    Parameters:
        text (str): The text to analyze.

    Returns:
        str: The name of the detected language or an error message.
    """
    try:
        # Detect the language code
        lang_code = detect(text)
        
        # Convert language code to full language name (e.g., 'en' -> 'English')
        lang_name = Language.get(lang_code).display_name()
        
        return f"Detected language: {lang_name} (Code: {lang_code})"
    except Exception as e:
        return f"Could not detect language. Error: {str(e)}"

if __name__ == "__main__":
    # Example texts for testing
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
