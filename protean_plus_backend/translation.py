from transformers import MarianMTModel, MarianTokenizer
from langdetect import detect

# Load models only once
hi_tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-hi-en")
hi_model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-hi-en")

def detect_language(text):
    return detect(text)

def translate_hi_to_en(text):
    batch = hi_tokenizer([text], return_tensors="pt", padding=True)
    gen = hi_model.generate(**batch)
    return hi_tokenizer.decode(gen[0], skip_special_tokens=True)
