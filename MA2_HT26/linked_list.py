""" linked_list.py

Student: Joel Wittrin
Mail: joel.wittrin.6917@student.uu.se
Reviewed by: Andreas Michael
Review date: 17-09-26
"""
class Person: #for Ex7
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __lt__(self, other_person):
            return self.pnr < other_person.pnr

    def __le__(self, other_person):
        return self.pnr <= other_person.pnr

    def __eq__(self, other_person):
                return self.pnr == other_person.pnr

    def __gt__(self, other_person):
                    return self.pnr > other_person.pnr

    def __str__(self):
        return f'{self.name}:{self.pnr}'

class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __contains__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented


    def length(self):             # Exc1
        nodes = 0
        f = self.first
        while f:
            nodes += 1
            f = f.succ
            if f == None:
                break
        return nodes


    def remove_last(self):        # Exc2
        f = self.first
        if f == None:
            raise ValueError ('List is empty')

        if f.succ == None:
            value = f.data
            self.first = None
            return value

        # we check if the next node exists since we want to edit the current one.
        while f.succ.succ:
            f = f.succ
        value = f.succ.data
        f.succ = None

        return value


    def remove(self, x):          # Exc3

        f = self.first

        if self.first == None:
            return False

        if f.data == x:
            self.first = f.succ
            return True

        while f.succ:
            if f.succ.data == x:
                f.succ = f.succ.succ
                return True
            else:
                f = f.succ

        return False


    #Exc4 below
    def to_list(self):
        return self._to_list(self.first)

    def _to_list(self, f):
        if f == None:
            return []
        else:
            return [f.data] + self._to_list(f.succ)
    

    def __str__(self):            # Exc5
        string = ''
        for d in self:
            string += str(d) + ', '

        # simply remove the last ', ' as this works for all types
        return '(' + string[:-2] + ')'


    def copy(self):
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
        # Complexity for this implementation:
        # Theta(n^2) since we get n*(n-1)/2

    def new_copy(self):               # Exc6, should be more efficient
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
            
        # New method has complexity of Theta(n) since the only loop is 'for d in self' and we insert from back

def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()

    # Test code:

    print(lst.length())
    print(lst.remove_last())
    print(lst.remove(7))
    print(lst.to_list())
    print(lst.__str__())

    # Exc 7
    plist = LinkedList()
    p = Person('Joel', 20030927)
    q = Person('Frisco', 20230311)
    plist.insert(p)
    plist.insert(q)
    print(plist)


if __name__ == '__main__':
    main()

