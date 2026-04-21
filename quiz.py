import pgzrun
import random
WIDTH=800
HEIGHT=400
score=0
game_over=False
game_complete=False
questions=[]
def load_questions():
    file=open("question.txt","r")
    for i in file:
        qna=i.strip().split(",")
        q=qna[0]
        a=qna[-1]
        o=qna[1:5]
        questions.append((q,a,o))
load_questions()
temp=0
print(questions)
coordinates=[Rect((100,220),(200,60)),Rect((400,220),(200,60)),Rect((100,320),(200,60)),Rect((400,320),(200,60))]
def draw():
    screen.fill("Blue")
    screen.draw.text("Quiz Game",center=(300,50),fontsize=40,color="white")
    if game_over:
        screen.fill("red")
        screen.draw.text("Game Over\n score:{}/10".format(score),center=(300,200),fontsize=40,color="white")
    elif game_complete:
        screen.fill("yellow")
        screen.draw.text("Congratulations! You have won\n score:{}/10".format(score),center=(300,200),fontsize=40,color="white")
    else:
        q,a,o=questions[temp]
        screen.draw.text(q,center=(300,200),fontsize=30,color="white")
        for i,j in enumerate(coordinates):
            screen.draw.filled_rect(j,"light blue")
            screen.draw.text(o[i],center=j.center,color="white")
pgzrun.go()
            





        
