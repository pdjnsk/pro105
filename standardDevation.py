data = [60,61,65,63,98,99,90,95,91,96]

def mean(data):
    n = len(data)
    total = 0

    for x in data:
        total += int(x)

    mean = total/n

    return mean

     
squaredList= []
for number in data:

    a = int(number) - mean(data)
    a= a**2
    squaredList.append(a)

sum =0

for i in squaredList:

    sum =sum + i


result = sum/ (len(data)-1)

print(sum)



