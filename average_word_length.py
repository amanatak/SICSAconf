# Buggy Function: Compute Average Word Length, Ignoring Empty Strings
def average_word_length(words):
    total_length = 0
    count = 0
    for word in words:
        if word != "":
            total_length += len(word)
        count += 1
    if count == 0:
        return 0
    return total_length / count