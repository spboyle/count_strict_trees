#!/usr/bin/env python

PRIME_MOD = 9901


def count_strict_trees(n, k):
    trees_per = [[0]*(k+1) for i in range(n+1)]
    trees_per[1][1] = 1
    for nodes in range(1, n+1, 2):
        for h in range(1, k+1):
            sum_up_trees(trees_per, nodes, h)

    print('Real answer: {}'.format(trees_per[n][k]))
    return trees_per[n][k] % PRIME_MOD


def sum_up_trees(a, n, depth):
    for left_half in range(1, (n+1) // 2, 2):
        right_half = n - left_half - 1
        mult = 1 if right_half == left_half else 2

        rhs_less_than_depth = 0
        lhs_less_than_depth = 0
        # Calculate the number of tree structures shorter than depth
        for h in range(1, depth-1):
            rhs_less_than_depth += a[right_half][h]
            lhs_less_than_depth += a[left_half][h]

        # Add together the three scenarios,
        # 1. lhs reaches depth
        # 2. rhs reaches depth
        # 3. both sides reach depth
        a[n][depth] += mult * (
            a[left_half][depth-1] * rhs_less_than_depth +
            a[right_half][depth-1] * lhs_less_than_depth +
            a[left_half][depth-1] * a[right_half][depth-1]
        )
