Using Min Heap


We use a hashmap<key, value> to store the frequencies of all unique words in the list, where the key is the word and value is the frequency of that word in the list. While iterating over each word, we will increment the frequency corresponding to that word in the hashmap by 1.

 

Now, we need to find the K largest frequencies among them. For this, we will first initialize a min-heap of size K that will keep the least frequency word as the top(root) element. When two words have the same frequencies we will keep the lexicographically larger word at the top of other words in the min-heap(as the lexicographically larger word will have the least priority from all top most K words). 

 

Now, iterating through the Hashmap, we will add first K words into the min-heap. For the next words, we will compare the frequency of the current word with the minimum frequency from the heap(top element of min heap). If the current frequency is larger than the minimum frequency from the heap. We will pop the top element from the min-heap and insert our current word into the list. Otherwise, if the current frequency is equal to the minimum frequency then we will compare both the words and only keep the lexicographically smaller word from them.

 

Now, our min heap will be storing the top K most frequent words. We will pop all words in a list. This list will now contain the least frequent word out of these K words at the 0th position and the most frequent word at the (K - 1)th position. This means we need to return the reverse of this list as our answer.

Space Complexity: O(n)Explanation:
O(N), where N is the total number of words.
 

In the worst case, we will be storing all the N words in a map that requires O(N) space. Also, O(K) space will be required to maintain a heap of size K.

Time Complexity: OtherExplanation:
O(N * log(K)), where N is the total number of words, and K is the number of words to return.
 

In the worst case, we will be iterating on all N words in the list and adding it to the min-heap of size K that requires O(logK) time, and when the min-heap is full of its capacity removing one word will also take O(logK) time.