'''
Lets build Rock paper scissor game that we have played on our childhood 
basic idea:
1 = rock
0 = paper
-1 = scissor
computer makes a choice (rock paper scissor) and 
you make a choice (rock paper scissor)

rock wins scissor and looses paper
paper wins rock and looses scissor
scissor wins paper and looses rock

'''
import random
computer_choice = random.choice([-1,1,0])
your_choice = int(input("Lets Play the game:\n\n1 for rock\n0 for paper\n-1 for scissor\nEnter your choice: "))
l = [-1,0,1]

game = {
    1:"rock",
    0:"paper",
    -1:"scissor"
}

print(f"\nYour choice = {game[your_choice]}\nComputer choice = {game[computer_choice]}\n")


def play(a,b): #a = your_choice, b = computer_choice
    if((a==1 and b==-1) or (a==0 and b==1) or (a==-1 and b==0)):
        print("Congrats!! You win\n")
    elif(a==b):
        print("Its draw\n")
    else:
        print("Oops! You Lose\n")
    
if(your_choice in l):
    play(your_choice,computer_choice)
    
else:
    print("Enter correct choice..\n")

