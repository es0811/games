import random
user_action=''
print('Type exit to quit and get scores!')
you,computer=0,0
while(user_action!='exit'):
  user_action=input('Enter a choice (rock, paper, scissors):')
  possible_actions=['rock','paper','scissors']  
  computer_action=random.choice(possible_actions)
  if user_action==computer_action:
    print(f'Both the players selected {user_action}. It is a tie!')
  
  elif user_action=='rock':
    if computer_action=='scissors':
      print('Rock smashes scissors. You win!')
      you+=1
    else:
      print('Paper covers rock. You lose!')
      computer+=1
  
  elif user_action=='paper':
    if computer_action=='scissors':
      print('Scissors cut paper. You lose!')
      computer+=1
    else:
      print('Paper covers rock. You win!')
      you+=1
  elif user_action=='scissors':
    if computer_action=='rock':
      print('Rock smashes scissors. You lose!')
      computer+=1
    else:
      print('Scissors cut paper. You win!')
      you+=1
if you>computer:
  print('You win the game. Congratulations!')
      
elif you<computer:
  print('You lose the game. Better luck next time!')

else:
  print('Its a tie! Consider yourself a winner!')
  