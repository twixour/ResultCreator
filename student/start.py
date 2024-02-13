import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from data import *
from main import *

# create the root window
root = tk.Tk()
root.title('Student Results PDF Generator')
root.resizable(False, False)
root.geometry('400x300')
csvPath = ''
students = []
finalTestNameList = []

# START button command

folderPath = ''


def select_folder_path():
    global folderPath
    folderPath = fd.askdirectory()


def select_file(numberOfTests):
    global students
    global csvPath
    global finalTestNameList

    filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a csv file',
        initialdir='/',
        filetypes=filetypes)
    csvPath = filename
    students, finalTestNameList = getData(filename, int(numberOfTests))
    


def launchGeneration(testName, fullMarks, passMarks, numberOfTests, folderPath, finalTestNameList):
    global students
    
    if (len(students) > 0):
        
        if (testName and fullMarks and passMarks and numberOfTests):
            startMain(students, fullMarks, [testName], passMarks, folderPath, finalTestNameList)
            noDataLabelVar.set("PDF Generated.")

        else:
            noDataLabelVar.set("Enter test name, full marks\n and pass marks")
    else:
        noDataLabelVar.set(
            "No Data to Work with.\n Please select a csv file")


# END button command

# START GUI
# TEST NAME
testNameLabel = ttk.Label(root, text="Test Name")
testNameLabel.grid(row=1, column=1)
testLabelEntry = ttk.Entry(root)
testLabelEntry.grid(row=1, column=3)
# TEST NAME ENDS

# FULL MARKS
fullMarksLabel = ttk.Label(root, text="Full Marks")
fullMarksLabel.grid(row=2, column=1)
fullMarksLabelEntry = ttk.Entry(root)
fullMarksLabelEntry.grid(row=2, column=3)
# FULL MARKS ENDS

# PASS MARKS
passMarksLabel = ttk.Label(root, text="Pass Marks")
passMarksLabel.grid(row=3, column=1)
passMarksLabelEntry = ttk.Entry(root)
passMarksLabelEntry.grid(row=3, column=3)
# PASS MARKS ENDS

#Number Of Tests Field
numberOfTestsLabel = ttk.Label(root, text="Number Of Tests")
numberOfTestsLabel.grid(row=4, column=1)
numberOfTestsLabelEntry = ttk.Entry(root)
numberOfTestsLabelEntry.grid(row=4, column=3)
#Number of Tests Field Ends

# PDF LOCATION STARTS
pdf_location_selection_button = ttk.Button(
    root,
    text='Choose PDF Location',
    command=select_folder_path
)

pdf_location_selection_button.grid(row=6, column=1)
# PDF LOCATION ENDS

# CSV FILE AND PDF GENERATION
open_button = ttk.Button(
    root,
    text='Open a CSV File',
    command= lambda: select_file(numberOfTestsLabelEntry.get())
    
)

open_button.grid(row=7, column=1)

pdfGenerateButton = ttk.Button(
    root, text='PDF Generate', command=lambda: launchGeneration(testLabelEntry.get(), fullMarksLabelEntry.get(), passMarksLabelEntry.get(), numberOfTestsLabelEntry.get(),folderPath, finalTestNameList))

pdfGenerateButton.grid(row=7, column=3)
# CSV FILE AND PDF GENERATION ENDS


noDataLabelVar = tk.StringVar()
noDataLabel = ttk.Label(
    root, textvariable=noDataLabelVar)
noDataLabel.grid(row=5, column=1)
# END GUI


# run the application

root.mainloop()
