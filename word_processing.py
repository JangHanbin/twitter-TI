from nltk import word_tokenize, pos_tag, ne_chunk



class Preprocessing():
    def __init__(self):
        pass

    def tokenize(self, text):
        return ne_chunk(pos_tag(word_tokenize(text)))