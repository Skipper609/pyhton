lst = [[0,1,2,3],[3,4,5,5],[6,7,8,8],[9,0,1,9]]


print(f"minimum value element in the array:{min(map(lambda x: min(x),lst))}")
print(f"maximum value element in the array:{max(map(lambda x: max(x),lst))}")
col_min = list(min(map(lambda x: x[i],lst)) for i in range(4))
print(f"elements with minimum values column-wise: {col_min}")
col_max = list(max(map(lambda x: x[i],lst)) for i in range(4))
print(f"elements with maximum values column-wise: {col_max}")
row_min = list(map(lambda x:min(x),lst))
row_max = list(map(lambda x:max(x),lst))
print(f"elements with minimum values row-wise: {row_min}")
print(f"elements with maximum values row-wise: {row_max}")