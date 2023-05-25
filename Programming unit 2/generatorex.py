# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 17:18:10 2021

@author: Siria

experimenting with generators
"""
def gt_eval_rand(u) -> bool:
    """Returns True if this node evaluates to a win, otherwise False"""
    if u.leaf:
        return u.win
    else:
        random_children = (gt_eval_rand(child) for child in random_order(u.children))
        if u.op == "OR":
            return any(random_children)
        if u.op == "AND":
            return all(random_children)
