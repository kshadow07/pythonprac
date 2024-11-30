
import random
import words 
import hangman_logo


print(hangman_logo.logo)
chosen_word=""
answer=[]
death_counter=0
end= False
chosen_word+=random.choice(words.word_list)
print(chosen_word)

for i in chosen_word:
  answer.append("_")

while not end:
  guess=input("Guess a letter: ").lower()
  if guess not in chosen_word:
    death_counter+=1
    print(hangman_logo.stages[death_counter])
    print(f'Wrong {guess} is not the letter')
  for i in range(len(chosen_word)):
    if chosen_word[i]==guess:
      answer[i]=guess
  if "_" not in answer:
    end=True
    print("You win")
  print(answer)
  if death_counter==6:
    end=True
    print("YOU lost")
    