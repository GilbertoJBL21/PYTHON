from urllib import request


class hash_table():
    def __init__(self):
        self.table = [None] * 127
    
    def Hash_func(self, value):
        key = 0
        for i in range(0,len(value)):
            key += ord(value[i])
        return key % 127

    def Insert(self, value):
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            self.table[hash] = value
   
    def Search(self,value):
        hash = self.Hash_func(value);
        if self.table[hash] is None:
            return None
        else:
            return hex(id(self.table[hash]))
        

table = hash_table
books =[
    'The Little Prince',
    'The Old Man and the Sea',
    'The Little Mermaid',
    'Beauty and the Beast',
    'The Last Leaf',
    'Alice in WonderLand'
]
for book in books:
    key = sum(map(ord,book))
    table.put(key,book)
for key in table.table.keys():
    print(key, table.table[key])