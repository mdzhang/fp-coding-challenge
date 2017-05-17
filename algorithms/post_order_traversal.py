import unittest


def post_order_traversal(tree):
    if not tree:
        return []

    traversal = []

    for child in tree[1:]:
        child_traversal = post_order_traversal(child)
        traversal.extend(child_traversal)

    traversal.append(tree[0])

    return traversal


class TestPostOrderTraversal(unittest.TestCase):
    def test_given(self):
        tree1 = [1, [2, [4], [5], [3]]]
        expected1 = [4, 5, 3, 2, 1]

        self.assertEqual(post_order_traversal(tree1), expected1)

        tree2 = ['f', ['b', ['a'], ['d', ['c'], ['e']]], ['g', ['i', ['h']]]]
        expected2 = ['a', 'c', 'e', 'd', 'b', 'h', 'i', 'g', 'f']

        self.assertEqual(post_order_traversal(tree2), expected2)

        tree3 = [
            're', ['b', ['orn'], ['ate']],
            ['alize', ['s']], ['lief'], ['d', ['der']]
        ]
        expected3 = [
            'orn', 'ate', 'b', 's', 'alize',
            'lief', 'der', 'd', 're'
        ]

        self.assertEqual(post_order_traversal(tree3), expected3)

    def test_empty(self):
        self.assertEqual(post_order_traversal([]), [])

    def test_single(self):
        self.assertEqual(post_order_traversal([1]), [1])


if __name__ == '__main__':
    unittest.main()
