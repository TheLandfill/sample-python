#!/usr/bin/env python3

def count_words(filename):
    word_counts = {}
    with open(filename, "r") as reader:
        for line in reader:
            words = line.split()
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    return word_counts

def main():
    word_counts = count_words("sample-text.txt")
    sorted_word_counts = sorted(word_counts.items(), key = lambda x: -x[1])
