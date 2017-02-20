items = set()

for i in range(31):
    with open(str(i+1)+'.txt') as f:
        data = f.readlines()
    
    for line in data:
        items.add(line.split()[0])

save = ''
for item in items:
    save += item.replace('/', '-') + '\n'
    
savefile = open("allItems.txt", 'w')
savefile.write(save)
savefile.close()