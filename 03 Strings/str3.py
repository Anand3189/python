#String slicing: Extracting particular portion of a string
x="python program"
#Extract-->only "python"
print(x[0:6]) #Always upper bound is excluded
#Extract--->"prog"
print(x[7:11])
print(x[11:7])#Empty string-->bcoz always slicing in the forward direction
#Extract--->"prog" using -ve index
print(x[-7:-3])
#Extract-->"program"
print(x[7:14])
print(x[7: ])
print(x[-7: ])
print(x[ :6])
print(x[ : ])
print(x[:])
print(x)
print(x[0: ])
print(x[0:14:2]) #(startvalue,stopvalue,stepvalue)
print(x[::2])
print(x[::-1]) #reverses the string

#palindrome: If we reverse a string,if we get the same string then it is a palindrome
#ex: madam,malayalam,dad,eye,level,radar,racecar

x="madam"
print(x)

y=x[::-1]
print(y)














