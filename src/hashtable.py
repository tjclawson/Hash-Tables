# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return hash(key)

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        """
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            current_pair = self.storage[index]

            # loop to iterate til next is none or key matches
            while current_pair is not None:
                if current_pair.key == key:
                    current_pair.value = value
                    return
                elif current_pair.next is None:
                    current_pair.next = LinkedPair(key, value)
                else:
                    current_pair = current_pair.next

        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        """
        index = self._hash_mod(key)
        current_node = self.storage[index].next
        previous_node = self.storage[index]
        if previous_node.key == key:
            self.storage[index] = previous_node.next
        elif current_node is not None:
            while current_node.key != key:
                current_node = current_node.next
                previous_node = previous_node.next
            previous_node.next = current_node.next
        else:
            print("Warning: Key not found")

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        """
        index = self._hash_mod(key)
        if self.storage[index]:
            current_pair = self.storage[index]
            while current_pair is not None:
                if current_pair.key == key:
                    return current_pair.value
                else:
                    current_pair = current_pair.next
        else:
            return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        """
        old_storage = self.storage.copy()
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity

        for bucket_item in old_storage:
            if bucket_item is not None:
                self.insert(bucket_item.key, bucket_item.value)
                while bucket_item.next is not None:
                    self.insert(bucket_item.next.key, bucket_item.next.value)
                    bucket_item = bucket_item.next

ht = HashTable(8)

ht.insert("key-0", "val-0")
ht.insert("key-1", "val-1")
ht.insert("key-2", "val-2")
ht.insert("key-3", "val-3")
ht.insert("key-4", "val-4")
ht.insert("key-5", "val-5")
ht.insert("key-6", "val-6")
ht.insert("key-7", "val-7")
ht.insert("key-8", "val-8")
ht.insert("key-9", "val-9")

ht.remove("key-0")
ht.remove("key-1")
ht.remove("key-2")
ht.remove("key-3")
ht.remove("key-4")
ht.remove("key-5")
ht.remove("key-6")
ht.remove("key-7")
ht.remove("key-8")
ht.remove("key-9")


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
