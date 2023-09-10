#CREATING A SIMPLE CALCULATOR!!
#CODE BY PRITAM x ANK
import os 
os.system("clear")
a = "\033[1;35m\033[1m\033[5m            [[ CREATED BY ]] \033[1;35m\033[1m\033[5m [[ ANKxPRT ]]             "
print(a)
print()
print()
num1 = int(input("\033[0;32m ENTER FIRST NUMBER "))
num2 = int(input("\033[0;32m ENTER SECOND NUMBER "))

print('\033[0;35m\033[1m______________________________________')
print()
# DISPLAY HOW  NUM WHAT DO.........

print("\033[0;34m\033[1m [1] FOR ADDITION")
print("\033[0;34m\033[1m [2] FOR SUBTRACTION")
print("\033[0;34m\033[1m [3] FOR MULTIPLECTION")
print("\033[0;34m\033[1m [4] FOR DIVISION")
print()
op = int(input("\033[1;31m ENTER  "))

print()
# CONDITION if elif and else.
if op == 1:
   print("\033[1;36m ANSWER " , num1+num2)
elif op == 2:
     print("\033[1;36m ANSWER " , num1-num2)
elif op == 3:
     print("\033[1;36m ANSWER " , num1*num2)
elif op == 4 :
     print("\033[1;36m ANSWER " , num1/num2)

else:
   print("\033[1;33mTRY FOR ANK")
print()
