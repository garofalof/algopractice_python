class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node) -> None:
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def add(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self.remove(node)
            self.add(node)
        else:
            node = Node(key, val)
            self.cache[key] = node

            if self.size < self.cap:
                self.size += 1
                self.add(node)
            else:
                tail_prev_key = self.tail.prev.key
                del self.cache[tail_prev_key]
                self.remove(self.tail.prev)
                self.add(node)


"""
Explanation:

The Node class represents a node in the linked list. Each node contains a key and val to store the key-value pair, and prev and next pointers to maintain the doubly linked structure. The LRUCache class initializes the cache with a given capacity. It also initializes the cache dictionary, head, and tail nodes. The size variable keeps track of the current number of items in the cache.

The remove method removes a given node from the linked list by adjusting the prev and next pointers of its neighboring nodes. The add method adds a given node to the front of the linked list by adjusting the prev and next pointers of the head node and its neighboring nodes.

The get method retrieves the value associated with a given key. If the key exists in the cache, the corresponding node is moved to the front of the linked list (since it was recently used) using the remove and add methods, and its value is returned. If the key doesn't exist in the cache, -1 is returned.

The put method inserts or updates the value associated with a given key. If the key exists in the cache, the corresponding node is updated with the new value, and it is moved to the front of the linked list using the remove and add methods. If the key doesn't exist in the cache, a new node is created and added to the front of the linked list. If the cache has reached its capacity, the least recently used item is evicted by removing it from the cache and the linked list, and the new node is added to the front.

Notes:

Time Complexity: O(1) for all methods

Space Complexity: O(n), where n is the cache capacity
"""

# Test Case 1: Basic operations
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
cache.put(4, 4)
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4

# Test Case 2: Capacity of 1
cache = LRUCache(1)
cache.put(1, 1)
assert cache.get(1) == 1
cache.put(2, 2)
assert cache.get(1) == -1
assert cache.get(2) == 2

# Test Case 3: Max capacity and operations
cache = LRUCache(3000)
for i in range(3000):
    cache.put(i, i)
assert cache.get(0) == 0
assert cache.get(2999) == 2999
cache.put(3000, 3000)
assert cache.get(1) == -1
assert cache.get(3000) == 3000

# Test Case 4: Maximum calls to get and put
cache = LRUCache(3000)
for i in range(2 * 105):
    cache.put(i, i)
    cache.get(i // 2)
    cache.put(i // 2, i // 2)
assert cache.get(0) == 0
assert cache.get(2 * 105 - 1) == 2 * 105 - 1
