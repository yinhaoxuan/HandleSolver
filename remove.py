# check if the word to check is still possible with the information from feedback
def agree(word_to_check, guessed_word, feedback):
    # TODO
    return 1

def remove(l, feedback, word):
    l1 = []
    for w1 in l:
        if agree(w1, word, feedback):
            l1.append(w1)
    return l1