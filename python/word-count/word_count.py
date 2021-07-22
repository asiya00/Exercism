import re

def count_words(sentence):
    sentence = sentence.lower()
    for i in "\n\t,_!@#$%^&*:;/{}()<>.":
        sentence = sentence.replace(i," ")
    words = sentence.split()
    word_count = {}
    for word in words:
        pattern = re.search(r"[a-z0-9]+\'?[a-z0-9]+|[a-z0-9]", word)
        if pattern:
            actual_word = pattern.group()
            if actual_word in word_count:
                word_count[actual_word] += 1
            else:
                word_count[actual_word] = 1

    return word_count
