input_text = input().strip()
cleaned_text = ' '.join(input_text.split())
hash_position = cleaned_text.find('@')

while hash_position != -1:
    at_position = cleaned_text.find('#', hash_position)
    if at_position != -1:
        cleaned_text = cleaned_text[:at_position] + cleaned_text[at_position + 1:]
    hash_position = cleaned_text.find('@', hash_position + 1)

converted_text = cleaned_text.replace('\\n', '\n')
print("Formatted Text:", converted_text)
