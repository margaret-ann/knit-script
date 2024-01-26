# Generate the most basic ribbed raglan pattern possible
import garment as gar
import math

#Define 4cm gauge of garment
colGauge = 3 / 2.57 * 4
rowGauge = 5 / 2.57 * 4

#Define garment measurements
wrist = gar.Measurement("wrist", True, 23, colGauge, rowGauge, [2]) #1x1 ribbing count
bust = gar.Measurement("bust", True, 122, colGauge, rowGauge, [2]) #1x1 ribbing count
neck = gar.Measurement("neck", True, 59, colGauge, rowGauge, [2]) #1x1 ribbing count
arm = gar.Measurement("arm", True, 46, colGauge, rowGauge) #includes underArm
underArm = gar.Measurement("underArm", True, 5, colGauge, rowGauge)
bodyLength = gar.Measurement("bodyLength", False, 28, colGauge, rowGauge) #includes ribbing
armLength = gar.Measurement("armLength", False, 38, colGauge, rowGauge) #includes ribbing
raglanDepth = gar.Measurement("raglanDepth", False, 20, colGauge, rowGauge) #does not include ribbing
ribDepth = gar.Measurement("ribDepth", False, 5, colGauge, rowGauge)
NeckShapeDepth = gar.Measurement("NeckShapeDepth", False, 3, colGauge, rowGauge)

garment = [bust, neck, arm, underArm, wrist, bodyLength, armLength, raglanDepth, ribDepth, NeckShapeDepth]

#Define decrease and increase types
sleeve_inc_row = 2 #intend to inc 2 stitches per decrease row of sleeve (M1L, M1R)
yoke_dec_row = 8 #intend to dec 16 stitches per increase row of yoke (K2tog, SSK)

#Make a sleeve rate decision
wristTarget = wrist.getTargetStitches()
armTarget = arm.getTargetStitches()
armLengthTarget = arm.getTargetStitches() - ribDepth.getTargetStitches()

#Define Rate Estimates
sleeve_rate_est = (arm.getTargetStitches()-wrist.getTargetStitches())/armLength.getTargetStitches()

#Define Decrease Type
sleeve_inc_row = 2 #intend to inc 2 stitches per decrease row of sleeve (M1L, M1R)
yoke_dec_row = 8 #intend to dec 16 stitches per increase row of yoke (K2tog, SSK)

#Make a sleeve rate decision
wristTarget = wrist.getTargetStitches()
armTarget = arm.getTargetStitches()
armLengthTarget = arm.getTargetStitches() - ribDepth.getTargetStitches()

rate_error = 0
sleeve_rates = []
min_sleeve_error = 100
sleeve_rate_choice = None
interval_guess = 1 #1 means increase every row
while True:
    rate_guess = sleeve_inc_row/interval_guess
    calc_arm = rate_guess*armLengthTarget+wristTarget
    calc_error = abs(calc_arm-armTarget)/armTarget
    if calc_error < min_sleeve_error:
        min_sleeve_error = calc_error
        sleeve_rate_choice = (rate_guess, interval_guess, calc_error)
    sleeve_rates.append((rate_guess, interval_guess, calc_error))
    if rate_guess < sleeve_rate_est:
        break
    interval_guess += 1

#Solidify pattern up to start of yoke
armActual = (armLength.getActualStitches()-(armLength.getActualStitches()%sleeve_rate_choice[1]))*sleeve_rate_choice[0]
arm.setActualStitches(armActual)

#Make a yoke rate decision
bustActual = bust.getActualStitches()
underArmActual = underArm.getActualStitches()
neckTarget = neck.getTargetStitches()
raglanDepthActual = raglanDepth.getActualStitches()

yokeActual = bustActual + 2 * (armActual - underArmActual)
yoke_rate_est = (yokeActual-neckTarget)/raglanDepthActual

rate_error = 0
yoke_rates = []
min_yoke_error = 100
yoke_rate_choice = None
interval_guess = 1 #1 means decrease every row
while True:
    rate_guess = yoke_dec_row/interval_guess
    calc_neck = yokeActual - rate_guess * raglanDepthActual
    calc_error = abs(calc_neck-neckTarget)/neckTarget
    if calc_error < min_yoke_error:
        min_yoke_error = calc_error
        yoke_rate_choice = (rate_guess, interval_guess, calc_error)
    yoke_rates.append((rate_guess, interval_guess, calc_error))
    if rate_guess < yoke_rate_est:
        break
    interval_guess += 1

