import csv


def getData(path, numberOfTests):
    students = []
    with open(path, mode='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            sLog = {
                'name': lines[0],
                'section': lines[1],
                #'score': lines[2]
            }
            for i in range(2, numberOfTests + 2):
                if lines[i]:
                    key = 'MTS0' + str(i-1)
                    sLog[key] = lines[i]
            students.append(sLog)
    m = students.pop(0)
    imp_keys = m.keys()
    imp_keys_arr = list(imp_keys)
    imp_keys_arr.remove('name')
    imp_keys_arr.remove('section')
    
    return students, imp_keys_arr
