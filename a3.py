import sys
b = 1921000
mb = b / (1024*1024)
print("b in mb:", mb, "MB")
b_n = 3 ** 9090001
mb_n = sys.getsizeof(b_n) / (1024*1024)
print("b_n in mb_n:", mb_n , "MB")