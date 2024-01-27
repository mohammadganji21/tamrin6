def obscure_code():
    user_input = input()
    words_list = user_input.split()
    sorted_words = sort_by_num_suffix(words_list)
    initials = extract_initial_letters(sorted_words)
    print_result(''.join(initials))

def sort_by_num_suffix(words):
    return sorted(words, key=num_suffix)

def num_suffix(word):
    return int(word[1:])

def extract_initial_letters(words):
    return list(map(first_letter, words))

def first_letter(word):
    return word[0]

def print_result(output):
    print(output)

if __name__ == "__main__":
    obscure_code()
