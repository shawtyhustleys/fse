x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
steps1 = x1 + y1
steps2 = x2 + y2
color1 = "White" if steps1 % 2 == 0 else "Black"
color2 = "White" if steps2 % 2 == 0 else "Black"
same = "YES" if color1 == color2 else "NO"
print(same)
print(color1 if same == "YES" else "", end="") # else "", end="" ничего не пиши, не переходи на новую строчку, замри,  тольуо для того чтобы закончить конструкцию без измен.
