precip = [None] * 31 
errors = []
with open ("precip2.txt", "r", encoding="utf-8") as file:
    file.readline() 
    loc = file.readline()
    month = file.readline()
    lineNum = 3
    for line in file:
        lineNum += 1 
        parts = line.split() #Читает строку как текст (пр "75\t6.26\n") и .split() разрезает её по пробелам/табам в список: ['75', '6.26']
        if not parts: #Если в строке только пробелы/пусто
            continue# закончить выполнять цикл этого случая
        day = int(parts[0])
        amount = float(parts[1])
        if day < 1 or day > 31: # проверка на invalid day
            errors.append("Invalid       " + day_str + "         " + line_str)
        elif precip[day - 1] is not None:
            day_str = str(day).rjust(3) #Итоговая строка должна состоять ровно из 3 символов. Cтрока короче чем 3 симв пр '8' .rjust(3) допишет перед 8 два пробела
            line_str = str(lineNum).rjust(3)
            errors.append("Repeated      " + day_str + "         " + line_str)
        else:
            precip[day - 1] = amount
with open("Report.txt", "w", encoding="utf-8") as out:
    out.write("Programmer: Dwight Barnette\n")
    out.write("CS 1044 Project 5 Fall 2008\n\n")
    out.write("Precipitation report for " + loc + " during " + month + "\n\n")
    out.write("Error         Day       Line\n")
    for err in errors:
        out.write(err + "\n")
    out.write("\n")
    out.write("Day Amount Graph\n")
    for d in range(1, 32):
        val = precip[d - 1]
        d_str = str(d).rjust(3)
        if val is None:
            out.write(d_str + "     NA\n")
        else:
            if val == 0:
                stars_count = 0
            else:
                stars_count = math.ceil(val / 0.25)
            stars = "*" * stars_count
            val_str = str(round(val, 2))
            if len(val_str.split(".")[1]) == 1:
                val_str = val_str + "0"
            out.write(d_str + "   " + val_str + " " + stars + "\n")
    out.write("\n")
    valid_data = []
    for x in precip:
        if x is not None:
            valid_data.append(x)
    out.write("Minimum     Maximum     Average\n")
    if not valid_data:
        out.write("   NA          NA          NA\n")
    else:
        v_min = min(valid_data)
        v_max = max(valid_data)
        v_avg = sum(valid_data) / len(valid_data)
        min_str = str(round(v_min, 2)).rjust(7)
        max_str = str(round(v_max, 2)).rjust(11)
        avg_str = str(round(v_avg, 2)).rjust(11)
        out.write(min_str + max_str + avg_str + "\n")