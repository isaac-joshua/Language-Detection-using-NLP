# Importing TextBlob for text processing
from textblob import TextBlob

# Step 1: Input text with spelling errors
text = "I havv a speling errror in this sentnce."

# Step 2: Create a TextBlob object
blob = TextBlob(text)

# Step 3: Use the 'correct' method to fix the spelling errors
corrected_text = blob.correct()

# Step 4: Compare and print the original and corrected text
print("Original Text:", text)
print("Corrected Text:", corrected_text)

# Step 5: Word-wise correction analysis
print("\nWord-wise Correction Analysis:")
original_words = text.split()
corrected_words = str(corrected_text).split()

# Analyze each word to see if it was corrected
for original, corrected in zip(original_words, corrected_words):
    if original != corrected:
        print(f"Original: '{original}' -> Corrected: '{corrected}'")