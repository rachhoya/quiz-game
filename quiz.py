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
coordinates=[Rect((170,220),(200,60)),Rect((425,220),(200,60)),Rect((170,320),(200,60)),Rect((425,320),(200,60))]
def draw():
    screen.fill("royal blue")
    screen.draw.text("Quiz Game",center=(400,50),fontsize=40,color="white")
    if game_over:
        screen.fill("red")
        screen.draw.text("Game Over\n score:{}/10".format(score),center=(400,200),fontsize=40,color="white")
    elif game_complete:
        screen.fill("yellow")
        screen.draw.text("Congratulations! You have won\n score:{}/10".format(score),center=(400,200),fontsize=40,color="black")
    else:
        q,a,o=questions[temp]
        random.shuffle(o)
        screen.draw.text(q,center=(400,150),fontsize=30,color="white")
        for i,j in enumerate(coordinates):
            screen.draw.filled_rect(j,"blue")
            screen.draw.text(o[i],center=j.center,color="white")
def next():
    global temp,game_over,game_complete
    temp=temp+1
    if temp>=len(questions):
        game_complete=True
def on_mouse_down(pos):
    global score,game_over
    q,a,o=questions[temp]
    for i,j in enumerate(coordinates):
        if j.collidepoint(pos):
            if o[i]==a:
                score=score+1
            else:
                game_over=True
            next()

pgzrun.go()





        
