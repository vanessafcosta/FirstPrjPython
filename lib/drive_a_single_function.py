# ===== Challenge ======
# A function called count_words that takes a string as an argument and returns the number of words in that string.

def count_words(text):
    if text is not None:
        result = text.split()    
        return len(result)
    else:
        raise Exception("Empty String")

