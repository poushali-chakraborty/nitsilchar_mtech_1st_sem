# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 22:52:13 2022

@author: Joe
"""

from sympy import symbols, Eq, solve



''' Input coefficients of objective funtion and constraints as matrix '''

objective=[2,1] #[coeff of x, coeff of y]
constraints=[[1,1,3,1],  #[coeff of x ,coeff of y ,constant, -1 for > inequality]     
       [1,2,5,1],
       [1,0,2,1],
       [1,0,0,-1],
       [0,1,0,-1]]

print("Objective Function: ", objective[0],"x +",objective[1],"y")
print("subject to:")
for i in constraints:
    if i[3]==1:
        sym='<='
    else:
        sym='>='
    print(i[0],"x +",i[1],"y",sym, i[2])



''' Convert constraints to equation format to solve using sympy library '''
x, y = symbols('x,y') #declare variables for the equations
eq=[ Eq((i[0]*x+i[1]*y),i[2]) for i in constraints] #list to store eqn 


###for i in constraints:
     ####eq.append(Eq((i[0]*x+i[1]*y),i[2])) #put equation format according to sympy library
s=[]
def solveFunc(i,j):
    global s
    ss=solve((eq[i],eq[j]),(x,y))     #solves linear eqn i and j and returns solution
    print("solving",i+1,"and",j+1,"sol=",ss)
    if ss!=[]:  #ignore empty list(no solution)
        s=list(ss.values()) #convert solution to list
    return [float(k) for k in s]
     
sols=[solveFunc(i,j) for i in range(len(constraints)) for j in range(i,len(constraints)) if i!=j ] #list to store the solutions
'''
sols=[]
#for loop to find intersection of all eqn in eq[]
for i in range(len(constraints)):
    for j in range(i,len(constraints)):
        if i!=j:
            ss=solve((eq[i],eq[j]),(x,y))     #solves linear eqn i and j and returns solution
            print("solving",i+1,"and",j+1,"sol=",ss)
            if ss!=[]:  #ignore empty list(no solution)
                s=list(ss.values()) #convert solution to list
            s=[float(k) for k in s]
            sols.append(s)
'''
#print("sols")


''' From list of solutions filter out the feasible solutions'''
#print(sols)
feasibleSols=[] #list to store all feasible solution



#for loop tp test each solution with each constraints 
for i in sols:
    flag=1 #1 inicates feasible 0 indicate non-feasible
    #######print("for point: (",i[0],",",i[1],")")
    #try:
    for j in constraints:
        
        if j[3]==1:
            sym='<='
        else:
            sym='>='
        #######print(j[0],"x +",j[1],"y",sym, j[2], end=" ")
        if j[3]*(j[0]*i[0]+j[1]*i[1])<=j[3]*j[2]:
            flag&=1
            ######print(" True")
        else:
            flag&=0
            #######print(" False")
    if flag==1:
        feasibleSols.append(i)
        ######print("feasilble")
    ####print()
     
####print()
print("Feasible list:")
print(feasibleSols) 


''' calculate objective function for all feasible solutions'''

for i in range(len(feasibleSols)):
    z= objective[0] *feasibleSols[i][0]+ objective[1] *feasibleSols[i][1] #calculate z for i and add to list i
    feasibleSols[i].append(z)

feasibleSols.sort(key = lambda x: x[2])  #sort feasible solutions based on z value
print("Minimum point:", feasibleSols[0][0:2])
print('Value:', feasibleSols[0][2])

m=len(feasibleSols)-1
print("Maximum point:", feasibleSols[m][0:2])
print('Value:', feasibleSols[m][2])