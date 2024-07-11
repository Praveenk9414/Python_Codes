def print_even_length_words(input_str):
    words = input_str.split()
    even_length_words = [word for word in words if len(word) % 2 == 0]

    print("Even-length words:", " ".join(even_length_words))

# Example: Print even-length words from a string
input_str = "Print only even length words in this example"
print_even_length_words(input_str)