import re

def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002600-\U000026FF"  # miscellaneous symbols
        u"\U0001F900-\U0001F9FF"  # supplemental symbols & pictographs
        u"\U0001FA70-\U0001FAFF"  # symbols & pictographs extended-A
        u"\U0001F004"             # Mahjong tiles
        u"\U0001F0CF"             # playing cards
        u"\U00002700-\U000027BF"  # Dingbats
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# Function to remove Arabic diacritics (Tashkeel) and Tatweel (elongation)
def remove_diacritics(text):
    arabic_diacritics = re.compile(r'[\u0617-\u061A\u064B-\u0652\u0653-\u0655\u0670]')
    text = re.sub(arabic_diacritics, '', text)
    return re.sub(r'ـ', '', text)  # Remove Tatweel (elongation)

# Function to normalize Arabic letters to their standard forms
def normalize_arabic(text):
    text = re.sub(r'[إأآا]', 'ا', text)  # Normalize different forms of Alef to "ا"
    #text = re.sub(r'ة', 'ه', text)       # Convert Ta Marbuta to Ha
    text = re.sub(r'ى', 'ي', text)       # Convert Alef Maqsura to Ya
    #text = re.sub(r'ؤ', 'و', text)       # Convert Hamza above Waw to Waw
    #text = re.sub(r'ئ', 'ي', text)       # Convert Hamza above Ya to Ya
    return text

def remove_special_whitespace(text):
    # This pattern targets various invisible whitespace characters like non-breaking spaces, zero-width spaces, etc.
    whitespace_characters = re.compile(r'[\u200B-\u200D\u2060-\u206F\u00A0\u060C\u061F?!]+')  # Non-breaking spaces, zero-width spaces, etc.
    return whitespace_characters.sub(' ', text)

# Function to ensure proper punctuation spacing
def fix_punctuation_spacing(text):
    # Remove spaces before punctuation
    text = re.sub(r'\s+([?.!,])', r'\1', text)  # Removes spaces before punctuation marks
    return text

# Function to count words in a text
def count_words(text):
    return len(text.split())

# Main function to clean text
def clean_text(text):
    if not isinstance(text, str):
        return text  # Return the original value if it's not a string
    text = text.strip()                                      # Remove leading/trailing whitespace
    text = remove_emojis(text)                               # Remove emojis
    text = remove_diacritics(text)                           # Remove Arabic diacritics and Tatweel
    text = normalize_arabic(text)                            # Normalize Arabic letters
    text = remove_special_whitespace(text)                   # Remove special/invisible Unicode spaces
    text = fix_punctuation_spacing(text)                     # Fix punctuation spacing issues
    text = re.sub(r'\s+', ' ', text).strip()                 # Final pass to remove any remaining multiple spaces
    return text