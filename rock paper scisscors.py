input1= input("player 1 enter Rock, Paper or Scissor:")
input2= input("player 2 enter Rock, paper or Scissor:")

if input1=='Rock' and input2=='Paper':
    print ("Player 2 wins")
elif input1=='Rock' and input2=='Scissors':
    print ("Player 1 wins")
elif input1=='Paper' and input2=='Rock':
    print ("Player 1 wins")
elif input1=='Paper' and input2=='Scissors':
    print ("Player 2 wins")
elif input1=='Scissors' and input2=='Rock':
    print("Player 2 wins")
elif input2=='Scissors'and input2=='Paper':
    print("Player 1 wins")
else:
    print("oops!! No one wins, Play again")






