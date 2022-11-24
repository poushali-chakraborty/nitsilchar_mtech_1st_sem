probabilities={
"no_of_gabby_s" : 0.0,
"no_of_gabby_p" : 0.0,
"no_of_quiet_s" : 0.0,
"no_of_quiet_p" : 0.0,
"no_of_baked_s" : 0.0,
"no_of_baked_p" : 0.0,
"no_of_fried_s" : 0.0,
"no_of_fried_p" : 0.0,
"no_of_roasted_s" : 0.0,
"no_of_roasted_p" : 0.0,
"no_of_clogs_s" : 0.0,
"no_of_clogs_p" : 0.0,
"no_of_sandal_p" : 0.0,
"no_of_sandal_s" : 0.0,
"no_of_student" : 0.0,
"no_of_profess" : 0.0
}
class Dataset:
    
    def __init__(self,h,e,f,p):
        self.habit = h
        self.eats=e
        self.footwear=f
        self.profession=p

        if self.profession == "student":
            if self.habit == "gabby":
                probabilities["no_of_gabby_s"] += 1
            else: probabilities["no_of_quiet_s"] += 1
            if self.eats == "baked":
                probabilities["no_of_baked_s"] += 1
            elif self.eats == "roasted":
                probabilities["no_of_roasted_s"] +=1
            else: probabilities["no_of_fried_s"] +=1
            if self.footwear == "clogs":
                probabilities["no_of_clogs_s"] += 1
            else: probabilities["no_of_sandal_s"] +=1
            probabilities["no_of_student"] +=1
        else:
            if self.habit == "gabby":
                probabilities["no_of_gabby_p"] += 1
            else: probabilities["no_of_quiet_p"] +=1
            if self.eats == "baked":
                probabilities["no_of_baked_p"] += 1
            elif self.eats == "roasted":
                probabilities["no_of_roasted_p"] +=1
            else: probabilities["no_of_fried_p"] +=1
            if self.footwear == "clogs":
                probabilities["no_of_clogs_p"] += 1
            else: probabilities["no_of_sandal_p"] +=1
            probabilities["no_of_profess"] +=1  

            
def MLE(n,habit,eats,footwear):
    p_habit_p = 0.0
    p_habit_s = 0.0
    p_eats_p = 0.0
    p_eats_s = 0.0
    p_footwear_p = 0.0
    p_footwear_s = 0.0

    Prior_p = probabilities["no_of_profess"] / n
    Prior_s = probabilities["no_of_student"] / n

    print("Calculation of probabilities for MLE:")

    if habit == "gabby":
        p_habit_p = probabilities["no_of_gabby_p"] /probabilities["no_of_profess"]
        p_habit_s = probabilities["no_of_gabby_s"] / probabilities["no_of_student"]
        print("Probablity of habit = gabby given class is professor :", p_habit_p)
        print("Probablity of habit = gabby given class is student :", p_habit_s)
    else:
        p_habit_p = probabilities["no_of_quiet_p"] / probabilities["no_of_profess"]
        p_habit_s = probabilities["no_of_quiet_s"] /probabilities["no_of_student"]
        print("Probablity of habit = quiet given class is professor :", p_habit_p)
        print("Probablity of habit = quiet given class is student :", p_habit_s)
    
    if eats == "roasted":
        p_eats_p =probabilities["no_of_roasted_p"] /probabilities["no_of_profess"]
        p_eats_s =probabilities["no_of_roasted_s"] / probabilities["no_of_student"]
        print("Probablity of eats = roasted given class is professor :", p_eats_p)
        print("Probablity of eats = roasted given class is student :", p_eats_s)

    elif eats == "baked":
        p_eats_p = probabilities["no_of_baked_p"] /probabilities["no_of_profess"]
        p_eats_s = probabilities["no_of_baked_s"] /probabilities["no_of_student"]
        print("Probablity of eats = baked given class is professor :", p_eats_p)
        print("Probablity of eats = baked given class is student :", p_eats_s)

    else:
        p_eats_p = probabilities["no_of_fried_p"] / probabilities["no_of_profess"]
        p_eats_s = probabilities["no_of_fried_s"] /probabilities["no_of_student"]
        print("Probablity of eats = fried given class is professor :", p_eats_p)
        print("Probablity of eats = fried given class is student :", p_eats_s)

    if footwear == "clogs":
        p_footwear_p = probabilities["no_of_clogs_p"] /probabilities["no_of_profess"]
        p_footwear_s = probabilities["no_of_clogs_s"] /probabilities["no_of_student"]
        print("Probablity of footwear = clogs given class is professor :", p_footwear_p)
        print("Probablity of footwear = clogs given class is student :", p_footwear_s)
    else:
        p_footwear_p =probabilities["no_of_sandal_p"] /probabilities["no_of_profess"]  
        p_footwear_s = probabilities["no_of_sandal_s"] / probabilities["no_of_student"]
        print("Probablity of footwear = sandals given class is professor :", p_footwear_p)
        print("Probablity of footwear = sandals given class is student :", p_footwear_s)

    MLE_P = Prior_p * p_habit_p * p_eats_p * p_footwear_p
    MLE_S = Prior_s * p_habit_s * p_eats_s * p_footwear_s

    print("Maximum Likelihood Estimation, Professor Class:", MLE_P)
    print("Maximum Likelihood Estimation, Student Class:", MLE_S)

    if MLE_P != 0 or MLE_S != 0:
        if MLE_P > MLE_S:
            print("Pattern belongs to Professor Class.")
        else: print("Pattern belongs to Student Class.")
    else: print("Pattern cannot be classified using Maximum Likelihood Estimation.")

