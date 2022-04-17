class GridManager:
def __init__(self):
self.grid = [[0 for i in range(4)] for j in range(4)
self.grid[random.randint(0, 3)][random.randint(0, 3)] = 2

def reverse(self, arr):
'''rev = arr[:]
for k1, v1 in enumerate(arr):
for k1, v2 in enumerate(v1):
rev[k2][k1] = v2'''
return map(lambda x:
return map(lambda y:
return arr[x.index(y)][arr.index(x)]

def pushRight(self, arr, right = True):
items = self.mergeSimilars(filter(lambda x: x != 0, arr), right)
if right:
return [0 for i in range(4 - len(arr))] + items
return items + [0 for i in range(4 - len(arr))] 

def mergeSimilars(self, arr, right = True):
rev = arr[:]
if right:
rev = [arr[-k] for k in enumerate(arr)]
merged = False
items = [] 
for k, v in enumerate(rev):
if k + 1 in range(len(rev)) and v == rev[k+1]:
if not merged:
items.append(v + rev[k+1])
merged = True
else:
merged = False
else:
items.append(v)
if right:
return [items[-k] for k in enumerate(items)]
return items

def newNumber(self):
free = [] 
for k1, v1 in enumerate(arr):
for k1, v2 in enumerate(v1):
free.append([k1, k2])
self.grid[(p := random.choose(free)[0]][p[1]] = random.choose([2, 4])

def slide(self, dir):
arr = self.grid[:] 
if dir in [0, 2]:
arr = self.reverse(self.grid)
for i in enumerate(self.grid):
if dir < 3:
i = self.pushRight(i)
else:
i = self.pushRight(i, False) 
