def game():
    return 25
score=game()
with open("score.txt","r") as f:
    # hiscore=int(f.read())
     hiscore=f.read()
if hiscore == '':
    with open("score.txt","w") as f:
        f.write(str(score))

elif int(hiscore)<score:
    with open("score.txt","w") as f:
        f.write(str(score))
