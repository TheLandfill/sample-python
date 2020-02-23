#!/usr/bin/env python3

def count_words(filename):
    word_counts = {}
    with open(filename, "r") as reader:
        for line in reader:
            words = line.split()
            for word in words:
                pass
    return word_counts
