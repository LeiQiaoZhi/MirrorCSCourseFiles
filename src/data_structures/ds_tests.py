from asyncio.log import logger
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

try:
    from utils.logger import Logger
    import matplotlib.pyplot as plt
    import os
    from binary_search_tree import BinarySearchTree
    from heap import BinaryHeap
    import graphviz
except:
    print('Import Failed')
    quit()


def draw_binary_tree(tree: BinarySearchTree, name='default_tree'):
    Logger.important("Drawing Binary Tree")
    G = graphviz.Graph('Binary Tree', node_attr={'shape': 'record'})
    G.node(str(tree.key),
           f"<f0> k:{tree.key} | <f1> v:{tree.value}")
    to_explore = [tree]
    while len(to_explore) > 0:
        current_node = to_explore.pop()
        if current_node.left != None:
            G.node(str(current_node.left.key),
                   f"<f0> k:{current_node.left.key} | <f1> v:{current_node.left.value}")
            G.edge(str(current_node.key), str(current_node.left.key))
            to_explore.append(current_node.left)
        if current_node.right != None:
            G.node(str(current_node.right.key),
                   f"<f0> k:{current_node.right.key} | <f1> v:{current_node.right.value}")
            G.edge(str(current_node.key), str(current_node.right.key))
            to_explore.append(current_node.right)

    file_name = os.path.join(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.realpath(__file__)))), "plots", "bsts", name)
    G.render(file_name, format='png')
    Logger.important(f"Binary tree graph saved as {file_name}")


def draw_heap(heap: BinaryHeap, name='default_heap'):
    Logger.important("Drawing Binary Heap")
    G = graphviz.Graph('Binary Heap', node_attr={'shape': 'record'})
    G.node(str(heap.key),
           f"<f0> k:{heap.key} | <f1> v:{heap.value}")
    to_explore = [heap]
    while len(to_explore) > 0:
        current_node = to_explore.pop()
        if current_node.left != None:
            G.node(str(current_node.left.value),
                   f"<f0> k:{current_node.left.key} | <f1> v:{current_node.left.value}")
            G.edge(str(current_node.value), str(current_node.left.value))
            to_explore.append(current_node.left)
        if current_node.right != None:
            G.node(str(current_node.right.value),
                   f"<f0> k:{current_node.right.key} | <f1> v:{current_node.right.value}")
            G.edge(str(current_node.value), str(current_node.right.value))
            to_explore.append(current_node.right)

    file_name = os.path.join(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.realpath(__file__)))), "plots", "heaps", name)
    G.render(file_name, format='png')
    Logger.important(f"Binary heap graph saved as {file_name}")


def test_bst_get():
    Logger.print_title("Testing BST get", char='=', total_length=50)
    tree = BinarySearchTree.default_tree()
    draw_binary_tree(tree, "default_tree")
    for i in range(2, 31, 2):
        v = tree.get(i)
        if (v != i):
            Logger.important(
                f"BST: get test failed, get({i}) should return {i}, instead got {v}.", Logger.RED)
            return False
    Logger.important("BST: get test passed.", Logger.GREEN)
    return True


def test_bst_update_overwrite():
    Logger.print_title("Testing BST update overwrite",
                       char='=', total_length=50)
    tree = BinarySearchTree.default_tree()
    for i in range(2, 31, 2):
        tree.update(i, i*10)
        if (tree.get(i) != i*10):
            Logger.important(
                f"BST: update overwrite test failed, value at key {i} should be updated to {i*10}, instead it is {tree.get(i)}.", Logger.RED)
            return False
    draw_binary_tree(tree, "tree_after_overwrite")
    Logger.important("BST: update overwrite test passed.", Logger.GREEN)
    return True


def test_bst_update_new():
    Logger.print_title("Testing BST update insert", char='=', total_length=50)
    tree = BinarySearchTree(4, 4)
    keys = [0, 2, 1, 3, 6, 8, 5, 7]
    for i in keys:
        tree.update(i, i)
    draw_binary_tree(tree, "tree_after_insertion")
    for i in keys+[4]:
        v = tree.get(i)
        if (v != i):
            Logger.important(
                f"BST: update insert test failed, value at key {i} should be updated to {i}, instead got {v}.", Logger.RED)
            return False
    Logger.important("BST: update insert test passed.", Logger.GREEN)
    return True


def test_heap_property(heap: BinaryHeap):
    if not heap.left and not heap.right:
        return True
    if heap.left:
        if heap.left.key < heap.key:
            Logger.important(
                f"Heap: heap property violated. k:{heap.left.key} is child of k:{heap.key}", Logger.RED)
            return False
        if heap.right:
            if heap.right.key < heap.key:
                Logger.important(
                    f"Heap: heap property violated. k:{heap.right.key} is child of k:{heap.key}", Logger.RED)
                return False
            return test_heap_property(heap.left) and test_heap_property(heap.right)
        return test_heap_property(heap.left)


def test_heap_pop():
    Logger.print_title("Testing Heap get", char='=', total_length=50)
    heap = BinaryHeap.default_heap()
    draw_heap(heap, "default_heap")
    item = heap.pop()
    if item != 0:
        Logger.important(
            f"Heap: item popped should be 0, but get {item}.", Logger.RED)
        return False
    draw_heap(heap, "heap_after_pop")
    passed = test_heap_property(heap)
    if passed:
        Logger.important(
            "Heap: pop test passed. Check plots/heaps/heap_after_pop.png to see if the heap looks correct.", Logger.GREEN)
    return True


def test_heap_push():
    Logger.print_title("Testing Heap push", char='=', total_length=50)
    heap = BinaryHeap.default_heap()
    heap.push(-1, -1)
    draw_heap(heap, "heap_after_push")
    item = heap.pop()
    if item != -1:
        Logger.important(
            f"Heap: heap root after push should be -1, but get {item}.", Logger.RED)
        return
    passed = test_heap_property(heap)
    if passed:
        Logger.important(
            "Heap: push test passed. Check plots/heaps/heap_after_push.png to see if the heap looks correct.", Logger.GREEN)
