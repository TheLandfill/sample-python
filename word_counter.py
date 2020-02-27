#!/usr/bin/env python3
import re
from scipy.optimize import curve_fit as fit
import matplotlib.pyplot as plt

def save_word_counts_to_file(word_counts, word_count_file):
    with open(word_count_file, "w") as writer:
        for word in word_counts:
            writer.write(word[0] + " " + str(word[1]) + "\n")

def pareto(x, x_m, alpha):
    return (x_m / x) ** alpha

def pareto_fit(counts):
    word_ranks = list(range(1, len(counts) + 1))
    popt, pcov = fit(pareto, word_ranks, counts, p0=[counts[0], 1])
    perc_std_dev = lambda var, val: str(100 * var ** 0.5 / val) + "%"
    print("x_m:\t" + str(popt[0]) + u" \u00B1 " + perc_std_dev(pcov[0][0], popt[0]))
    print("alpha:\t" + str(popt[1]) + u" \u00B1 " + perc_std_dev(pcov[1][1], popt[1]))
    return popt

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

def gen_plot(popt, counts):
    word_ranks = list(range(1, len(counts) + 1))
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(word_ranks, [pareto(k, popt[0], popt[1]) for k in word_ranks], label="Predicted")
    plt.plot(word_ranks, counts, label="Actual")
    plt.legend()
    plt.savefig("word-counts.png")

def main():
    word_counts = count_words("sample-text.txt")
    sorted_word_counts = sorted(word_counts.items(), key = lambda x: -x[1])
    save_word_counts_to_file(sorted_word_counts, "word-counts.txt")
    counts = [k[1] for k in sorted_word_counts]
    popt = pareto_fit(counts)
    gen_plot(popt, counts)

if __name__ == "__main__":
    main()
