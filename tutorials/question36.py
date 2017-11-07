from bokeh.plotting import output_file,figure,show







from collections import Counter

import json


with open('info.json', 'r') as f:
    #use load in file handling
    #use loads when json is a element
    data = json.load(f)
lst=[]
print("we have the following data :")
for i in data:
    print(" "+i)
    #preparing data for the counter
    var  = data[i].split('/')
    lst.append(var[1])
#takes the lst and shows the frequency
c = Counter(lst)


output_file('plot.html')
# load our x and y data
x = []
y=[]
for i in c:
    y.append(c[i])
    x.append(int(i))

print x
print y

# create a figure
p = figure()

# create a histogram
p.vbar(x=x, top=y, width=0.5)

# render (show) the plot
show(p)