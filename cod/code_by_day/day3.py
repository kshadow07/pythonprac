
print('Welcome to Treasure Island challenge')

play=True
if play==True:
 direction= input('where do you want to go left or right:') 
 if direction=='left':
    second_choice=input('You want to swim or wait: ')
    if second_choice=='wait':
        door= input('Which door do you want to go red,blue or yellow: ')
        if door=='yellow':
            print('Congratulations you found the treasure')
        else:
            print('game over')    
    else:
        print('Game Over')
 else:
    print('Game Over')
    
play_again=input('Do you Want to play y or n')    
if play_again=='y':
    play=True
    direction= input('where do you want to go left or right:') 
    if direction=='left':
        second_choice=input('You want to swim or wait: ')
        if second_choice=='wait':
          door= input('Which door do you want to go red,blue or yellow: ')
          if door=='yellow':
            print('Congratulations you found the treasure')
          else:
            print('game over')    
        else:
         print('Game Over')
    else:
     print('Game Over')
else:
    play=False
    print("Thank you for Playing")