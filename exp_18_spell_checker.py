from nltk.corpus import words
from nltk.metrics.distance import edit_distance

# nltk.download('words')

def spell_check(word):
    english_words = set(words.words())
    if word in english_words:
        return word  
    
    best_match = None
    min_distance = float('inf')
    
    for w in english_words:
        distance = edit_distance(word, w) #compares two words and calculate their edit distancer
        if distance < min_distance:
            min_distance = distance
            best_match = w
    
    return best_match

# Example usage
print(spell_check("Longiude"))
