from collections import Counter
import re

def evaluate_coherence(text):
    # Preprocessing: Remove punctuation and convert text to lowercase
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    
    # Tokenize the text into words
    words = text.split()
    
    # Calculate word frequency
    word_freq = Counter(words)
    
    # Calculate coherence score based on word repetition
    coherence_score = sum(count - 1 for count in word_freq.values()) / len(words)
    
    return coherence_score

def main():
    text = """
    Text coherence refers to how well the ideas in a text are logically connected. 
    A coherent text flows smoothly and is easy to understand. 
    It avoids abrupt shifts in topic or perspective.
    """
    coherence_score = evaluate_coherence(text)
    print("Coherence Score:", coherence_score)

if __name__ == "__main__":
    main()
