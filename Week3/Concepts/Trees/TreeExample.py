import poc_draw_tree
from Tree import Tree


def run_examples():
    """
    Create some trees and apply various methods to these trees
    """
    tree_a = Tree("a", [])
    tree_b = Tree("b", [])
    print "Tree consisting of single leaf node labelled 'a'", tree_a
    print "Tree consisting of single leaf node labelled 'b'", tree_b

    tree_cab = Tree("c", [tree_a, tree_b])
    print "Tree consisting of three node", tree_cab

    tree_dcabe = Tree("d", [tree_cab, Tree("e", [])])
    print "Tree consisting of five nodes", tree_dcabe
    print

    my_tree = Tree("a", [Tree("b", [Tree("c", []), Tree("d", [])]),
                         Tree("e", [Tree("f", [Tree("g", [])]), Tree("h", []),
                                    Tree("i", [])])])
    print "Tree with nine nodes", my_tree

    print "The tree has", my_tree.num_nodes(), "nodes,",
    print my_tree.num_leaves(), "leaves and height",
    print my_tree.height()

    poc_draw_tree.TreeDisplay(my_tree)


run_examples()
