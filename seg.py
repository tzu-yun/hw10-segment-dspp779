# -*- coding: utf-8 -*-
from lm import LanguageModel
from memoize import Memoize


lm = LanguageModel()


def splits(text, max_len=10):
    return [(text[:i+1], text[i+1:]) for i in range(min(len(text), max_len))]


@Memoize
def segment(text):
    text = text.strip()
    if not text:
        return []

    candidates = [[left] + segment(right) for left, right in splits(text)]
    return max(candidates, key=lm.get_words_prob)


if __name__ == '__main__':
    test = [
        'colorlessgreenideassleepfuriously.',
        'ihaveadream.',
        'howtotrainadragon.',
        'canwetakeaphotoofyou?'
    ]

    for text in test:
        words = segment(text)
        print(text)
        print(' '.join(words))
        print()
