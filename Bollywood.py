import random
lv1=['sanju','golmaal','kgf',"ra one","dhamaal","baaghi","airlift","ghayal","fan","azhar","robot",'raabta']
lv2=['hera pheri','all the best',"heropanti","housefull","udta punjab","bank chor","tubelight"]
lv3=['anjaana anjaani','loveshhuda','half girlfriend','hindi medium']
score=0
heart=7
df=df1=df2=0
def game(lv,heart,score,lvadd):
    heart1=None
    a=""
    d=0
    mov=""
    joi=0
    lo=0
    jhk=[]
    while 1!=0:
        lem=0
        while 1!=0:
            b=random.randint(0,len(lv)-1)
            jhk.append(b)
            if b in jhk:
                break
        movie=lv[b]
        for kl in movie:
            if kl not in mov:
                lo+=1
            mov+=kl
            if kl.isalnum():
                lem+=1
        life=lem
        for i in movie:
            if i.isalnum():
                a+="_ "
            else:
                a+="  "
        print(a)
        while d!=lem:
            ac=input("Guess a word or 'quit' to quit the game: ")
            if ac!="quit":
                if ac!=movie:
                    l=0
                    for j in range(len(movie)):
                        if ac==movie[j]:
                            a=a[0:(2*j)]+ac+a[((2*j)+1):]
                            l+=1
                            d+=1
                    if l==0:
                        if (life-1)>0:
                            life-=1
                            print('You lost one life')
                        else:
                            if score-20<0:
                                score=0
                            else:
                                score-=20
                            print("You lost one heart and your score is deducted by 20")
                            print("Your score is:",score)
                            heart-=1
                            life = lem
                    else:
                        print("Good, it was a correct guess")
                        joi+=1
                        score+=lvadd
                
                    if heart!=0 and d!=lem:
                        print(a)
                    if heart==0:
                        print("Your hearts are zero!!")
                        print("GAME OVER!!")
                        break
                    else:
                        continue
                else:
                    score-=(joi*lvadd)
                    score+=lo*(lvadd+1)
                    d=lem
            else:
                heart1=0
                break
        print("Your score is:",score)
        if heart1==0:
            print("Thank You for playing :)")
        if d==lem:
            print("congratulations!!!")
            break
        else:
            break
    return (score,heart,heart1)

while 1!=0:
    if score<80:
        df+=1
        if df==1:
            print("Level 1")
        score,heart,heart1=game(lv1,heart,score,5)
        if heart==0:
            break
        if heart1==0:
            break
        print("Your hearts left are:",heart)
    elif score<200 and score>=80:
        df1+=1
        if df1==1:
            print("Level 2")
        score,heart,heart1=game(lv2,heart,score,7)
        if heart==0:
            break
        if heart1 == 0:
            break
        print("Your hearts left are:",heart)
    elif score<500 and score>=200:
        df2+=1
        if df2==1:
            print("Level 3")
        score,heart,heart1=game(lv3,heart,score,10)
        if heart==0:
            break
        if heart1==0:
            break
        print("Your hearts left are:",heart)    
    else:
        print("Congratulations!!")
        print("You have won the game!!!")
        break
