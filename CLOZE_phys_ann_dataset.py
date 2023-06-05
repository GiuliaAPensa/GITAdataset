f = open("sample.txt", "w")
print('"actor":')
x = input().split()
print('"objects":')
y = input().split()

#story number
print("story_number (same as example_id, in quotes):")
o = input()
print('{',o, ': ', file = f)
#story_id
print("story_id (NO quotes, NO letter, only number):")
a = input()
print('{"story_id":', a, file = f)
#worker_id
print("worker_id (in quotes):")
b = input()
print(', "worker_id":', b, file = f)
#type
print("type (NULL for positive, ORDER, or CLOZE, in quotes):")
c = input()
print(', "type":', c, file = f)
#idx:
print("idx (null, or 0):")
d = input()
print(', "idx":', d, file = f)
#aug: false senza comillas
print("aug (false):")
e = input()
print(', "aug":', e, file = f)
#actor
print(', "actor":', x, file = f)
#location
print("location (in quotes):")
g = input()
print(', "location":', g, file = f)
#objects
print(', "objects":', y, file = f)
print("sentences (separated by tabs):")
g = input().split('\t')
print(', "sentences": [', file = f)
for element in g:
    print(f'"{element}", ', file=f)
#length siempre 5
print("length:")
h = input()
print(', "length":', h, file = f)
#example_id = alla story_id
print("example_id (same as story number, in quotes):")
i = input()
print(', "example_id":', i, file = f)
#plausible senza virgolette
print("plausible:")
l = input()
print(', "plausible":', l, file = f)
#breakpoint sempre -1 per le storie che sono true
print("breakpoint:")
m = input()
print(', "breakpoint":', m, file = f)
#confl_sents:[]
print("confl_sents (conflict sentence, other than breakpoint):")
n = input()
print(', "confl_sents": [', n, ']', file = f)
#confl_pairs:[]
print(', "confl_pairs":', '[[', n, '],[', m, ']]' ,file = f)


#PHYSICAL STATES
for element_h in x:
    print(', "states":\n[{"h_location": [["', element_h, '", 0]], "conscious": [["', element_h, '", 0]], "wearing": [["', element_h, '", 0]], "h_wet": [["', element_h, '", 0]], "hygiene": [["', element_h, '", 0]], ', file=f)

print('"location": [', file=f)
for element in y:
    print(f' ["{element}", 0],', file=f)

print('], "exist": [', file=f)
for element in y:
    print(f'["{element}", 0],', file=f)

print('], "clean": [', file=f)
for element in y:
    print(f'["{element}", 0],', file=f)

print('], "power": [', file=f)
for element in y:
    print(f'["{element}", 0],', file=f)

print('], "functional": [', file=f)
for element in y:
    print(f'["{element}", 0],', file=f)

print('], "pieces": [', file=f)
for element in y:
    print(f'["{element}", 0],', file=f)

print('], "wet": [', file=f)
for element in y:
    print(f'["{element}", 0],', file=f)

print('], "open": [', file=f)
for element in y:
    print(f'["{element}", 0],', file=f)

print('], "temperature": [', file=f)
for element in y:
    print(f'["{element}", 0],', file=f)

print('], "solid": [', file=f)
for element in y:
    print(f'["{element}", 0],', file=f)

print('], "contain": [', file=f)
for element in y:
    print(f'["{element}", 0],', file=f)

print('], "running": [', file=f)
for element in y:
    print(f'["{element}", 0],', file=f)

print('], "moveable": [', file=f)
for element in y:
    print(f'["{element}", 0],', file=f)

print('], "mixed": [', file=f)
for element in y:
    print(f'["{element}", 0],', file=f)

print('], "edible": [', file=f)
for element in y:
    print(f'["{element}", 0],', file=f)


print("]", file=f)
f.close() 

#FORMATTING

with open("sample.txt") as r:
  text = r.read().replace("['", '"')
  
with open("sample.txt", "w") as w:
  w.write(text)

f.close() 


with open("sample.txt") as r:
  text = r.read().replace("']", '"')
  
with open("sample.txt", "w") as w:
  w.write(text)

f.close()


with open("sample.txt") as r:
  text = r.read().replace("', '", ', ')
  
with open("sample.txt", "w") as w:
  w.write(text)

f.close()

with open("sample.txt") as r:
  text = r.read().replace(", \n,", "]\n, ")
  
with open("sample.txt", "w") as w:
  w.write(text)

f.close()

with open("sample.txt") as r:
  text = r.read().replace("],\n]", "]]")
  
with open("sample.txt", "w") as w:
  w.write(text)

f.close
