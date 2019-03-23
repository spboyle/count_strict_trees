#!/usr/bin/env python


PRIME_MOD = 9901


memoized_trees_at_nodes_and_height = [[-1] * 100 for y in range(200)]
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
    elif memoized_trees_at_nodes_and_height[nodes_left][height] != -1:
        return memoized_trees_at_nodes_and_height[nodes_left][height]

    subtree_height = height - 1
    half_of_nodes = (nodes_left - 1) // 2
    num_trees = 0

    # From left subtree having 1 node to half of remaining nodes
    # Calculate how many trees can be generated
    # Note that in this loop, the right tree always has more nodes than left tree
    for left_half in range(1, half_of_nodes, 2):
        right_half = nodes_left - 1 - left_half
        lhs_bigger = (
            num_trees_at_height(left_half, subtree_height) *
            num_trees_at_most_height(right_half, subtree_height-1)
        )
        rhs_bigger = (
            num_trees_at_most_height(left_half, subtree_height-1) *
            num_trees_at_height(right_half, subtree_height)
        )
        equal_height = (
            num_trees_at_height(left_half, subtree_height) *
            num_trees_at_height(right_half, subtree_height)
        )
        num_trees += lhs_bigger + rhs_bigger + equal_height

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

    memoized_trees_at_nodes_and_height[nodes_left][height] = num_trees
    return num_trees

def num_trees_at_most_height(nodes_left, height):
    num_trees = 0
    for x in range(1,height+1):
        num_trees += num_trees_at_height(nodes_left, x)

    return num_trees
