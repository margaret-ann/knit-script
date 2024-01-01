# Script to generate pattern for basic raglan sweater inspired by "Donegal Wool Easy Sweater" sold on Toast
# https://us.toa.st/products/donegal-wool-easy-sweater-cinnamon

import garment as gar

# User input: 1 inch gauge
rowGauge = 3
colGauge = 5

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
ribbing_depth = 1.5
neck_shaping_depth = 1
front_neck = (1/3)*full_neck
back_neck = (1/3)*full_neck
arm_neck = (1/6)*full_neck
full_yoke = pit_to_pit + 2*arm_hole - 4*under_arm
yoke_arm = arm_hole - under_arm
yoke_front = pit_to_pit/2 - under_arm

# Create our objects
raglan = gar.Garment(rowGauge, colGauge)
raglan.addTarget("full neck", True, full_neck)

# Pattern math

# Pattern text

