"""
Find avg of N numbers
 > User enters the number of characters to be entered
 > Users provides the values from input
 > Count is calculated as values
 >

"""
number = int(input("Enter number of integers:: "))
total_sum = 0

for i in range(number):
    num = float(input("Enter Number " + str(i) + ": "))
    total_sum += num

avg = total_sum/number
print("Average of Given values is:: %f" %(avg))


