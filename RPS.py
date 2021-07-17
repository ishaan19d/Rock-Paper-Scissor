import random

print("Rock Paper Scissor")
print("---------------------------------------")
print("****************************")
print("*Source Code by Ishaan Das *")
print("****************************")
print("Welcome to this vintage game")
print("---------------------------------------")
print("For ROCK press R")
print("For PAPER press P")
print("For Scissor press S")
print("---------------------------------------")
rps_list=["Rock","Paper","Scissor"]
while(True):
    ai_move=random.choice(rps_list)
    rps=input("Enter your move: ")
    if ((ai_move=="Rock" and (rps=="R" or rps=="r")) or (ai_move=="Paper" and (rps=="P" or rps=="p")) or (ai_move=="Scissor" and (rps=="S" or rps=="s"))):
        print("Take this",ai_move,", Ohh no same, Let's play again!")
    elif ((ai_move=="Rock" and (rps=="P" or rps=="p")) or (ai_move=="Paper" and (rps=="S" or rps=="s")) or (ai_move=="Scissor" and (rps=="R" or rps=="r"))):
        print("Take this",ai_move,", Ohhhh Man,You Win!!")
    elif ((ai_move=="Rock" and (rps=="S" or rps=="s")) or (ai_move=="Paper" and (rps=="R" or rps=="r")) or (ai_move=="Scissor" and (rps=="P" or rps=="p"))):
        print("Take this",ai_move,", HaHa,You Lose....LoL")
    else:
        print("Enter a valid move")