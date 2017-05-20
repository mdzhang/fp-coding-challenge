*NB*: The following solutions assume Python v3.6.1

> Write a function that computes the hamming distance between two iterables. The hamming distance is defined as the number of positions where the symbols are different. <https://en.wikipedia.org/wiki/Hamming_distance>

##### Solution

[See solution](./hamming_distance.py)

> Uniquely Encode a string to as short a length as possible then decode it. Feel free to look up established algorithms to attempt the shortest length possible, but cite the algorithm you have chosen. We will compare your compression against Run Length Encoding, listed next to each example is the length of the compressed string using Run Length Encoding.

##### Solution

*NB*: The following solution is, admittedly, not ideal for compressing short strings due to the overhead of space needed to encode the Huffman tree. But, the cost of storing the encoded tree is amortized as the length of the string grows, as is evident if you use it to encode `fixtures/lorum.txt`.

*NB*: The following solution also assumes a third party lib or tool such as e.g. `gzip` should not have been used.

[See solution](./string_compression.py)

> Given a tree, find the postorder traversal: Leftmost leaf, Leaf to the right of that leaf, root of those, left of the next right branch, etc.
<https://en.wikipedia.org/wiki/Tree_traversal#Post-order>

##### Solution

*NB*: The following solution assumes the first example in the provided problem description had a typo wherein

`[1, [2, [4], [5], [3]]]` really should have been `[1, [2, [4], [5]], [3]]`

[See solution](./post_order_traversal.py)
