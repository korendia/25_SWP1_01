#Inhwan Bae,Kookmin University,2025, May,4

def count_score():
    count=int(input())
    all_score=list(map(int,input().split()))
    score=[0,0,0,0,0]
    for i in range(count):
        if all_score[i]>=90:
            score[0]+=1
        elif all_score[i] >= 80:
            score[1]+=1
        elif all_score[i] >= 70:
            score[2]+=1
        elif all_score[i] >= 60:
            score[3]+=1
        else:
            score[4]+=1
    score=list(map(str,score))
    print(' '.join(score))

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        count_score()