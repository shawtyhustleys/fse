x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 > 0 and y1 >0:
    quarter1 = "I"
elif x1 < 0 and y1 > 0:
    quarter1 = "II"
elif x1 < 0 and y1 < 0:
    quarter1 = "III"
else:
    quarter1 = "IV"
if x2 > 0 and y2 >0:
    quarter2 = "I"
elif x2 < 0 and y2 > 0:
    quarter2 = "II"
elif x2 < 0 and y2 < 0:
    quarter2 = "III"
else:
    quarter2 = "IV"
if quarter1 == quarter2:
    print(f"yes, {quarter1}")
else: print("no")
