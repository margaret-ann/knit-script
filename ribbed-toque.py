# Generate basic 2x2 ribbed, rolled-brim toque pattern
import garment as gar
import math

#Define 4cm gauge of knitting
colGauge = 13 / 10 * 4
rowGauge = 21 / 10 * 4

#Target size chart
size_names = ["Newborn", "3-6 Months", "6-12 Months", "Toddler", "Child", "Adult S", "Adult L"]
size_chart = [ #(circumference, length)
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
        gar.Measurement("head_circ", True, c, colGauge, rowGauge, [4], rounding='error'),
        gar.Measurement("length", False, l, colGauge, rowGauge, rounding='error'),
    ]
    garments.append(gar.Garment(rowGauge, colGauge, measurements))

#Function to write pattern for crown of hat
def build_crown(circ_stitches):
    """ Return pattern text for the crown of the hat based on number of circumference stitches """
    assert int(circ_stitches) % 4 == 0, 'Error: This pattern requires the CO to be divisible by 4'
    ptn_str = []
    dec1 = circ_stitches * (3/4) #P2tog, K2
    dec2 = dec1 * (2/3) #P, K2tog
    dec3 = dec2 * (1/2) #K2tog
    ptn_str += [f"Decrease row 1: P2tog, K2 ({int(dec1)} stitches)",
                "Knit in pattern for 3 rows",
                f"Decrease row 2: P, K2tog ({int(dec2)} stitches)",
                "Knit in pattern for 3 rows",
                f"Decrease row 3: K2tog ({int(dec3)} stitches)"]
    if dec3 % 3 == 0:
        dec4 = dec3 * (1/3) #K3tog
        ptn_str += [f"Decrease row 4: K3tog ({int(dec4)} stitches)"]
    elif dec3 % 3 == 1:
        ptn_str += [f"TBD"]
    elif dec3 % 3 == 2:
        ptn_str += [f"TBD"]
    ptn_str += ["Cut yarn with 10cm tail. Use tapestry needle to thread tail through remaining stitches. Pull yarn tight & weave in ends."]

    return ptn_str

#Generate pattern text & add to garment objects
for index, thisHat in enumerate(garments):
    thisHat.addPattern([f"CO {thisHat.actualStitchesByName('head_circ')} stitches using the long-tail method"])
    thisHat.addPattern([f"P2, K2 every round until hat measures {thisHat.targetSizeByNameCm('length')}cm from brim"])
    thisHat.addPattern(build_crown(thisHat.actualStitchesByName('head_circ')))
    text = thisHat.getPattern()
    print(size_names[index])
    for line in text:
        print(f"{line}")
    print()