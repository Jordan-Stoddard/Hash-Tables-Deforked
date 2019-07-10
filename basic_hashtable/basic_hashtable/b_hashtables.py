

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0

# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    h = 3313

    for char in string:
        h = ((h << 5) + h) + ord(char)
    return h % max

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    for item in hash_table.storage:
        try:
            if item.key == key:
                return print('That key already exists in this hashtable.')
        except AttributeError:
            continue
    
    hash_table.storage[hash_table.count] = Pair(key, value)
    hash_table.count += 1


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    removed = False
    for i in range(hash_table.count):
        if removed:
            hash_table.storage[i - 1] = hash_table.storage[i]
        elif hash_table.storage[0].key == key:
            removed = True
    if removed:
        hash_table.count -= 1
        hash_table.storage[hash_table.count] = None
    else:
        print('Key not found in Hash Table.')


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    for item in hash_table.storage:
        try:
            if item.key == key:
                return item.value
        except AttributeError:
            continue
    return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
