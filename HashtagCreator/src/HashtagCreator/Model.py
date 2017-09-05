class Model():
    
    def __init__(self, word, count, file, sentence):
        self.word = word
        self.count = count
        self.file = file
        self.sentence = sentence
        
    def combine_models(self, model):
        self.word = self.word
        self.count = self.count + model.count
        self.file = self.file + model.file
        self.sentence = self.sentence + model.sentence
    
    def __repr__(self):
        sentences = [''.join(sentence) for sentence in self.sentence]
        files = [''.join(file) for file in self.file]
        return '\n' + 'Word : ' + self.word + '\n' + 'Occurences : ' + str(self.count) + '\nContained in file(s) : ' + str(files) + '\nIn Sentences : ' + str(sentences) + '\n\n'
    
    def __iter__(self):
        return iter([self.word, self.count, self.file, self.sentence])
    
    def __json__(self):
        return {'word': self.word, 'count': self.count, 'file': self.file, 'sentence': self.sentence}