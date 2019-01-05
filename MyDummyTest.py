
s = [{'A': 'bob', 'B': None, 'C': None}, {'A': None, 'B': 'Alice', 'C': None},
     {'A': None, 'B':None, 'C': 'Jack', 'D': None}]

ss = {'A':None, 'B': None, 'C': 'Paul', 'D': None, 'E': 'Dan', 'F': 'GHUs'}

qw = sum(1 for k, v in ss.items() if v is None)

print(qw)

result = sum(sum(1 for v in i.values() if v is None) for i in s if i is not None)

print(result)

