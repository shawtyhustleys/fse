s = int(input())
hrs = (s // 3600) % 24
min = (s // 60) % 60
sec = s % 60
print("{:d}:{:02d}:{:02d}".format(hrs, min, sec))