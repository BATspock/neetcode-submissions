import bisect
class MyHashSet:

    def __init__(self):
        #initialize a binary search
        self.arr = []
        self.len = len(self.arr)
    
    def return_index(self, key: int)->int:
        index = bisect.bisect_left(self.arr, key)
        if index < self.len and self.arr[index] == key:
            return index
        return -1

    def add(self, key: int) -> None:
        # add element and reconstrcut
        # find the closest index
        index = self.return_index(key)
        if index == -1:
            bisect.insort(self.arr, key)
            self.len+=1

    def remove(self, key: int) -> None:
        # remove element and reconstruct
        # check if contains works
        index = self.return_index(key)
        if index!=-1:
            self.arr.pop(index)
            self.len-=1
    
    def contains(self, key: int) -> bool:
        # do a binary search
        if self.return_index(key) != -1:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)