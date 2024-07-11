import string

def remove_punctuation(s):
    translator = str.maketrans('', '', string.punctuation)
    return s.translate(translator)

input_str = 'This, is best: for ! us /;;'
print(remove_punctuation(input_str))