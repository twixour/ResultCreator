from pdf_template_rkv import rkv_temp  # import the template
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from data import *
from rkvGraphy import *
import base64
from PIL import Image
import os


def create_pdf(student, result_string, pdfName, chart, folderPath, full_marks, pass_marks, testName):
    candidateScore = student[testName]
    
    if(float(candidateScore) < 0):
        candidateScore = 'NA'
    pdfFolderLocation = os.path.join(folderPath, 'pdf')
    imageFolderLocation = os.path.join(folderPath, 'image')
    if (not os.path.exists(pdfFolderLocation)):
        os.mkdir(pdfFolderLocation)
    if (not os.path.exists(imageFolderLocation)):
        os.mkdir(imageFolderLocation)
    pdf_path = folderPath + '/pdf/'
    c = canvas.Canvas(pdf_path + pdfName, pagesize=letter)
    c = rkv_temp(c)  # run the template

    c.setFillColorRGB(0, 0, 0)  # font colour
    c.setFont("Helvetica", 17)
    row_gap = 0.6  # gap between each row
    line_y = 7.5  # location of fist Y position

    # Test Information
    c.drawString(0, 8.4*inch, 'Test Number:- ')
    c.drawRightString(3*inch, 8.4*inch, str(testName))

    c.drawString(3.5*inch, 8.4*inch, 'FM:- ')
    c.drawRightString(4.75*inch, 8.4*inch, str(full_marks))

    c.drawString(5.3*inch, 8.4*inch, 'PM:- ')
    c.drawRightString(6.5 * inch, 8.4*inch, str(pass_marks))
    c.setFont("Helvetica", 20)
    c.drawString(0.1*inch, line_y*inch, str(student['name']))  # p Name
    c.drawRightString(3.3*inch, line_y*inch,
                      str(student['section']))  # p Price
    c.drawRightString(4.8*inch, line_y*inch, str('Maths'))  # p Qunt
    c.drawRightString(5.7*inch, line_y*inch,
                      str(candidateScore))  # Sub Total
    c.setFont("Helvetica", 15)
    c.drawRightString(7*inch, line_y*inch,
                      str(result_string))

    line_y = line_y-row_gap

    c.setFont("Times-Bold", 22)
    c.setFillColorRGB(1, 0, 0)  # font colour
    myChartImg = base64.b64decode(chart)
    imuri = f'data:image/png;base64,{(myChartImg)}'
    # c.drawInlineImage(myChartImg, 0.1*inch, 6.3*inch)
    # c.drawString(0.1*inch, 6.3*inch, imuri)

    filename = folderPath + '/image/' + \
        f"{student['name']}-result.png"
    with open(filename, 'wb') as f:
        f.write(myChartImg)
    img = Image.open(filename)
    img = img.resize((int(img.width/1.8), int(img.height/1.8)))

    c.drawInlineImage(img, inch*0.01, inch*2.8)

    c.showPage()
    c.save()
# c.drawRightString(7*inch, 2.1*inch, str(float(total)))  # Total
