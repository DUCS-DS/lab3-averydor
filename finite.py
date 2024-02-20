from llist import LList, Node, append


def length(lst):
    """return the length of a finite linked list"""
    counter = 0
    current = lst.head
    while current:
        counter += 1
        current = current.next
    return counter

def llprint(lst):
    """print a finite linked list"""
    current = lst.head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()



if __name__ == "__main__":
    llist = LList()
    append(llist, Node(1))
    append(llist, Node(2))
    append(llist, Node(3))
    append(llist, Node(8))
    append(llist, Node(16))
    append(llist, Node(32))
    append(llist, Node(64))
    append(llist, Node(128))
    append(llist, Node(256))
    append(llist, Node(512))
    print(length(llist))
    llprint(llist)