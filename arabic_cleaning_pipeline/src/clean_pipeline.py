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

def remove_diacritics(text):
    arabic_diacritics = re.compile(r'[\u0617-\u061A\u064B-\u0652\u0653-\u0655\u0670]')
    text = re.sub(arabic_diacritics, '', text)
    return re.sub(r'ـ', '', text)

def normalize_arabic(text):
    text = re.sub(r'[إأآا]', 'ا', text)
    text = re.sub(r'ى', 'ي', text)
    return text

def remove_special_whitespace(text):
    whitespace_characters = re.compile(r'[\u200B-\u200D\u2060-\u206F\u00A0\u060C\u061F?!]+')
    return whitespace_characters.sub(' ', text)

def fix_punctuation_spacing(text):
    text = re.sub(r'\s+([?.!,])', r'\1', text)
    return text
# Count the words
def count_words(text):
    return len(text.split())

def clean_text(text):
    if not isinstance(text, str):
        return text
    text = text.strip()
    text = remove_emojis(text)
    text = remove_diacritics(text)
    text = normalize_arabic(text)
    text = remove_special_whitespace(text)
    text = fix_punctuation_spacing(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

__all__ = ["clean_text", "count_words"]
