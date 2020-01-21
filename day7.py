l=["cat","dog","cap"]
import random
def hangman():
    num=random.randint(0,2)
    word=l[num]
    wrong=0
    stages=["",
            "___________     ",
            "|               ",
            "|         |     ",
            "|         0     ",
            "|        /|L  ",
            "|         /|    ",
            "|                "
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("welcome to hangman")
    while wrong < len(stages)-1:
        print("\n")
        y=input("1文字を予測:")
        if y in rletters:
            c=rletters.index(y)
            board[c]=y
            rletters[c]="$"
        else:
            wrong+=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you win")
            print(" ".join(board))
            win=True
            break
        if not win:
            print("\n".join(stages[0:wrong+1]))
            print("you lose answer is {}.".format(word))

hangman()

