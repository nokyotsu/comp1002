#!/usr/bin/env python3

class BinTree:
    data, left, right = None, None, None
    
    def __init__(self, data, left=None, right=None):
        self.data  = data
        self.left  = left
        self.right = right
            
    def __str__(self):
        return '({0} {1} {2})'.format(self.data, self.left, self.right)

def PreOrder(node, visit=[]):
    if node is not None:
        visit.append(node.data)
        PreOrder(node.left, visit)
        PreOrder(node.right, visit)
    return visit

def PostOrder(node, visit=[]):
    if node is not None:
        PostOrder(node.left, visit)
        PostOrder(node.right, visit)
        visit.append(node.data)
    return visit

def InOrder(node, visit=[]):
    if node is not None:
        InOrder(node.left, visit)
        visit.append(node.data)
        InOrder(node.right, visit)
    return visit

a = BinTree('a',
      BinTree('b',
        BinTree('d',
          BinTree('g',
            BinTree('i')
          ),
          BinTree('h')
        )
      ),
      BinTree('c',
        BinTree('e'),
        BinTree('f')
      )
    )

print("Pre-order:  ", ", ".join(PreOrder(a)))
print("Post-order: ", ", ".join(PostOrder(a)))
print("In-order:   ", ", ".join(InOrder(a)))
