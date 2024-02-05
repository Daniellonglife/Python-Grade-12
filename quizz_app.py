#file name quizz_app.py
#getting the user respond
name = input("What your name ah nop? ")
print("Sur Sdey!!", name )

money = input("I need 5000$ please!!! (Write number 5000$ when you sent it to me) ")
if money == "5000$" :
    print("Thank you for the money(Emoji smile),", name ,)
else: 
    print("Kom bork nh ey bro bro ot torn sent money mor teh(emoji upset) " ,name ,)

print('1.This is question Number Two'
     
 )
print("Please answer this qustion to get the money back if you want. ")

total_point = 0
question = input("2 + 2? ")
if question == "4":
    total_point = total_point + 1 
    print('correct')
else: 
    print("incorrect")

question = input("10 + 2? ")
if question == "12":
    total_point = total_point + 1 
    print('correct')
else: 
    print("incorrect")

question = input("22 + 9? ")
if question == "31":
    total_point = total_point + 1 
    print('correct')
else: 
    print("incorrect")

question = input("200 + 25? ")
if question == "225":
    total_point = total_point + 1 
    print('correct')
else: 
    print("incorrect")

question = input("4950 + 50? ")
if question == "5000":
    total_point = total_point + 1 
    print('correct')
else: 
    print("incorrect")

print( name , f"your score is : ", (int(total_point/5*100)) , "%")

if  total_point >= 60:
    print("Here your money 5000$ mnus jit akrk", name ,)
else:
    print("Sorry pg na nob luy ng ot ban vinh teh ")
#float