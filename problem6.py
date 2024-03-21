def remove_duplicates_and_sort(words):
    word_list = words.split()

    unique_words = set(word_list)

    sorted_words = sorted(unique_words)
    result = ' '.join(sorted_words)

    return result
input_words = input("Enter a sequence of whitespace separated words: ")
result = remove_duplicates_and_sort(input_words)

print("Output:", result)