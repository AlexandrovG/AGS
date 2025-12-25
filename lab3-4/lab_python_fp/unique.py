class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.seen = set()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            try:
                item = next(self.items)
                
                if self.ignore_case and isinstance(item, str):
                    key = item.lower()
                else:
                    key = item
                
                if key not in self.seen:
                    self.seen.add(key)
                    return item
            except StopIteration:
                raise StopIteration

if __name__ == "__main__":
    print("Test Unique with numbers:")
    data1 = [1, 1, 2, 2, 3, 3]
    result1 = list(Unique(data1))
    print(result1)
    
    print("\nTest Unique with strings (ignore_case=False):")
    data2 = ['a', 'A', 'b', 'B', 'a']
    result2 = list(Unique(data2))
    print(result2)