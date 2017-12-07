# -*- coding: utf-8 -*-
import json
import re
from collections import Counter


def open_file():
    data = []
    with open("groups.txt") as f:
        for line in f:
            data.append(json.loads(line))
    return data


def count_words(data):
    words = []
    for i in data:
        words.append(i['names'])

    count = 0
    dict_ = []
    for i in words:
        for a in i:
            count += 1
            dict_.append(a.lower())
    dict_ = str(dict_).replace('[', '').replace('\'', '').replace(']', '').replace(',', '')
    dict_ = dict_.split(' ')
    r = re.compile("[а-я]+")
    e = re.compile("[a-z]+")
    russian = [w for w in filter(r.match, dict_)]
    english = [w for w in filter(e.match, dict_)]

    russian_words = Counter(russian)
    english_words = Counter(english)

    print(russian_words)
    print(english_words)


def main():
    data = open_file()

    count_words(data)

if __name__ == '__main__':
    main()
