# Generate basic 2x2 ribbed, rolled-brim toque pattern
import pattern as p
import garment as g
import measurement as m
import document as doc
import math

#User input of 10cm gauge
#colGauge = int(input("Enter 10cm column gauge: "))
#rowGauge = int(input("Enter 10cm row gauge: "))

#10cm gauge of Malabrigo Worsted held double
colGauge = 13
rowGauge = 21

#General pattern information
yarnWeight = ""
yarnType = "Malabrigo Worsted held double"
needleSize = ""
skillLevel = "beginner"

#Target size chart
size_names = ["Newborn", "3-6 Months", "6-12 Months", "Toddler", "Child", "Adult S", "Adult L"]
dim_names = ["circumference", "length"]
size_chart = [
    (35.5, 12.5),
    (40.5, 15.5),
    (45.5, 16.5),
    (48, 17.5),
    (51, 19.5),
    (56, 25.5),
    (61, 29),
]

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
myPattern.appendPattern([f"CO {myPattern.formatDimension(myPattern.getStitchDimension('head_circ'))} stitches using the long-tail method"])
myPattern.appendPattern([f"P2, K2 every round until hat measures {myPattern.formatDimension(myPattern.getTargetCmDimension('length'))}cm from brim"])
myPattern.appendPattern(build_crown(myPattern.getStitchDimension('head_circ'), myPattern))

#Print text pattern to terminal
text = myPattern.getPattern()
for line in text:
    print(f"{line}")

#Generate pattern pdf
myTitle = "Brevity Toque"
mySubtitle = "A bulky, knit hat to keep your entire family warm."
myDocument = doc.Document(myPattern, myTitle, mySubtitle)