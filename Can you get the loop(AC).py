def loop_size(node):
    p1 = node
    p2 = node.next
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            break
    i = 0
    while True:
        p1 = p1.next
        p2 = p2.next.next
        i += 1
        if p1 == p2:
            return i
            