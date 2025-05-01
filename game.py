import random


# def game():
#     print("Game begins")
#     score=random.randint(1,100)
#     print(f"Your Score {score}")
#     return score


# with open("game.txt","w") as f:
#     f.write(f"Score is {game()}")

# -----------------------------------------------------


def game():
    print("Game begins")
    score=random.randint(1,100)
    with open("highscore.txt") as f :
        highscore=f.read()
    print(f"your score {score}")

    if(score>int(highscore)):
       with open("highscore.txt","w") as f :
        f.write(f"{score}")


   
game()