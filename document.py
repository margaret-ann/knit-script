# 'Document' class hierarchy
# Creates a pdf document based on garment pattern and data 
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import ParagraphStyle
import styles

P_HEIGHT=defaultPageSize[1]
P_WIDTH=defaultPageSize[0]

class Document:
    def __init__(self, garment, data, logoPath):
        self.garment = garment
        self.title = data.__dict__['patternTitle']
        self.subtitle = data.__dict__['patternSubtitle']
        self.yarnWeight = data.__dict__['yarnWeight']
        self.yarnType = data.__dict__['yarnType']
        self.needleSize_mm = data.__dict__['needleSize_mm']
        self.needleSize_US = data.__dict__['needleSize_US']
        self.skillLevel = data.__dict__['skillLevel']
        self.introSection = data.__dict__['patternIntro']
        self.sizingSection = data.__dict__['patternSizing']
        self.needleSection = data.__dict__['patternNeedles']
        self.yarnSection = data.__dict__['patternYarn']
        self.gaugeSection = data.__dict__['patternGauge']
        self.notionsSection = data.__dict__['patternNotions']
        self.abbrevSection = data.__dict__['patternAbbrev']
        self.sizeChart = data.__dict__['patternSizeChart']
        self.fileName = f"{self.title.lower().replace(' ', '')}pattern.pdf"
        self.docTitle = f"{self.title} Pattern"
        self.title = self.title
        self.subtitle = self.subtitle
        self.logoPath = logoPath

        # Register our font
        pdfmetrics.registerFont(
            TTFont('IMFell', 'IMFellEnglish-Regular.ttf')
        )

        # Set up stylesheet for document paragraphs
        style = getSampleStyleSheet()

        self.buildDocument()

    def myCoverPage(self, canvas, doc):
        canvas.saveState()

        # Draw title
        canvas.setFont('IMFell', 50)
        canvas.drawCentredString(P_WIDTH/2, P_HEIGHT-3*inch, self.title)

        # Draw first footer
        canvas.setFont('IMFell', 25)
        canvas.drawCentredString(P_WIDTH/2, P_HEIGHT-4*inch, self.subtitle)

        #canvas.drawString(inch, 0.75 * inch, "First Page / %s" % self.subtitle)
        canvas.restoreState()

    def myLaterPages(self, canvas, doc):
        canvas.saveState()

        # Draw footer
        canvas.setFont('IMFell', 15)
        canvas.drawString(0.4 * inch, 0.4 * inch, "Page %d %s" % (doc.page, ""))

        canvas.restoreState()

    def buildDocument(self):

        # Create the document template
        doc = SimpleDocTemplate(
                self.fileName,
                pagesize=letter,
                topMargin = 0.5*inch,
                bottomMargin = 0.5*inch,
                leftMargin = 0.5*inch,
                rightMargin = 0.5*inch,
        )

        Story = [Spacer(1,7*inch)]

        # Introduction section
        for para in self.introSection:
            p = Paragraph(para, styles.introStyle)
            Story.append(p)
            Story.append(Spacer(1,0.2*inch))
        Story.append(PageBreak())

        # Sizes
        Story.append(Paragraph("Sizes", styles.titleStyle))
        Story.append(Spacer(1,0.2*inch))
        for para in self.sizingSection:
            p = Paragraph(para, styles.patternStyle)
            Story.append(p)
            Story.append(Spacer(1,0.2*inch))
        Story.append(Spacer(1,0.2*inch))

        # Yarn
        Story.append(Paragraph("Yarn", styles.titleStyle))
        Story.append(Spacer(1,0.2*inch))
        for para in self.yarnSection:
            p = Paragraph(para, styles.patternStyle)
            Story.append(p)
            Story.append(Spacer(1,0.2*inch))
        Story.append(Spacer(1,0.2*inch))

        # Needles
        Story.append(Paragraph("Needles", styles.titleStyle))
        Story.append(Spacer(1,0.2*inch))
        for para in self.needleSection:
            p = Paragraph(para, styles.patternStyle)
            Story.append(p)
            Story.append(Spacer(1,0.2*inch))
        Story.append(Spacer(1,0.2*inch))

        # Gauge
        Story.append(Paragraph("Gauge", styles.titleStyle))
        Story.append(Spacer(1,0.2*inch))
        for para in self.gaugeSection:
            p = Paragraph(para, styles.patternStyle)
            Story.append(p)
            Story.append(Spacer(1,0.2*inch))
        Story.append(Spacer(1,0.2*inch))

        # Notions
        Story.append(Paragraph("Notions", styles.titleStyle))
        Story.append(Spacer(1,0.2*inch))
        for para in self.notionsSection:
            p = Paragraph(para, styles.patternStyle)
            Story.append(p)
            Story.append(Spacer(1,0.2*inch))
        Story.append(Spacer(1,0.2*inch))

        # Abbreviations
        Story.append(Paragraph("Abbreviations", styles.titleStyle))
        Story.append(Spacer(1,0.2*inch))
        Story.append(PageBreak())

        # Size chart & size diagram
        Story.append(Paragraph("Size Chart & Fit Guide", styles.titleStyle))
        Story.append(Spacer(1,0.2*inch))
        Story.append(Table(self.sizeChart))
        Story.append(PageBreak())

        # Write pattern instructions
        Story.append(Paragraph("Pattern Instructions", styles.titleStyle))
        Story.append(Spacer(1,0.2*inch))
        for line in self.garment.getPattern():
            p = Paragraph(line, styles.patternStyle)
            Story.append(p)
            Story.append(Spacer(1,0.08*inch))
        
        # Build document
        doc.build(Story, onFirstPage=self.myCoverPage, onLaterPages=self.myLaterPages)