
def file_to_list(file): #converts the input file to a list in which each element is a line in the input file
    mylines = []
    with open(file,'rt') as myfile:
        for myline in myfile:
            mylines.append(myline)
    relevant = []

    for element in mylines:
        relevant.append(element.strip())

    while '' in relevant:
        relevant.remove('')
  #  while 'Information Technology (CS)' in relevant:
  #      relevant.remove('Information Technology (CS)')
  #  while 'Engineering' in relevant:
  #      relevant.remove('Engineering')
    return relevant


def gate(ar): #returns number of times gate written and max of all score
    i=0
    idx=0
    score =[]
    for elements in ar: 
        idx = idx+1 
        if elements == 'GATE':
            i=i+1
            k=0
            while True:
                k=k+1
                try:
                    if int(ar[idx+k])<1000 and int(ar[idx+k])>=500:
                       score.append(int(ar[idx+k]))
                    else:
                       score.append(-1)
                    break
                except ValueError:
                    pass
    if i!=0:
        return (i, max(score));
    else:
        return (0,0);


def whichcat(ar): #gives category of candidate. 
    index=0
    for elements in ar:
        index=index+1
        if elements == 'General':
            i=0
        if elements == 'Gen - Economically Weak':
            i=1
        if elements == 'OBC-NCL':
            i=2
        if elements == 'SC':
            i=3
        if elements == 'ST':
            i=4
        if elements == 'PH Category:':
            if ar[index] == 'Yes':
                i=-1
                break
    return i;

def fullpart(ar): #checks if applied in full-time or part-time mode
    for elements in ar:
        i=-1
        if elements == 'FullTime':
            i=1;
            break
        if elements == 'PartTime':
            i=0;
            break
    return i;
    
    
list_of_files = []
for i in range(1,5159,2):
    list_of_files.append(str(i)+'.txt')

filegen =[]
filegenews=[]
fileobc=[]
filesc=[]
filest=[]
fileph=[]
filepart=[]
erroneous=[]
for file in list_of_files:
    ar = file_to_list(file)
    if fullpart(ar)==0:
        filepart.append(file)
    elif fullpart(ar)==1:
        if whichcat(ar) in [0,1,2,3,4,-1] and gate(ar)[1] >= xxx:
            filegen.append(file)
        elif whichcat(ar) == 1 and gate(ar)[1] >= xxx and gate(ar)[1] < xxx:
            filegenews.append(file)
        elif whichcat(ar) == 2 and gate(ar)[1] >=xxx and gate(ar)[1] < xxx:
            fileobc.append(file)
        elif whichcat(ar) == 3 and gate(ar)[1] >= xxx and gate(ar)[1] < xxx:
            filesc.append(file)
        elif whichcat(ar) == 4 and gate(ar)[1] >= xxx and gate(ar)[1] < xxx:
            filest.append(file)
        elif whichcat(ar) == -1 and gate(ar)[1] >= xxx and gate(ar)[1] < xxx:
            fileph.append(file)
        else:
            erroneous.append(file)

with open("filegen.txt", 'w') as output:
    for row in filegen:
        output.write(str(row) + '\n')

with open("filegenews.txt", 'w') as output:
    for row in filegenews:
        output.write(str(row) + '\n')

with open("fileobc.txt", 'w') as output:
    for row in fileobc:
        output.write(str(row) + '\n')

with open("filesc.txt", 'w') as output:
    for row in filesc:
        output.write(str(row) + '\n')

with open("filest.txt", 'w') as output:
    for row in filest:
        output.write(str(row) + '\n')

with open("fileph.txt", 'w') as output:
    for row in fileph:
        output.write(str(row) + '\n')

with open("filepart.txt", 'w') as output:
    for row in filepart:
        output.write(str(row) + '\n')

with open("filegen.txt", 'w') as output:
    for row in filegen:
        output.write(str(row) + '\n')

