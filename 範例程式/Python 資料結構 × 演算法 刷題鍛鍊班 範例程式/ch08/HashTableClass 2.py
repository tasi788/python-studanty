class MapEntry :
  def __init__( self, key, value ):
    self.key = key
    self.value = value
class HashTable:
  def __init__(self, M = 101):
    self.m = M
    self.table = [None]*self.m
  def add(self, key, value):
    entry = MapEntry(key, value)
    slot = abs(hash(key)) % self.m
    while self.table[slot] :  #occupied
      slot = (slot + 1) % self.m
    self.table[slot] = entry
  def get(self, key):
    slot = abs(hash(key)) % self.m
    while self.table[slot] and \
          self.table[slot].key != key: 
      slot = (slot + 1) % self.m
    if not self.table[slot]:  #search failed
      return None
    return self.table[slot].value

def main():
  h = HashTable()
  keys = list(map(int, input().split()))
  values = input().split()
  for i in range(len(keys)):
    h.add(keys[i], values[i])
  while True:
    keyin = input("input a key:")
    if not keyin: break
    print(h.get(int(keyin)))
  print('Bye')  
if __name__ == '__main__':
  main()