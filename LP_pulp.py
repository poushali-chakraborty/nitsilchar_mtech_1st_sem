# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 17:35:05 2022

Linear programming using PULP


@author: JoeP
"""
# import the library pulp as p
import pulp as p
  
# Create a LP Minimization problem
Lp_prob = p.LpProblem('Problem', p.LpMinimize) 

#for maximization,
Lp_prob = p.LpProblem('Problem', p.LpMinimize) 

  
# Create problem Variables 
x = p.LpVariable("x", lowBound = 0)   # Create a variable x >= 0
y = p.LpVariable("y", lowBound = 0)   # Create a variable y >= 0
  
# Objective Function
Lp_prob += 2 * x + 1 * y   
  
# Constraints:
Lp_prob += 1 * x + 1 * y <= 3
Lp_prob += 1 * x + 2 * y <= 5
Lp_prob += x <= 2

  
# Display the problem
print(Lp_prob)
  
status = Lp_prob.solve()   # Solver
print(p.LpStatus[status])   # The solution status
  
# Printing the final solution
print(p.value(x), p.value(y), p.value(Lp_prob.objective)) 