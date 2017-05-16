def post_order_traversal(tree):
    # TODO
    pass


Tree1 = [1, [2, [4], [5], [3]]]
Tree2 = ['f', ['b', ['a'], ['d', ['c'], ['e']]], ['g', ['i', ['h']]]]
Tree3 = ['re', ['b', ['orn'], ['ate']], ['alize', ['s']], ['lief'], ['d', ['der']]]

assert post_order_traversal(Tree2) == [4,5,2,3,1]
assert post_order_traversal(Tree2) == ['a', 'c', 'e', 'd', 'b', 'h', 'i', 'g', 'f']
assert post_order_traversal(Tree3) == ['orn', 'ate', 'b', 's', 'alize', 'lief', 'der', 'd',
're']
