#####written by Poushali Chakraborty @7:47pm 5 Oct 2022 
# this program can be used to classify a given pattern based on the training dataset's attribute values.
# it uses Bayes’ classifier with Maximum Likelihood Estimation

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
    "pattern":"t8",
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

def probability(atribute,valuei,cls,tvalue): #calculate the probability of the class for a given atrribute value
    ck=0
    ckij=0
    an=[] 
    for d in dataset:
        if d[atribute] not in an: # this list is used to calculate the no of distinct values for a given atrribute
            an.append(d[atribute])
            
        if d["class"]==cls:
            ck+=1
            if d[atribute]==valuei:
                ckij+=1
    if not tvalue:
        return maximumLikelyHood(ckij,ck)
    else:
        return nb(ckij,ck,len(an))
    
def probabilityClass(cls,tvalue): #caculates the probability for the given class
    ck=0 #no of prof/students
    for d in dataset:
        if d["class"]==cls:
            ck+=1
    if not tvalue:
        return maximumLikelyHood(ck,len(dataset))
    else:
        return nb(ck,len(dataset),2)
    




def classifier(given_pattern): #classifies the given data as professor or student
    print("maximum likelyhood")
    print("professor")
    prof=probabilityClass("professor",False)#maximumLikelyHood
    print("student")
    stud=probabilityClass("student",False)#maximumLikelyHood
    for key,val in given_pattern.items(): #take each row of key, value pair from given
        print(key,val)
        print("professor")
        prof*=probability(key,val,"professor",False)#maximumLikelyHood
        print("student")
        stud*=probability(key,val,"student",False)#maximumLikelyHood
    print("probability>> professor= ",prof," student= ",stud)
    if(prof==0.0 or stud==0.0):
       print("naive bayes")
       print("professor")
       prof=probabilityClass("professor",True)#naive bayes
       print("student")
       stud=probabilityClass("student",True)#naive bayes
       for key,val in given_pattern.items():
            print(key,val)
            print("professor")
            prof*=probability(key,val,"professor",True)#naive bayes
            print("student")
            stud*=probability(key,val,"student",True) #naive bayes
    print("probability>> professor= ",prof," student= ",stud)
    print("class for the given pattern: ",given_pattern," >>")
    if(prof>stud):
        print("professor")
    else:
        print("student")

    return

given_pattern={
    "habit":"gabby",
    "eats":"roasted",
    "footware":"clogs"
}
classifier(given_pattern)


