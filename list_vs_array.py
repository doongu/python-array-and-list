from array import array

list_large = list(range(0, 10**6))
arr_large = array('I', list_large)

print('list_rage sizeof : ', list_large.__sizeof__())
print('arr_large sizeof : ', arr_large.__sizeof__())