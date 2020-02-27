#!/usr/bin/env python3
import re

def save_word_counts_to_file(word_counts, word_count_file):
    with open(word_count_file, "w") as writer:
        for word in word_counts:
            writer.write(word[0] + " " + str(word[1]) + "\n")

def count_words(filename):
    word_counts = {}
    with open(filename, "r") as reader:
        for line in reader:
            clean_line = re.sub(r"[^a-zA-Z0-9\s]", "", line).lower()
            words = clean_line.split()
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    return word_counts

def main():
    word_counts = count_words("sample-text.txt")
    sorted_word_counts = sorted(word_counts.items(), key = lambda x: -x[1])
    save_word_counts_to_file(sorted_word_counts, "word-counts.txt")

if __name__ == "__main__":
    main()
