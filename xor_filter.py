class XORFilter:
    def __init__(self):
        self.filter_set = set()

    def add(self, hash_value):
        self.filter_set.add(hash_value)

    def contains(self, hash_value):
        return hash_value in self.filter_set
