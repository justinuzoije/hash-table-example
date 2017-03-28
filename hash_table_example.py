class MyHashTable:
    def __init__(self):
        # Nothing
        self.table = [];

    def hash(self, value):
        # Assume value is a string
        # Return hashed value.
        self.value = value
        # num_index = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        first_letter = self.value[0]
        # letter_index = index()
        return alphabet.index(first_letter)

myTable = MyHashTable()
print myTable.hash('apple')
print myTable.hash('banana')
