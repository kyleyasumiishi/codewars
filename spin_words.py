
# Takes a string of one or more words, and returns the same string, but with all words n letters or more reversed 

def spin_words(sentence, n):
    updated_words_list = []
    for word in sentence.split(" "):
        updated_words_list.append(word[::-1]) if len(word) >= n else updated_words_list.append(word)         
    return " ".join(updated_words_list)

print(spin_words("Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed", 5))