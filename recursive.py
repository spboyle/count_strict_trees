#!/usr/bin/env python

# Count the number of different strict binary trees of
# height K that can be made from N nodes.
# Strict binary tree = every non-leaf node has two children
#
# To count number of trees for 11 nodes:
# Remove one node -- this is the root for our right & left subtrees
#
# With remaining ten nodes, divide them between left and right subtrees
#   * each subtree must get an odd number of nodes
# LHS   RHS
# 1     9
# 3     7
# 5     5
# 7     3
# 9     1
#
# Example: 11
#                x         x         x         x         x
#               / \   +   / \   +   / \   +   / \   +   / \
#              1   9     3   7     5   5     7   3     9   1
#
#              f(11) = f(1)*f(9) + f(3)*f(7) + f(5)*f(5) + f(7)*f(3) + f(9)*f(1)
#
# Example: 9
#                x         x         x         x
#               / \   +   / \   +   / \   +   / \
#              1   7     3   5     5   3     7   1
#
#              f(9) = f(1)*f(7) + f(3)*f(5) + f(5)*f(3) + f(7)*f(1)
#
# For each pair of sizes of LHS and RHS subtrees, there are three cases to consider:
# 1. Only LHS reaches the full height of the tree
# 2. Only RHS reaches the full height of the tree
# 3. Both LHS & RHS reach full height of tree

PRIME_MOD = 9901


def count_strict_trees(n, k):
    if n % 2 == 0:
        return 0
    answer = num_trees_at_height(n, k)
    print(answer)
    return answer % PRIME_MOD


def num_trees_at_height(nodes_left, height):
    if height < 1:
        return 0
    elif height == 1 and nodes_left == 1:
        return 1

    subtree_height = height - 1
    half_of_nodes = (nodes_left - 1) // 2
    num_trees = 0

    # From left subtree having 1 node to half of remaining nodes
    # Calculate how many trees can be generated
    # Note that in this loop, the right tree always has more nodes than left tree
    for left_half in range(1, half_of_nodes, 2):
        right_half = nodes_left - 1 - left_half
        lhs_reaches_height = (
            num_trees_at_height(left_half, subtree_height) *
            num_trees_at_most_height(right_half, subtree_height-1)
        )
        rhs_reaches_height = (
            num_trees_at_most_height(left_half, subtree_height-1) *
            num_trees_at_height(right_half, subtree_height)
        )
        equal_height = (
            num_trees_at_height(left_half, subtree_height) *
            num_trees_at_height(right_half, subtree_height)
        )
        num_trees += lhs_reaches_height + rhs_reaches_height + equal_height

    # Use symmetry between left tree and right tree to count those solutions
    # where the right tree has fewer nodes than the left tree
    num_trees *= 2

    # Add the special case where left and right subtrees have equal number of nodes,
    # because we don't want that amount to be doubled
    if half_of_nodes % 2:
        subtrees_at_height = num_trees_at_height(half_of_nodes, subtree_height)
        subtrees_less_than_height = num_trees_at_most_height(half_of_nodes, subtree_height-1)
        num_trees += subtrees_less_than_height * subtrees_at_height * 2
        num_trees += subtrees_at_height * subtrees_at_height

    return num_trees

def num_trees_at_most_height(nodes_left, height):
    num_trees = 0
    for x in range(1,height+1):
        num_trees += num_trees_at_height(nodes_left, x)

    return num_trees
