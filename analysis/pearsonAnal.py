from scipy.stats.stats import pearsonr

#  import items data
with open('items/allItems.txt') as f:
    allItems = [line.split()[0] for line in f.readlines()]

#  import weather data
with open('weather-2015-Aug.txt') as f:
    weatherTemp = [map(float, line.split()[1:]) for line in f.readlines()]

def isWeekday(day):
    if day % 7 >= 2:
        return True
    return False

def correlates(results):
    for factor in range(5):
        if abs(results[factor][0]) >= 0.5 and results[factor][1] <= 0.05:
            return True
    return False
    
#  prepare weather data
weather = [[], [], [], [], []]
for day in range(31):
    if isWeekday(day):
        for factor in range(5):
            weather[factor].append(weatherTemp[day][factor])

#  import item sales per day data           
data = []
for day in range(31):
    with open('items/' + str(day + 1) + '.txt') as f:
        temp = [line.split()[:2] for line in f.readlines()]
        data.append({temp[day][0] : temp[day][1] for day in range(len(temp))})
        
save = ''
for item in allItems:
    sales = []
    for day in range(31):
        if isWeekday(day):
            sales.append(float(data[day].get(item, "0")))
    
    results = [pearsonr(sales, weather[factor]) for factor in range(5)]
    
    if correlates(results):
        save += item + '\n'
        for factor in range(5):
            save += ' '.join(map(str, results[factor])) + '\n'
        save += '\n'

#  save results
savefile = open('pearsonCor.txt', 'w')
savefile.write(save)
savefile.close()
        