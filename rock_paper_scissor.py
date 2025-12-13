print("========================")

print("Rock Paper Scissors")

print("========================")
print("1) ✊")
print("2) 🖐️")
print("3) ✌️")
import random
player = int(input("Pick a number: "))
computer = random.randint(1,3)
if player ==1 :
  player_choice="✊"
elif player ==2 :
  player_choice="🖐️"
elif player ==3 :
  player_choice="✌️"  

if computer ==1 :
  computer_choice="✊"
elif computer ==2 :
  computer_choice="🖐️"
elif computer ==3 :
  computer_choice="✌️" 
print("You chose:",player_choice)
print("CPU chose:",computer_choice)

if player == 1  and computer == 2:
  print("The cpu won!")
elif player==2 and computer==1:
  print("The player won!")
elif player==1 and computer==3:
  print("The player won!")
elif player==3 and computer==1:
  print("The cpu won!")
elif player==2 and computer==3:
  print("The cpu won!")
elif player==3 and computer==2:
  print("The player won!")
elif player==computer:
  print("Oops tied!")
