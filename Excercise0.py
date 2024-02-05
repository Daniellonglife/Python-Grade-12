#Print the lenght of my string
my_str = "Hello, World!"
print (len(my_str)) 

#print world from my_string
print (my_str[6:11])

#Print character H in my string
print (my_str[0])

#print "Hello, WOrld " from my string
print (my_str.upper())

#print "hello, world " from my string
print (my_str.lower())

#print "Bye Bye World " from my string
print (my_str.replace('Hello', "Bye Bye") )

#print a splited my_string 
print (my_str.split(","))

#print this is my world say Hello World 
print("This is my world, say" + ' '+ '"' + (my_str) + '"')

Student_name = "Not a real student name"
grade = 12

print(f"my name is {Student_name} from grade {grade}")