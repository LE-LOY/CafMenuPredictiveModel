from scipy.stats.stats import pearsonr

with open('items/allItems.txt') as f:
    allItems = [line.split()[0] for line in f.readlines()]

with open('weather-2015-Aug.txt') as f:
    weatherTemp = [map(float, line.split()[1:]) for line in f.readlines()]

weather = [[], [], [], [], []]
for i in range(31):
    if i % 7 >= 2:
        temp = weatherTemp[i]
        for j in range(5):
            weather[j].append(temp[j])
    
data = []
for i in range(31):
    with open('items/' + str(i+1) + '.txt') as f:
        temp = [line.split()[:2] for line in f.readlines()]
        data.append({temp[i][0] : temp[i][1] for i in range(len(temp))})
        
#print weather
print allItems

save = ''

for item in allItems:
    sales = []
    for i in range(31):
        if i % 7 >= 2:
            sales.append(float(data[i].get(item, "0")))
    
    #to_include = False
    to_include = False
    results = [pearsonr(sales, weather[i]) for i in range(5)]
    
    for i in range(5):
        if abs(results[i][0]) >= 0.5 and results[i][1] <= 0.05:
            to_include = True
    
    if to_include:
        save += item + '\n'
        for i in range(5):
            save += str(results[i][0]) + ' ' + str(results[i][1]) + '\n'
        save += '\n'
    
savefile = open('pearsonCor.txt', 'w')
savefile.write(save)
savefile.close()
        