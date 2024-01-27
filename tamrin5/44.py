import re

def remove_punctuation(text):
    punctuation_pattern = re.compile(r'[،:؛.؟!٬٫]+')
    cleaned_text = punctuation_pattern.sub('', text)
    return cleaned_text

def calculate_hamming_distance(word1, word2):
    len1, len2 = len(word1), len(word2)
    max_len = max(len1, len2)

    # Calculate the Hamming distance
    distance = sum(c1 != c2 for c1, c2 in zip(word1.ljust(max_len, '_'), word2.ljust(max_len, '_')))

    return distance

def find_similar_words(n, sentence, target_word):
    cleaned_sentence = remove_punctuation(sentence)
    words = cleaned_sentence.split(" ")

    result = [word for word in words if calculate_hamming_distance(word, target_word) <= n]

    return result

# Example usage
n = int(input())
sentence = input()
target_word = input()

result = find_similar_words(n, sentence, target_word)
for word in result:
    print(word)
