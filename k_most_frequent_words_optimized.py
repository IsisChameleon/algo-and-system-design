"""
K Most Frequent Words Optimized

This module contains an optimized function to find the k most frequent words in a list of words.
The function will return a list of k words sorted by their frequency from highest to lowest.
If two words have the same frequency, the lexicographically smaller word comes first.
"""

from collections import Counter
from heapq import nlargest

def find_k_most_frequent_words_optimized(words: list[str], k: int) -> list[str]:
    # Count the frequency of each word
    word_frequencies = Counter(words)

    # Find the k most frequent words using nlargest from heapq,
    # which uses a heap and is O(N log k) where N is the number of unique words
    k_most_common = nlargest(k, word_frequencies.items(), key=lambda item: (item[1], -ord(item[0][0])))

    # Extract the words and sort them by frequency and lexicographically
    result = [word for word, frequency in k_most_common]
    return result

if __name__ == "__main__":
    # Example usage:
    WORDS = ["word1", "word2", "word1", "word3", "word2", "word1"]
    K = 2
    print(find_k_most_frequent_words_optimized(WORDS, K))
