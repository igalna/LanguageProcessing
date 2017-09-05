import string
from nltk import word_tokenize, sent_tokenize

def split_with_contractions(token):
    exclude = set(string.punctuation)
    return [''.join(ch for ch in word if ch not in exclude) for word in filter(lambda word: word not in ',.\'', token.split(" "))]
    #translator = str.maketrans('', '', string.punctuation)
    #return [word.translate(translator) for word in filter(lambda word: word not in ',-', token.split(" "))]

def split_without_contractions(token):
    return [word for word in filter(lambda word: word not in ',-', word_tokenize(token))]

def get_sentence_tokens_from_string(data):
    return sent_tokenize(data)