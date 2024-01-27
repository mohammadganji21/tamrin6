import re
def remove_punctuation(text):
    # Define a regular expression pattern for removing punctuation
    punctuation_pattern = re.compile(r'[،:؛.؟!٬٫]+')
    
    # Replace punctuation with an empty string
    cleaned_text = punctuation_pattern.sub('', text)
    
    return cleaned_text

def calculate_hamming_distance(word1, word2):
    # Pad the shorter word with "_" to make lengths equal
    len1, len2 = len(word1), len(word2)
    if len1 < len2:
        word1 += '_' * (len2 - len1)
    elif len1 > len2:
        word2 += '_' * (len1 - len2)

    # Calculate the Hamming distance
    distance = sum(c1 != c2 for c1, c2 in zip(word1, word2))

    return distance

def find_similar_words(n, sentence, target_word):
    # Remove punctuation from the sentence
    cleaned_sentence = remove_punctuation(sentence)
    
    # Split the cleaned sentence into words
    words = cleaned_sentence.split(" ")
    
    result = []

    for word in words:
        distance = calculate_hamming_distance(word, target_word)
        if distance <= n:
            result.append(word)

    return result

# Example usage
n = int(input())
sentence = input()
target_word = input()

result = find_similar_words(n, sentence, target_word)
for word in result:
    print(word)