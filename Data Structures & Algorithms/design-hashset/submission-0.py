class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        current_pointer = self.set[key % len(self.set)]

        while current_pointer.next:
            if current_pointer.next.key == key:
                return                
            current_pointer = current_pointer.next

        current_pointer.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        current_pointer = self.set[key % len(self.set)]

        while current_pointer.next:
            if current_pointer.next.key == key:
                current_pointer.next = current_pointer.next.next
                return                
            current_pointer = current_pointer.next
        

    def contains(self, key: int) -> bool:
        current_pointer = self.set[key % len(self.set)]

        while current_pointer.next:
            if current_pointer.next.key == key:
                return True
            current_pointer = current_pointer.next

        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)