import nltk
from nltk.util import ngrams
from collections import defaultdict

# Download necessary tokenizer data if not already available
#nltk.download('punkt')

def train_ngrams(text, n):
    tokens = nltk.word_tokenize(text.lower())
    n_grams = list(ngrams(tokens, n))
    print(n_grams)
    
    # Initialize a regular defaultdict
    model = defaultdict(dict)
    
    # Count occurrences
    for n_gram in n_grams:
        prefix = tuple(n_gram[:-1])
        suffix = n_gram[-1]
        print(suffix,prefix)
        
        if prefix not in model:
            model[prefix] = {}
        
        if suffix not in model[prefix]:
            model[prefix][suffix] = 0
        
        model[prefix][suffix] += 1
    
    # Convert counts to probabilities
    for prefix in model:
        total_count = float(sum(model[prefix].values()))
        for suffix in model[prefix]:
            model[prefix][suffix] /= total_count  # Normalize to probabilities

    return model

def predict_next(model, text, n):
    tokens = nltk.word_tokenize(text.lower())
    prefix = tuple(tokens[-(n-1):])  # Extract the last (n-1) words as prefix
    
    if prefix in model:
        next_word_probs = model[prefix]
        predicted_word = max(next_word_probs, key=next_word_probs.get)  # Choose word with highest probability
        return predicted_word
    else:
        return None
    
# Example usage
text = 'this is a simple text to demonstrate the n gram model'
trigram_model = train_ngrams(text, 3)
input_sequence = "simple text to"
next_word = predict_next(trigram_model, input_sequence, 3)

if next_word:
    print("Predicted word:", next_word)
else:
    print("Unable to make prediction")
