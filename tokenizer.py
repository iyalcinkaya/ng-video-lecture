import spacy

# Load the Turkish language model
nlp = spacy.load("tr_core_news_trf")

# Input text to be tokenized
input_text = "Merhaba dünya! Nasılsınız?"

# Process the input text with spaCy
doc = nlp(input_text)

# Print the tokens
for token in doc:
    print(token.text)