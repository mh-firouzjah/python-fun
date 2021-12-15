def loop_size(node):
    l = [node.next]
    i = 1
    while True:
        node = l[-1]
        if node.next not in l:
            l.append(node.next)
            i += 1
        else:
            return i - l.index(node.next)


'''
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
test.assert_equals(loop_size(node1), 3, 'Loop size of 3 expected')

# Make a longer chain with a loop of 29
nodes = [Node() for _ in xrange(50)]
for node, next_node in zip(nodes, nodes[1:]):
    node.next = next_node
nodes[49].next = nodes[21]
test.assert_equals(loop_size(nodes[0]), 29, 'Loop size of 29 expected')

# Make a very long chain with a loop of 1087
chain = create_chain(3904, 1087)
test.assert_equals(loop_size(chain), 1087, 'Loop size of 1087 expected')
'''
