dataset=[
    {
    "pattern":"t1",
    "habit":"gabby",
    "eats":"baked",
    "footware":"clogs",
    "class":"student"
    },
    {
    "pattern":"t2",
    "habit":"gabby",
    "eats":"roasted",
    "footware":"sandle",
    "class":"professor"
    },
    {
    "pattern":"t3",
    "habit":"gabby",
    "eats":"baked",
    "footware":"sandle",
    "class":"student"
    },
    {
    "pattern":"t4",
    "habit":"quite",
    "eats":"fried",
    "footware":"sandle",
    "class":"professor"
    },
    {
    "pattern":"t5",
    "habit":"gabby",
    "eats":"fried",
    "footware":"clogs",
    "class":"student"
    },
    {
    "pattern":"t6",
    "habit":"quite",
    "eats":"baked",
    "footware":"sandle",
    "class":"student"
    },
    {
    "pattern":"t7",
    "habit":"gabby",
    "eats":"fried",
    "footware":"sandle",
    "class":"professor"
    },
    {
    "pattern":"t4",
    "habit":"quite",
    "eats":"fried",
    "footware":"clogs",
    "class":"student"
    }

]

def maximumLikelyHood(ckij,ck):
    print("ml: "+str(ckij)+"/"+str(ck))
    return float(ckij/ck)

def nb(ckij,ck,i):
    print("nb: "+str(ckij+1)+"/"+str(i+ck))
    return((float(ckij+1)/(i+ck)))
def probability(a,i,c):
    ck=0
    ckij=0
    iin=0
    an=[]
    for d in dataset:
        if d[a] not in an:
            an.append(d[a])
            
        if d["class"]==c and d[a]:
            ck+=1
            if d[a]==i:
                ckij+=1
    return [maximumLikelyHood(ckij,ck),nb(ckij,ck,len(an))]

def probClass(c):
    ck=0
    ckij=0
    for d in dataset:
        if d["class"]==c:
            ckij+=1
        ck+=1
    return [maximumLikelyHood(ckij,ck),nb(ckij,ck,2)]




def classifier(given):
    print("maximum likelyhood")
    print("professor")
    prof=probClass("professor")[0]
    print("student")
    stud=probClass("student")[0]
    for key,val in given.items():
        print(key,val)
        print("professor")
        prof*=probability(key,val,"professor")[0]
        print("student")
        stud*=probability(key,val,"student")[0]
    print("probability>> professor= ",prof," student= ",stud)
    if(prof==0.0 or stud==0.0):
       print("naive bayes")
       print("professor")
       prof=probClass("professor")[1]
       print("student")
       stud=probClass("student")[1]
       for key,val in given.items():
            print(key,val)
            print("professor")
            prof*=probability(key,val,"professor")[1]
            print("student")
            stud*=probability(key,val,"student")[1] 
    print("probability>> professor= ",prof," student= ",stud)
    if(prof>stud):
        print("professor")
    else:
        print("student")

    return
'''
probability("habit","gabby","professor")
probability("habit","quite","professor")
probability("eats","baked","professor")
probability("eats","fried","professor")
probability("eats","rosted","professor")
probability("footware","clog","professor")
probability("footware","sandle","professor")
'''
given={
    "habit":"gabby",
    "eats":"roasted",
    "footware":"clogs"
}
classifier(given)


