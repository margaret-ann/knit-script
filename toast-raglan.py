# Script to generate pattern for basic raglan sweater inspired by "Donegal Wool Easy Sweater" sold on Toast
# https://us.toa.st/products/donegal-wool-easy-sweater-cinnamon

import garment as gar

# User input: 1 inch gauge
colGauge = 3
rowGauge = 5

# User input: Target garment measurements in inches
full_neck = 23
pit_to_pit = 48 #includes under_arm
arm_hole = 18 #includes under_arm
under_arm = 2
wrist = 9
body_length = 11 #without ribbing
arm_length = 14 #without ribbing
raglan_depth = 8 #without ribbing

# Other calculated or constant target garment measurements
ribbing_depth = 2 #same for all sizes
neck_shaping_depth = 1 #same for all sizes
front_neck = (1/3)*full_neck
back_neck = (1/3)*full_neck
arm_neck = (1/6)*full_neck
full_yoke = pit_to_pit + 2*arm_hole - 4*under_arm
yoke_arm = arm_hole - under_arm
yoke_front = pit_to_pit/2 - under_arm

# Create our objects
raglan = gar.Garment(rowGauge, colGauge)
raglan.addTarget("full neck", True, full_neck, [4]) # %2,4
raglan.addTarget("pit to pit", True, pit_to_pit, [4]) # %2,4
raglan.addTarget("arm hole", True, arm_hole)
raglan.addTarget("under arm", True, under_arm) # odd, 7
raglan.addTarget("wrist", True, wrist, [4]) # %2,4
raglan.addTarget("body length", False, body_length)
raglan.addTarget("arm length", False, arm_length)
raglan.addTarget("raglan depth", False, raglan_depth)
raglan.addTarget("ribbing depth", False, ribbing_depth)
raglan.addTarget("neck shaping depth", False, neck_shaping_depth)
raglan.addTarget("front neck", True, front_neck)
raglan.addTarget("back neck", True, back_neck)
raglan.addTarget("arm neck", True, arm_neck)
raglan.addTarget("full yoke", True, full_yoke)
raglan.addTarget("yoke arm", True, yoke_arm)
raglan.addTarget("yoke front", True, yoke_front)

#Do pattern math
print("Calculating Actual Design Measurements from Targets:")
raglan.calculateMeasurements(rowGauge, colGauge)
raglan.printSummary()


# Error calculation

# Pattern text
pattern_text = []
pattern_text.append(f"Using smaller needles, CO {raglan.targetStitchesByName("pit to pit")} in the round using long-tail method.")
pattern_text.append(f"Row 1-5: Knit all stitches.")
pattern_text.append(f"Row 6-11: K2, P2 ribbing.")
pattern_text.append(f"Row 12: *P1, K3, P1, K3, P1, K{raglan.targetStitchesByName("pit to pit")/2-9}* repeat once.")
pattern_text.append(f"Repeat row 12 until body measures {raglan.targetSizeByName("body length")+raglan.targetSizeByName("ribbing depth")} inches with stockinette after CO held uncurled.")

print()
print("PATTERN TEXT:")
for each in pattern_text:
    print(each)
