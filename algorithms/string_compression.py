from collections import Counter
from functools import total_ordering
import heapq
import unittest


@total_ordering
class HuffmanTree(object):
    """Huffman Code implementation
    
    See See https://en.wikipedia.org/wiki/Huffman_coding.
    """
    def __init__(self, weight, data, left=None, right=None):
        self.weight = weight
        self.data = data
        self.left = left
        self.right = right
        self.codebook = {}
        self.build_codebook()

    def __eq__(self, other):
        return (self.data, self.weight) == (other.data, other.weight)

    def __lt__(self, other):
        if self.weight == other.weight:
            return self.data < other.data
        else:
            return self.weight < other.weight

    def __repr__(self):
        ldata = self.left and self.left.data
        rdata = self.right and self.right.data
        return f'<HuffmanTree (data: {self.data}, left: {ldata}, right: {rdata})>'

    def is_leaf(self):
        return not self.right and not self.left

    def build_codebook(self):
        """Build the 'codebook', a dict mapping a char to sequences of 0s and 1s"""
        self.codebook = {}

        nodes = {
            '0': self.left,
            '1': self.right,
        }

        for prefix, node in nodes.items():
            if not node:
                continue

            if node.is_leaf():
                self.codebook[node.data] = prefix

            for data, code in node.codebook.items():
                self.codebook[data] = prefix + code

        return self.codebook

    @classmethod
    def from_string(cls, string):
        # count frequencies of characters in string
        frequency = Counter(string)

        # build priority queue from frequency counter -
        # higher frequency characters have lower priority
        heap = [HuffmanTree(weight, data) for data, weight in frequency.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            weight = left.weight + right.weight
            data = left.data + right.data

            parent = HuffmanTree(weight, data, left, right)
            heapq.heappush(heap, parent)

        return heapq.heappop(heap)

    def __to_header(self, leaves):
        """Encode tree structure as string
        
        Resulting string has 0s to indicate left nodes, 1s to indicate right 0s,
        and Ls to indicate leaves.
        """
        if self.is_leaf():
            leaves.append(self.data)
            return 'L'

        header = ''

        nodes = {
            '0': self.left,
            '1': self.right,
        }

        for prefix, node in nodes.items():
            if not node:
                continue

            header += prefix + node.__to_header(leaves)

        return header

    def to_header(self):
        """Encode tree as string
        
        First part is structure as built in __to_header. Then a delimiter, and
        then a string where each char left to right indicates the value of a 
        leaf in the tree traversed in preorder
        """
        leaves = []

        return self.__to_header(leaves) + '-' + ''.join(leaves)

    @classmethod
    def from_header(cls, full_header, idx=0):
        """Build weightless HuffmanTree from a header"""
        header_parts = full_header.split('-')
        if len(header_parts) != 2:
            raise ValueError('Improperly encoded string')

        header, leaves = header_parts
        leaves = list(leaves)

        def from_header_helper():
            nonlocal idx
            nonlocal leaves
            nonlocal header

            if idx >= len(header):
                return None

            char = header[idx]

            # leaf
            if char == 'L':
                idx += 1
                data = leaves.pop(0)
                return HuffmanTree(0, data)

            idx += 1
            left = from_header_helper()

            idx += 1
            right = from_header_helper()

            data = ''

            if left:
                data += left.data
            if right:
                data += right.data

            return HuffmanTree(0, data, left, right)

        return from_header_helper()

    @classmethod
    def encode(cls, string):
        """Encode the string and it's Huffman Tree"""
        huff_tree = HuffmanTree.from_string(string)

        data = huff_tree.base_encode(string)

        # string composed of bytes, each 8 bits
        # so must make sure string of 0s and 1s
        # has length which is a multiplier of 8
        pad = (8 - len(data)) % 8
        padded_data = '0' * pad + data

        data_chars = list(map(
            # convert string to binary and reinterpret as ascii char
            lambda eight: chr(int(eight, 2)),
            # split padded_data in segments of length 8
            [padded_data[i:i+8] for i in range(0, len(padded_data), 8)]
        ))

        segments = [huff_tree.to_header(), str(pad), ''.join(data_chars)]
        return '|'.join(segments)

    @classmethod
    def decode(cls, string):
        """Decode the string and it's Huffman Tree"""
        header, pad, data_chars = string.split('|', 2)
        huff_tree = HuffmanTree.from_header(header)
        pad = int(pad)

        padded_data = ''.join(list(map(
            # interpret ascii char as base 2 int, convert to binary string,
            # remove 0b cruft, and ensure has length 8
            lambda char: bin(ord(char))[2:].zfill(8),
            list(data_chars)
        )))

        data = padded_data[pad:]

        return huff_tree.base_decode(data)

    def base_encode(self, string):
        """Encode a string to another string using only 0s and 1s"""
        return ''.join(map(
            lambda char: self.codebook[char],
            string
        ))

    def base_decode(self, string):
        """Decode a string of 0s and 1s to the string before base encoding"""
        decoded_string = ''
        node = self

        for char in string:
            if char == '0':
                node = node.left
            elif char == '1':
                node = node.right
            else:
                raise ValueError('Improperly encoded string')

            if node.is_leaf():
                decoded_string += node.data
                node = self

        return decoded_string


class TestHuffmanTree(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(HuffmanTree(5, 'a') == HuffmanTree(5, 'a'), True)
        self.assertEqual(HuffmanTree(5, 'a') == HuffmanTree(5, 'b'), False)
        self.assertEqual(HuffmanTree(5, 'a') == HuffmanTree(6, 'a'), False)

    def test_lt(self):
        self.assertEqual(HuffmanTree(5, 'a') < HuffmanTree(5, 'b'), True)
        self.assertEqual(HuffmanTree(5, 'b') == HuffmanTree(5, 'a'), False)
        self.assertEqual(HuffmanTree(5, 'b') == HuffmanTree(6, 'a'), False)

    def test_from_string(self):
        string = 'abb'
        tree = HuffmanTree.from_string(string)
        self.assertEqual(tree.data, 'ab')
        self.assertEqual(tree.weight, 3)
        self.assertEqual(tree.codebook, {'a': '0', 'b': '1'})

        self.assertEqual(tree.left.data, 'a')
        self.assertEqual(tree.left.weight, 1)
        self.assertEqual(tree.left.codebook, {})

        self.assertEqual(tree.right.data, 'b')
        self.assertEqual(tree.right.weight, 2)
        self.assertEqual(tree.right.codebook, {})

    def test_base_encode(self):
        string = 'abb'
        tree = HuffmanTree.from_string(string)
        self.assertEqual(tree.base_encode(string), '011')

        string = 'hello world!'
        tree = HuffmanTree.from_string(string)
        self.assertEqual(tree.base_encode(string), '1110110101010010101000011110111001011')

    def test_base_decode(self):
        string = 'abb'
        tree = HuffmanTree.from_string(string)
        self.assertEqual(tree.base_decode('011'), string)

        string = 'hello world!'
        tree = HuffmanTree.from_string(string)
        self.assertEqual(tree.base_decode('1110110101010010101000011110111001011'), string)

    def test_to_header(self):
        string = 'abb'
        tree = HuffmanTree.from_string(string)

        self.assertEqual(tree.to_header(), '0L1L-ab')

        string = 'abbc'
        tree = HuffmanTree.from_string(string)

        self.assertEqual(tree.to_header(), '00L1L1L-acb')

    def test_from_header(self):
        header = '0L1L-ab'
        tree = HuffmanTree.from_header(header)

        self.assertEqual(tree.data, 'ab')
        self.assertEqual(tree.weight, 0)
        self.assertEqual(tree.codebook, {'a': '0', 'b': '1'})

        self.assertEqual(tree.left.data, 'a')
        self.assertEqual(tree.left.weight, 0)
        self.assertEqual(tree.left.codebook, {})

        self.assertEqual(tree.right.data, 'b')
        self.assertEqual(tree.right.weight, 0)
        self.assertEqual(tree.right.codebook, {})

        self.assertEqual(tree.to_header(), header)

    def test_encode(self):
        pass


def encode(string: str) -> str:
    return HuffmanTree.encode(string)


def decode(string: str) -> str:
    return HuffmanTree.decode(string)


class TestEncoding(unittest.TestCase):
    def test_given(self):
        strings = {
            '0DE9MDK9J8I1BMUQ18HARUPOKXFE4HLADWV12OYYTUFI59Y1', # 47 / 143
            '6QXXCOLMUNBLYY0WOB5BR2HIR5L5XG02TGRAGV', # 36 / 111
            '5PNL', # 4 / 19
            'GKF8ANZ2DH6P3B5WWFMELX8XEMRSJGKHMDN932EZTM2O', # 43 / 132
            '4ZILNB9DW3Y65GIG4Z5WWICIJN6H7HTU88', # 32 / 105
            'Aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa', # 12 / 36
            'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW', # 14 / 19
            (
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' 
                'Duis felis tellus, pharetra sit amet arcu vel, molestie luctus arcu.' 
                'Pellentesque mi nisi, viverra a nulla et, laoreet congue justo.' 
                'Praesent consectetur faucibus risus. Morbi semper velit et tortor hendrerit placerat.'
                'Vestibulum eu erat non justo fringilla molestie. Aliquam erat volutpat.'
                'Mauris sagittis, velit a bibendum convallis, est nunc pretium lacus, at aliquet mi ligula at ligula.'
                'Donec lobortis, tortor vitae ultricies dapibus, neque enim viverra urna, sed blandit quam magna eu nisl.'
                'Nulla volutpat suscipit aliquet. Pellentesque in odio tortor.'
                'Vivamus sagittis aliquet varius. Ut finibus purus dui, non molestie ex varius eu. Sed in varius quam.'
            ) # / 516
        }

        for string in strings:
            encoded = encode(string)
            decoded = decode(encoded)
            print(f'encoded string {string:.5} has encoding len {len(encoded)} (orig: {len(string)})')
            print(f'\tencoded: {encoded}')
            self.assertEqual(string, decoded)


if __name__ == '__main__':
    unittest.main()
