# 'Document' class hierarchy
# Used to generate the pdf pattern for a garment design
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import ParagraphStyle

class Document:
    def __init__(self, garment, title, subtitle):
        self.garment = garment
        self.fileName = f"{title.lower().replace(' ', '')}pattern.pdf"
        self.docTitle = f"{title} Pattern"
        self.title = title
        self.subtitle = subtitle

        #Create pdf object
        self.pdf = canvas.Canvas(self.fileName, pagesize=letter)
        self.pdf.setTitle(self.docTitle)
        pdfmetrics.registerFont(
            TTFont('IMFell', 'IMFellEnglish-Regular.ttf')
        )

        #Build pattern cover
        self.createCover()

        #Size & measurement information

        #Yarn information

        #Yardage information

        #Gauge information

        #Needle information

        #Print pattern text
        self.createPattern()

        self.pdf.save()

    def createCover(self):
        self.pdf.setFont('IMFell', 36)
        self.pdf.drawCentredString(300, 700, self.title)
        self.pdf.setFont('IMFell', 20)
        self.pdf.drawCentredString(300, 600, self.subtitle)


    def createPattern(self):
        textobject = self.pdf.beginText()
        textobject.setTextOrigin(10, 500)
        textobject.setFont('IMFell', 12)
        for line in self.garment.getPattern():
            textobject.textLine(line)
        self.pdf.drawText(textobject)

