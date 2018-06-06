# -*- coding: utf-8 -*-
import operator
from collections import Counter
from functools import reduce


# multiply all elements in a list
def product(iterable):
    return reduce(operator.mul, iterable, 1)


class LanguageModel():
    def __init__(self, filename='big.segmented.txt'):
        with open(filename, encoding='UTF-8') as f:
            word_count = Counter(word for line in f for word in line.split())
        self.total = sum(word_count.values())

        # compute probability of each word: count/total (as dict)
        self.word_prob = {word: count/self.total
                          for word, count in word_count.items()}

    def __getitem__(self, word):
        return self.get_word_prob(word)

    def get(self, word):
        return self[word]

    def get_word_prob(self, word):
        # return the probability of a word
        # if the word is not in the `self.word_prob` dictionary
        # return 10/10**len(word)/total as the default probability
        return self.word_prob.get(word, 10/10**len(word)/self.total)

    def get_words_prob(self, tokens):
        return product(map(self.get, tokens))


if __name__ == '__main__':
    lm = LanguageModel()

    # easy 9.074170876720021e-05
    print('easy', lm['easy'])
    # apple 7.755701604034206e-06
    print('apple', lm.get('apple'))
    # juice 3.877850802017103e-06
    print('juice', lm.get_word_prob('juice'))

    # apple juice is good 9.885965853143219e-17
    print('apple juice is good', lm.get_words_prob('apple juice is good'.split()))
