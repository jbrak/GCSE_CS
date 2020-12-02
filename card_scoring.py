def score(t1,t2):
    score1 = 0
    score2 = 0
    if t1[0] == "red" and t2[0] == "black":
        score1 += 1
    elif t2[0] == "red" and t1[0] == "black":
        score2 += 1
    elif t1[0] == "yellow" and t2[0] == "red":
        score1 += 1
    elif t2[0] == "yellow" and t1[0] == "red":
        score2 += 1
    elif t1[0] == "yellow" and t2[0] == "black":
        score2 += 1
    elif t2[0] == "yellow" and t1[0] == "red":
        score1 += 1
    else:
        if t2[1] > t1[1]:
            score2 += 1
        elif t1[1] > t2[1]:
            score1 += 1
        else:
            score1 += 1
            score2 += 1
    return score1,score2

print(score(("yellow",10), ("black",10)))
