""" bst.py

Student: Joel Wittrin 
E-mail: joel.wittrin.6917@student.uu.se
Reviewed by: Andreas Michael
Date reviewed: 17-09-26
"""


from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k): # given function
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    # Exc 8
    def contains(self, k):
        return self._contains(self.root, k)

    def _contains(self, r, k):
        if r is None:
            return False
        elif r.key == k:
            return True
        elif r.key > k:
            return self._contains(r.left, k)
        else:
            return self._contains(r.right, k)

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):             # Exc9     
        return self._height(self.root)

    def _height(self, r):

        if r == None:
            return 0
        else:
            left_height = self._height(r.left)
            right_height = self._height(r.right)
            if left_height > right_height:
                return 1 + left_height
            else:
                return 1 + right_height


    def __str__(self):            # Exc10       

        string = ''
        for d in self:
            string += str(d) + ', '

        return '<' + string[:-2] + '>'


    def to_list(self):            # Exc11   
        lst = []
        for d in self:
            lst.append(d)

        return lst
        # Complexity of Theta(n) due to visiting each node once

    def to_LinkedList(self):       # Exercise 12
        result = LinkedList()
        end = None

        for d in self:
            node = LinkedList.Node(d, None)
            if result.first == None:
                result.first = node
            else:
                end.succ = node
            end = node

        return result
        # Complexity of Theta(n) as each node is visited once through the loop

    def remove(self, key):
        self.root = self._remove(self.root, key)

    # Exercise 13
    def _min_key(self, r):
        while r.left:
            r = r.left
        return r.key

    def _remove(self, r, k):      
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
            # r.left = left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right, k)
            # r.right =  right subtree with k removed
        else:  
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  
                smallest_key = self._min_key(r.right)
                r.key = smallest_key
                r.right = self._remove(r.right, smallest_key)
        return r  # Remember this! It applies to some of the cases above


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")

    # Testing the functions:
    print(t.contains(3))
    print(t.height())
    print(t.__str__())
    print(t.to_list())
    print(t.to_LinkedList())

    t.remove(4)
    print(t)


if __name__ == "__main__":
    main()


"""
Exc14: In a binary search tree with n nodes and height h, what is the complexity in the
following scenarios:
==============================

1. Worst case of successful search: Theta(h), since we traverse down the entire tree to the final node.
2. Worst case of unsuccessful search: Theta(h) due to the same reason

If we have a tree with two successors each time, we get 2, 4, 8 ... 2^h +1 nodes (+1 due to root). We then get n ≈ 2^h, i.e. h = logn.
It's still the same principle, that the complexity is Theta(h), but h can be both logn and n

"""
