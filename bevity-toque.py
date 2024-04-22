# Brevity Toque Pattern
# Basic 2x2 ribbed, rolled-brim hat

import pattern as p
import garment as g
import measurement as m
import document as doc
import math
import patternData as pd

# Define 10cm gauge
colGauge = 13
rowGauge = 21

#Target size chart in cm
size_names = ["Premie", "Newborn", "3-6 Months", "6-12 Months", "Toddler", "Child", "Teen", "Adult S", "Adult M", "Adult L"]
dim_names = ["circumference", "length"]
size_chart = [
    (30, 11), #premie
    (36, 15), #newborn
    (43, 18), #3-6 mo
    (46, 19), #6-12 mo
    (48, 20), #toddler
    (51, 22), #child
    (53, 25), #teen
    (56, 28), #adult S
    (59, 28), #adult M
    (62, 29), #adult L
]
row1 = size_names.copy()
row1.insert(0,"")
row2 = [i[0] for i in size_chart]
row2.insert(0,dim_names[0])
row3 = [i[1] for i in size_chart]
row3.insert(0,dim_names[1])
sizeTable = [row1, row2, row3]

# Initalize pattern metadata object
pattern_data = pd.PatternData(
    colGauge = colGauge,
    rowGauge = rowGauge,
    patternTitle = "Brevity Toque",
    patternSubtitle = "A bulky, knit hat to fit heads of all sizes.",
    yarnWeight = "worsted + worsted = bulky",
    yarnType = "Malabrigo Worsted held double",
    needleSize_mm = 6.5,
    needleSize_US = 10.5,
    skillLevel = "beginner",
    patternIntro = ["""The classic 2x2 ribbed style hat has been a favorite of mine for years. It's
        comfortable to wear and simple to knit. After much experimenting, I present to you the Brevity
        Toque. Knit with Malabrigo Worsted held double, this hat is squishy and soft, while
        producing a fabric thick enough to keep you warm.""",
        """The heart of this pattern is for you to be able to make it for anyone that you love
        of any size. See the sizing section for more information.""",
        """If you are new to knitting, then welcome! This pattern is a great place to start for the adventurous beginner."""],
    #patternSizing = [],
    #patternNeedles = [],
    #patternYarn = [],
    #patternGauge = [],
    #patternNotions = [],
    #patternAbbrev = [],
    patternSizeChart = sizeTable
)

#Create a garment object for each size
garments = []
for c, l in size_chart:
    measurements = [
        m.Measurement("head_circ", True, c, colGauge, rowGauge, [4], rounding='error'),
        m.Measurement("length", False, l, colGauge, rowGauge, rounding='error'),
    ]
    garments.append(g.Garment(rowGauge, colGauge, measurements))

myPattern = p.Pattern(rowGauge, colGauge, size_names, dim_names, size_chart, garments)

#Function to write pattern for crown of hat
def build_crown(circ_stitches, hatPattern):
    """ Return pattern text for the crown of the hat based on number of circumference stitches """
    #assert int(circ_stitches) % 4 == 0 and int(circ_stitches) == circ_stitches, 'Error: This pattern requires the CO to be divisible by 4'
    #assert int(circ_stitches) >= 6, 'Error: This pattern requires the CO to be greater than 6'
    ptn_str = []
    dec1_list, dec2_list, dec3_list, dec4_list = [], [], [], []
    for size in circ_stitches:
        dec1 = size * (3/4) #P2tog, K2
        dec2 = dec1 * (2/3) #P, K2tog
        dec3 = dec2 * (1/2) #K2tog
        dec1_list.append(int(dec1))
        dec2_list.append(int(dec2))
        dec3_list.append(int(dec3))
    ptn_str += [f"Decrease row 1: P2tog, K2 ({hatPattern.formatDimension(dec1_list)} stitches)",
                "Knit in pattern for 3 rows",
                f"Decrease row 2: P, K2tog ({hatPattern.formatDimension(dec2_list)} stitches)",
                "Knit in pattern for 3 rows",
                f"Decrease row 3: K2tog ({hatPattern.formatDimension(dec3_list)} stitches)"]
    for index, dec3 in enumerate(dec3_list): #sizes diverge for dec4
        this_size = []
        if dec3 % 3 == 0: #case 1: div by 3
            this_size = [3] * (dec3//3)
        elif dec3 % 3 != 0:
            if dec3 % 3 == 1: #case 2: remainder 1
                this_size = [3] * (dec3//3-1)
                this_size.insert(0, 2)
                this_size.insert(math.ceil(len(this_size)/2), 2)
            elif dec3 % 3 == 2: #case 3: remainder 2
                this_size = [3] * (dec3//3)
                this_size.insert(int(len(this_size)//2), 2)
        dec4_list.append(this_size)

    case1_index = []
    case2_index = []
    for index, size in enumerate(dec4_list):
        if len(set(size)) == 1: #case 1: all elements are the same
            #ptn_str += [f"Decrease row 4: K3tog ({int(dec4)} stitches)"]
            case1_index.append((index + 1, len(dec4_list[index])))
        else: #case 2: all elements are not the same
            case2_index.append((index + 1, len(dec4_list[index])))
    ptn_str += [f"For sizes {hatPattern.formatDimension(list(i[0] for i in case1_index))} only - Decrease row 4: K3tog ({hatPattern.formatDimension(list(i[1] for i in case1_index))} stitches)"]
    for index, stitches in case2_index:
        dec4_str = ""
        dec4_str += f"For size {index} - Decrease row 4: "
        for i in range(len(dec4_list[index-1])):
            dec4_str += f"K{dec4_list[index-1][i]}tog"
            if i == len(dec4_list[index-1])-1:
                break
            dec4_str += ", "
        dec4_str += f" ({stitches} stitches)"
        ptn_str += [dec4_str]
    ptn_str += ["Cut yarn with 20cm tail. Use tapestry needle to thread tail through remaining stitches. Pull yarn tight & weave in ends."]
    return ptn_str

#Generate pattern text & add to garment objects
crown_height_cm = math.floor(8 * (10/rowGauge))
full_length_list_cm = myPattern.getTargetCmDimension('length')
length_list_cm = [x - crown_height_cm for x in full_length_list_cm]
myPattern.appendPattern([f"CO {myPattern.formatDimension(myPattern.getStitchDimension('head_circ'))} stitches using the long-tail method or another stretchy cast-on of your choice"])
myPattern.appendPattern([f"P2, K2 every round until hat measures {myPattern.formatDimension(length_list_cm)}cm from CO brim"])
myPattern.appendPattern(build_crown(myPattern.getStitchDimension('head_circ'), myPattern))

#Print text pattern to terminal
text = myPattern.getPattern()
for line in text:
    print(f"{line}")

#Generate pattern pdf
logoPath = "logo1.jpg"
myDocument = doc.Document(myPattern, pattern_data, logoPath)