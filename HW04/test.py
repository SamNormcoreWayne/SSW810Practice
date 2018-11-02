'''
def integers():
    i = 0
    while True:
        yield i
        i += 1


gen = integers()
for i in range(3):
    print(next(gen))
    print(gen)

for i in range(5):
    if i == 4:
        break
    elif i == 2:
        continue
    print(i)
'''

for i in range(0, 4, 2):
    for j in range(2):
        print(i, j)
