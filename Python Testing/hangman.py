import random

words= ['cooperate', 'produce', 'arm', 'qualified', 'script', 'battle', 'master']

ran_choice=random.choice(words)

display_word=['_' for _ in ran_choice]

attempts=8

print("Let's play hangman")
print("Here's your word: \n")

while attempts>0:
    print(" ".join(display_word))
    print()
    guess= input("Enter a letter: ").lower()
    attempts-=1
    
    if guess in ran_choice:
        
        for index, letter in enumerate(ran_choice):
            
            if guess == letter:
                display_word[index]= guess
                
            else:
                continue
            
        print("Congrats that letter is there")
    
    else:
        print("That letter ain't there loser")
    
    if "_" not in display_word and attempts!=0:
        break

    else:
        continue


  
  
  
  

if "_" in display_word and attempts==0:
    print()
    print(f'Game over! You used up your attempts, the word was {" ".join(display_word)}')

else:
  print()
  print(" ".join(display_word))
  print("Congrats you win!")
  



    
    
