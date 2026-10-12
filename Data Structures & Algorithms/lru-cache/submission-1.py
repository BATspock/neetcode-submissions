class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.val = value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache= {}
        self.cap = capacity
        self.left, self.right = Node(0,0), Node(0,0) #left = lru, right = mru
        self.left.next = self.right
        self.right.prev = self.left

    def add(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            #remove the key from cache and updated
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


