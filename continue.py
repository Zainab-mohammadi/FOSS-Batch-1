#break function
number = 0

for number in range(10):
   number = number + 1

   if number == 5:
      break   

   print('Number is ' + str(number))

print('Out of loop')

#continue function
number = 0

for number in range(10):
   number = number + 1

   if number == 5:
      continue  

   print('Number is ' + str(number))

print('Out of loop')
