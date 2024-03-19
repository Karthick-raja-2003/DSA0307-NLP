from transformers import MarianMTModel, MarianTokenizer
from transformers import MarianMTModel, MarianTokenizer
5
def translate(text, model_name="Helsinki-NLP/opus-mt-en-fr"):
    # Load the pre-trained model and tokenizer
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    # Perform translation
    translated = model.generate(**inputs)

    # Decode the translated text
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    
    return translated_text

def main():
    # English text to be translated
    english_text = "Hello, how are you?"

    # Translate the English text to French
    french_translation = translate(english_text)

    print("English Text:", english_text)
    print("French Translation:", french_translation)

if __name__ == "__main__":
    main()