def BE(n,habit,eats,footwear):
    p_habit_p = 0.0
    p_habit_s = 0.0
    p_eats_p = 0.0
    p_eats_s = 0.0
    p_footwear_p = 0.0
    p_footwear_s = 0.0

    Prior_p = (probabilities["no_of_profess"] + 1) / (n + 2)
    Prior_s = (probabilities["no_of_student"] + 1 ) / (n + 2)

    print("Calculation of probabilities for Bayesian Estimation:")

    if habit == "gabby":
        p_habit_p = (probabilities["no_of_gabby_p"] +1) / (probabilities["no_of_profess"] + 2)
        p_habit_s = (probabilities["no_of_gabby_s"] +1) / (probabilities["no_of_student"] + 2)
        print("Probablity of habit = gabby given class is professor :", p_habit_p)
        print("Probablity of habit = gabby given class is student :", p_habit_s)
    else:
        p_habit_p = (probabilities["no_of_quiet_p"] +1) / (probabilities["no_of_profess"] + 2)
        p_habit_s = (probabilities["no_of_quiet_s"] +1) / (probabilities["no_of_student"] + 2)
        print("Probablity of habit = quiet given class is professor :", p_habit_p)
        print("Probablity of habit = quiet given class is student :", p_habit_s)
    
    if eats == "roasted":
        p_eats_p = (probabilities["no_of_roasted_p"]+1) / (probabilities["no_of_profess"] + 3)
        p_eats_s = (probabilities["no_of_roasted_s"] +1) / (probabilities["no_of_student"] + 3)
        print("Probablity of eats = roasted given class is professor :", p_eats_p)
        print("Probablity of eats = roasted given class is student :", p_eats_s)

    elif eats == "baked":
        p_eats_p = (probabilities["no_of_baked_p"] +1) / (probabilities["no_of_profess"] + 3)
        p_eats_s = (probabilities["no_of_baked_s"] +1) / (probabilities["no_of_student"] + 3)
        print("Probablity of eats = baked given class is professor :", p_eats_p)
        print("Probablity of eats = baked given class is student :", p_eats_s)

    else:
        p_eats_p = (probabilities["no_of_fried_p"] +1) / (probabilities["no_of_profess"] + 3)
        p_eats_s = (probabilities["no_of_fried_s"] +1) / (probabilities["no_of_student"] + 3)
        print("Probablity of eats = fried given class is professor :", p_eats_p)
        print("Probablity of eats = fried given class is student :", p_eats_s)

    if footwear == "clogs":
        p_footwear_p = (probabilities["no_of_clogs_p"] +1) / (probabilities["no_of_profess"] + 2)
        p_footwear_s = (probabilities["no_of_clogs_s"] +1) / (probabilities["no_of_student"] + 2)
        print("Probablity of footwear = clogs given class is professor :", p_footwear_p)
        print("Probablity of footwear = clogs given class is student :", p_footwear_s)
    else:
        p_footwear_p = (probabilities["no_of_sandal_p"] + 1) / (probabilities["no_of_profess"] + 2)
        p_footwear_s = (probabilities["no_of_sandal_s"]+ 1) / (probabilities["no_of_student"] + 2)
        print("Probablity of footwear = sandals given class is professor :", p_footwear_p)
        print("Probablity of footwear = sandals given class is student :", p_footwear_s)

    BE_P = Prior_p * p_habit_p * p_eats_p * p_footwear_p
    BE_S = Prior_s * p_habit_s * p_eats_s * p_footwear_s

    print("Bayesian Estimation, Professor Class:", BE_P)
    print("Bayesian Estimation, Student Class:", BE_S)

    if BE_P > BE_S:
            print("Pattern belongs to Professor Class.")
    else: print("Pattern belongs to Student Class.")

n = 8

datasetList=[]
datasetList.append(Dataset("gabby", "baked", "clogs", "student"))
datasetList.append(Dataset("gabby", "roasted", "sandals", "professor"))
datasetList.append( Dataset("gabby", "baked", "sandals", "student"))
datasetList.append(Dataset("quiet", "fried", "sandals", "professor"))
datasetList.append(Dataset("gabby", "fried", "clogs", "student"))
datasetList.append(Dataset("quiet", "baked", "sandals", "student"))
datasetList.append( Dataset("gabby", "fried", "sandals", "professor"))
datasetList.append( Dataset("quiet", "fried", "clogs", "student"))
print("pattern 1")
MLE(8,"gabby","roasted","clogs")
BE(8,"gabby","roasted","clogs")
print("pattern 2")
MLE(8,"quiet","baked","clogs")
BE(8,"quiet","baked","clogs")
print("pattern 3")
MLE(8,"quiet","roasted","sandals")
BE(8,"quiet","roasted","sandals")



