"""
K Most Frequent Words

You have been given an array/list 'WORDS' of 'N' non-empty words, and an integer 'K'. Your task is to return the 'K' most frequent words sorted by their frequency from highest to lowest.
Note:
If two words have the same frequency then the lexicographically smallest word should come first in your answer.

Follow up:
Can you solve it in O(N * logK) time and O(N) extra space?
"""

from heapq import heappush, heappop

def find_k_most_frequent_words(words: list[str], k: int)-> list[str]:

    k_most_frequent_words = []
    word_frequencies = dict()
    distinct_words=0

    for word in words: #--> looping though all words O(N) time

        print(f'Processing word {word}...')
        # add word to frequencies dictionary / hashmap --> O(N) extra soace
        if word in word_frequencies:
            word_frequencies[word]+=1
            print(f'.. existing word with new frequency {word_frequencies[word]}...')
        else:
            word_frequencies[word]=1
            distinct_words+=1
            print(f'.. distinct word with freq 1, distinct words count {distinct_words}...')

            # add k first distinct words to the heap

            if distinct_words <= k:
                print(f'Adding word to heap {word}...')
                heappush(k_most_frequent_words, (word_frequencies[word], word))
                continue

        # if we have already k items in the heap, compare current item with minimum
        # if current item is bigger it needs to be inserted into the heap and the lower frequency removed

        print(f'current heap : {k_most_frequent_words}')
        current_lower_frequency_word = k_most_frequent_words[0][1] # take second element of tuple = word (first being frequency)
        current_lower_frequency = word_frequencies[current_lower_frequency_word]
        print(f'Word {current_lower_frequency_word} has the minimum frequency: {current_lower_frequency} of the top K')

        print(f'Current word {word} has frequency: {word_frequencies[word]}')
        if word_frequencies[word] >= current_lower_frequency:

            if word_frequencies[word] == current_lower_frequency:
                if word <= current_lower_frequency_word:
                    # if both words have the same frequencies and the new word is lexicographically smaller, let's no insert in heap
                    continue
            # remove current minimum from the heap
            heappop(k_most_frequent_words)
            # add new more frequent word
            heappush(k_most_frequent_words, (word_frequencies[word], word))
            print(f'Current word {word} added to heap: {k_most_frequent_words}')

    # now we have our k most frequent words in the min heap
    k_most_frequent = [item[1] for item in k_most_frequent_words]
    print(f'Final word {k_most_frequent}')

    return k_most_frequent


    





