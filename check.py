import csv
numberOfTests = int(input("Enter the number of tests taken.\n>>>"))
students = []
with open('Tests.csv', 'r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        sLog = {
            'name': lines[0],
            'section': lines[1],
            'MTS01': lines[2],
            
        }
        for i in range(3, numberOfTests+2):
            if lines[i]:
                key = 'MTS0' + str(i-1)
                sLog[key] = lines[i]

        
        students.append(sLog)
        
students.pop(0)

print(students)
    