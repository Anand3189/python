
#string methods:
#1.upper(): printing in uppercase
x="hyderabad"
print(x.upper())

#2.lower():To print in lowercase
x="MUMBAI"
print(x.lower())

#3.capitalize():For capitalizing the 1st character of a string 
x="india"
print(x.capitalize())

#4.tiltle():For capitalizing the 1st character of each word in a string
x="good evening hyderabad"
print(x.title())

#5.replace():For replacing a portion of a string
x="Java is easy"
print(x.replace("Java","Python"))

#6.swapcase(): For converting one case to another
x="good evening hyderabad"
print(x.swapcase())

#7.count():To count the no of occurences of a sub-string or a character
x="hello hello hello....how are you???"
print(x.count("hello"))
print(x.count("h"))

data='''1. Python is Simple
2. Python is user-friendly
3. Python supports interactive mode
4. Python supports 89300 modules
5. Python has many built-in libraries
6. Python supports object-oriented programming
7. Python supports all major databases
8. Python is dynamic typed
9. Python provides simple syntaxes
10.Python is extensible.
'''
print(data.count("Python"))
print(data.count("python"))
print(data.lower().count("python"))

#8.format():For substitutions
x="{} is the captain of Indian Team"
print(x.format("Rohith"))

#ex:2
x="{} is the {} of {}"
print(x.format("Delhi","capital","India"))
print(x.format("Modi","PM","India"))
print(x.format("Python","most popular","all languages"))

#9.strip():For removing the blankspaces before and after the string
x="            Good Evening Hyderabad                 "
print(x,len(x))

y=x.strip()
print(y,len(y))

#10.lstrip():left most strip
y=x.lstrip()
print(y,len(y))

#11.rstrip():right most strip
y=x.rstrip()
print(y,len(y))

#12.find():To check whether a sub-string is available or not
#If found,it returns the 1st character index position of the sub-string
#else it returns -1

x="python is easier than Java and python is simpler than Java"
print(x.find("Java"))
print(x.find("python"))
print(x.find("devops"))

#13.rfind():right most find
print(x.rfind("Java"))
print(x.rfind("python"))
print(x.rfind("devops"))

#14.split():If we split a string,we get a list
x="Good Evening hyderabad"
#Task: Extract only hyderabad from the above
y=x.split(" ")
print(y,type(y))
print(y[2])

#ex:2
emp="101,Ajay,50000,Manager"
#Extract--->only name and designation
y=emp.split(",")
print(y,type(y))
print(y[1],y[3])













































































