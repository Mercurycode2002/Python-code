carddata  = [9880080, 12, 90, 33, 9, 900, 57, 59, 91, 85]
count = 0
for x in range(1, 10):
    valuetoinsert = carddata[x]
    while carddata[x - 1] > valuetoinsert and x>0 :
       carddata[x], carddata[x - 1] = carddata[x - 1], carddata[x]
       x = x - 1
       count = count + 1

       
print(carddata, count)