#Solidify pattern up to neck
neckActual = yokeActual - ((raglanDepthActual-(raglanDepthActual%yoke_rate_choice[1]))*yoke_rate_choice[0])
neck.setActualStitches(neckActual)

#Write CSV with final measurements & error
f = open("bespoke-raglan.csv", "w")
f.write("name; target_cm; target_in; targetStitches; actualStitches; actual_cm; actual_in; error\n")
for meas in garment:
    f.write(f"{meas.getSummary()}\n")
f.close()

#TODO: Calculate some useful metrics for good design
#percent of arm stitches at neck
#percent of body stitches at neck

#Create text for pattern instructions
row_c = 1
title = "The Bespoke Bottom-Up Raglan"
pattern = []
pattern.append(f"{title}")

pattern.append("")
pattern.append(f"Section 1. Knit the Body")
row_c = 1
pattern.append(f"Using your favorite method, CO {bust.getActualStitches()} stitches in the round.")
pattern.append(f"Row {row_c}-{row_c+ribDepth.getActualStitches()}: Knit 1x1 ribbing.")
row_c = row_c + ribDepth.getActualStitches() + 1
pattern.append(f"Row {row_c}-{row_c+bodyLength.getActualStitches()-ribDepth.getActualStitches()}: Knit all stitches.")
row_c = row_c + bodyLength.getActualStitches() - ribDepth.getActualStitches() + 1
pattern.append(f"When complete, body should measure about {round(bodyLength.getActualCm())}cm, including the ribbing. Place all {bust.getActualStitches()} body stitches on hold while you make the sleeves.")

pattern.append("")
pattern.append(f"Section 2. Knit the Sleeves")
row_c = 1
pattern.append(f"Using your favorite method, CO {wrist.getActualStitches()} sleeve stitches.")
pattern.append(f"Row {row_c}-{row_c+ribDepth.getActualStitches()}: Knit 1x1 ribbing.")
row_c = row_c + ribDepth.getActualStitches() + 1
pattern.append(f"Row {row_c}-{row_c+sleeve_rate_choice[1]-2}: Knit all stitches.")
pattern.append(f"Row {row_c+sleeve_rate_choice[1]-1}: Increase round")
pattern.append(f"Repeat rows {row_c}-{row_c+sleeve_rate_choice[1]-1} {armLength.getActualStitches()//sleeve_rate_choice[1]-1} more times. When complete, you should have {arm.getActualStitches()} stitches on your needle.")
if armLength.getActualStitches()%sleeve_rate_choice[1] != 0:
    pattern.append(f"Knit {armLength.getActualStitches()%sleeve_rate_choice[1]} rows")
pattern.append(f"When complete, the sleeve should measure about {armLength.getActualCm()}cm, including the ribbing. Cut the yarn, and place all {arm.getActualStitches()} sleeve stitches on hold while you make a second sleeve.")
pattern.append(f"Once the second sleeve is complete, cut the yarn and move to section 3.")

pattern.append("")
pattern.append(f"Section 3. Join the Body and Sleeves")
row_c = 1
raglanBody = int((bust.getActualStitches()-underArm.getActualStitches()*2)/4)
raglanSleeve = arm.getActualStitches()-underArm.getActualStitches()
pattern.append(f"Row {row_c}: Return to the body stitches that you put on hold at the end of section 1. Knit {raglanBody} body stitches, PM, knit {raglanSleeve} left sleeve stitches, PM, knit {raglanBody*2} body stitches, PM, knit {raglanSleeve} right sleeve stitches, PM, knit to end of round.")
if bust.getActualStitches() != (raglanBody)*4+2*underArm.getActualStitches():
    print("RAISE ERROR: There was a rounding error while diving the body sections")
row_c = row_c+1
pattern.append(f"Row {row_c}: Decrease round {yoke_rate_choice[2]}")
pattern.append(f"Row {row_c}: Knit all stitches")
pattern.append(f"Row {row_c}-{row_c}: Repeat rows X and Y x more times. When complete, you should have X stitches ")

pattern.append("")
pattern.append(f"Section 4. Knit the Yoke")

#Write to a txt file
f = open("bespoke-raglan.txt", "w")
for row in pattern:
    f.write(f"{row}\n")
f.close()
