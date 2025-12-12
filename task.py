class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        # Compute the hash index for the given key
        key_hash = self.hash_function(key)

        # If bucket is empty, nothing to delete
        if self.table[key_hash] is None:
            return "Item not found"
        
        for index, pair in enumerate(self.table[key_hash]):
            if pair[0] == key:
                del self.table[key_hash][index]

                if len(self.table[key_hash]) == 0:
                   self.table[key_hash] = None

                return "Item deleted successfully"
        # Key was not found inside the bucket
        return "Item not found"



# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.get("apple"))   # Виведе: 10
print(H.get("orange"))  # Виведе: 20
print(H.get("banana"))  # Виведе: 30

print(H.delete("banana"))