from reportlab.lib.units import inch
from PIL import Image


def rkv_temp(c):

    c.translate(inch, inch)
# define a large font
    c.setFont("Times-Bold", 32)
# choose some colors
    c.setStrokeColorRGB(0, 0, 0)
    c.setFillColorRGB(1, 0, 0)  # font colour
    # c.drawImage('D:\\top2.jpg', -0.8*inch, 9.3*inch)
    c.drawString(0, 9*inch, "RAMAKANT VIDYAPITH")
    c.setFont("Times-Bold", 16)
    c.drawString(0, 8.7*inch, "Branch I: Kanhauli; Branch II: Goshala")
    c.setFillColorRGB(0, 0, 0)  # font colour

    c.line(0, 8.2*inch, 6.8*inch, 8.2*inch)

    c.setFillColorRGB(1, 0, 0)  # font colour
    c.setFont("Times-Bold", 40)

    c.rotate(45)  # rotate by 45 degree
    # font colour CYAN, MAGENTA, YELLOW and BLACK
    c.setFillColorCMYK(0, 0, 0, 0.08)
    c.setFont("Helvetica", 140)  # font style and size
    c.drawString(2*inch, 1*inch, "RESULT")  # String written
    c.rotate(-45)  # restore the rotation
    c.setFillColorRGB(0, 0, 0)  # font colour
    c.setFont("Times-Roman", 20)
    c.drawString(0.5*inch, 7.9*inch, 'Name')
    c.drawString(2.9*inch, 7.9*inch, 'Section')
    c.drawString(4*inch, 7.9*inch, 'Subject')
    c.drawString(5.12*inch, 7.9*inch, 'Score')
    c.drawString(6.2*inch, 7.9*inch, 'Result')
    c.setStrokeColorCMYK(0, 0, 0, 1)  # vertical line colour
    c.line(2.8*inch, 8.0*inch, 2.8*inch, 7.2*inch)  # first vertical line
    c.line(3.9*inch, 8.0*inch, 3.9*inch, 7.2*inch)  # second vertical line
    c.line(5*inch, 8.0*inch, 5*inch, 7.2*inch)  # third vertical line
    c.line(6.1*inch, 8.0*inch, 6.1*inch, 7.2*inch)  # fourth vertical line
    c.line(0.01*inch, 7.2*inch, 7*inch, 7.2*inch)  # horizontal line total

    c.drawString(3.3*inch, 6.8*inch, 'Graph')

    c.setFont("Times-Roman", 22)

    signatureImage = Image.open('signature.png')
    signatureImage = signatureImage.resize(
        (int(signatureImage.width/12), int(signatureImage.height/12)))
    c.drawInlineImage(signatureImage, inch*5.5, inch*.08)

    c.drawString(5.6*inch, -0.1*inch, 'Signature')
    c.setStrokeColorRGB(0.1, 0.8, 0.1)  # Bottom Line colour
    c.line(0, -0.7*inch, 6.8*inch, -0.7*inch)
    c.setFont("Helvetica", 8)  # font size
    c.setFillColorRGB(1, 0, 0)  # font colour
    c.drawString(0, -0.9*inch, u"\u00A9"+" Ramakant Vidyapith")

    return c
