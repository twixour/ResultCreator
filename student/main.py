from pdf_gen import create_pdf
from rkvGraphy import *
from graphyMultiScore import graphMultiRepresent

def startMain(students, fullMarks, testNameList, passMarks, folderPath, finalTestNameList):
    
    full_marks = float(fullMarks)
    pass_marks = float(passMarks)
    testName = testNameList[0].upper()
    highScore = 0
    topperScoreListNew = []
    
    for testName1 in finalTestNameList:
        
        for student in students:
            studentScore = float(student[testName1.upper()])

            if (studentScore > highScore):
                highScore = studentScore
        topperScoreListNew.append(highScore)
        highScore = 0
    # for student in students:
    #     studentScore = float(student[testName])

    #     if (studentScore > highScore):
    #         highScore = studentScore
    #topperScoreList = [highScore]
    
    for student in students:
        studentScoreList = []
        for testNameVar in finalTestNameList:
            studentScoreList.append(float(student[testNameVar]))
        #studentScoreList = [float(student[testName])]

        pdfName = str(student['name']) + '.pdf'
        percentage = (float(student[testName])/full_marks) * 100
        result_string = ''
        
        if(float(student[testName]) < 0):
            result_string = "Absent"
        elif (float(student[testName]) < pass_marks):
            result_string = 'Fail'
        elif (float(student[testName]) >= pass_marks):
            if (percentage <= 70):
                result_string = 'Pass'
            elif (percentage > 70 and percentage <= 90):
                result_string = 'Good'
            elif (percentage > 90 and percentage <= 95):
                result_string = 'V. good'
            elif (percentage > 95 and percentage <= 100):
                result_string = 'Excellent'

        chart = graphMultiRepresent(
            finalTestNameList, studentScoreList, topperScoreListNew, student['name'])

        create_pdf(student, result_string, pdfName, chart,
                   folderPath, full_marks, pass_marks, testName)
