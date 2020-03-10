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
        self.elements_count = 0
        self.initial_size = capacity

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
        return self._hash(key) % int(self.capacity)

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
                    self.elements_count += 1
                    return
                elif current_pair.next is None:
                    current_pair.next = LinkedPair(key, value)
                else:
                    current_pair = current_pair.next

        else:
            self.storage[index] = LinkedPair(key, value)

        self.elements_count += 1
        self.resize()

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
            self.elements_count -= 1
        elif current_node is not None:
            while current_node.key != key:
                current_node = current_node.next
                previous_node = previous_node.next
            previous_node.next = current_node.next
            self.elements_count -= 1
        else:
            print("Warning: Key not found")

        self.resize()

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
        initial_element_count = self.elements_count
        load_factor = self.elements_count / self.capacity
        if .2 < load_factor < .7:
            return

        old_storage = self.storage

        if load_factor < .2 and self.capacity == self.initial_size:
            return
        if load_factor > .7:
            self.capacity *= 2
        else:
            self.capacity /= 2

        self.storage = [None] * int(self.capacity)

        for bucket_item in old_storage:
            if bucket_item is not None:
                self.insert(bucket_item.key, bucket_item.value)
                while bucket_item.next is not None:
                    self.insert(bucket_item.next.key, bucket_item.next.value)
                    bucket_item = bucket_item.next

        self.elements_count = initial_element_count



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
