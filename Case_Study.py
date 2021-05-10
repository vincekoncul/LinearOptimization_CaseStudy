# -*- coding: utf-8 -*-
################################## Month 1 ##################################

#No servers are needed for this month due to lack of financial incentive or problem context

################################## Month 2 ##################################
from pulp import *

prob = LpProblem("CommuniCorp. Month 2", LpMinimize)

#Decision Variables - servers must be integers (cannot buy part of a server)
x1 = LpVariable('Standard Intel Pentium PC', lowBound = 0, cat = "Integer")
x2 = LpVariable('Enhanced Intel Pentium PC', lowBound = 0, cat = "Integer")
x3 = LpVariable('SGI Workstation',           lowBound = 0, cat = "Integer")
x4 = LpVariable('Sun Workstation',           lowBound = 0, cat = "Integer")

support_needed = 50 #50 or more sales employees must be able to access this month - 330 total employees

#Objective Function

# 10% discount on SGI, 25 % discount from Sun 
prob += 2500*x1 + 5000*x2 + (10000 - (10000 * .1)) * x3 + (25000 - (25000 *.25)) *x4

#Create big number
m=1000000

#Define our budget for month 1 and 2
budget = 9500

#Constraints
prob += x1 <= 1 #* m * y1 # does not make sense to purchase more than one standard pc
prob += x3 <= 1 # Cannot afford more than one SGI workstation this month due to budget
prob += x4 == 0 #We cannot afford a Sun workstation this month due to our budget
prob += 2500*x1 + 5000*x2 + (10000 - (10000 * .1)) * x3 + (25000 - (25000 *.25)) *x4 <= budget
prob += 30*x1 + 80 * x2 + 200 * x3 + 2000 * x4 >= support_needed

print(prob)

prob.solve()
print("status:" + LpStatus[prob.status]) #Tells if optimal or infeasible

#Loop through our model variables and display
for variable in prob.variables():
    print("{}* = {}".format(variable.name,variable.varValue))

#Slack and Shadow Price
for name, c in prob.constraints.items():
    print("\n", name, ":",c, ", Slack=", c.slack, ", Shadow Price=", c.pi)

#Reduced Cost
for v in prob.variables():
    print("\n", v.name, "=", v.varValue, ", Reduced Cost=", v.dj)

#Prints the value of the problem objective value     
print(value(prob.objective)) 

#Adds running total cost to total_cost variable
total_cost = value(prob.objective)


################################## Month 3 ##################################

from pulp import *

prob = LpProblem("CommuniCorp. Month 3", LpMinimize)

#Decision Variables - servers must be integers (cannot buy part of a server)
x1 = LpVariable('Standard Intel Pentium PC', lowBound = 0, cat = "Integer")
x2 = LpVariable('Enhanced Intel Pentium PC', lowBound = 0, cat = "Integer")
x3 = LpVariable('SGI Workstation',           lowBound = 0, cat = "Integer")
x4 = LpVariable('Sun Workstation',           lowBound = 0, cat = "Integer")
y1 = LpVariable('Standard vs Enhanced', lowBound =0, upBound = 1, cat = "Integer")
#y2 = LpVariable('Enhanced vs SGI', lowBound =0, upBound = 1, cat = "Integer")

#Employees to support
support_needed = 150 #Sales has 50 employees, manufacturing has 180 and requires one of the more powerful servers. 80 are currently covered already because of month 1

#Objective Function

# 10% discount on SGI, 25 % discount from Sun expired
prob += 2500*x1 + 5000*x2 + 10000 * x3 + 25000 *x4

#Create big number
m=1000000

#Constraints
#Our Budget has expired for the remainder of the months

prob += x2 == 2 * m * y1 # If x2 is equal to 2 we do not purchase because it is worse value than buying the SGI server
prob += 30*x1 + 80 * x2 + 200 * x3 + 2000 * x4 >= support_needed
prob += x2 + x3 + x3 >=1
print(prob)

prob.solve()
print("status:" + LpStatus[prob.status]) #Tells if optimal or infeasible

#Loop through our model variables and display
for variable in prob.variables():
    print("{}* = {}".format(variable.name,variable.varValue))

#Prints the value of the problem objective value     
print(value(prob.objective)) 

#Slack and Shadow Price
for name, c in prob.constraints.items():
    print("\n", name, ":",c, ", Slack=", c.slack, ", Shadow Price=", c.pi)

#Reduced Cost
for v in prob.variables():
    print("\n", v.name, "=", v.varValue, ", Reduced Cost=", v.dj)
    
total_cost += value(prob.objective)


################################## Month 4 ##################################
from pulp import *

prob = LpProblem("CommuniCorp. Month 4", LpMinimize)

#Decision Variables - servers must be integers (cannot buy part of a server)
x1 = LpVariable('Standard Intel Pentium PC', lowBound = 0, cat = "Integer")
x2 = LpVariable('Enhanced Intel Pentium PC', lowBound = 0, cat = "Integer")
x3 = LpVariable('SGI Workstation',           lowBound = 0, cat = "Integer")
x4 = LpVariable('Sun Workstation',           lowBound = 0, cat = "Integer")


support_needed = 0 #Sales has 50 employees, manufacturing has 180 and the warehouse has 30 employees. This totals 260 and we currently have 280 covered

#Employees each support
support_capacity ={'Standard Intel Pentium PC':30,
          'Enhanced Intel Pentium PC':80,
          'SGI Workstation':200,
          'Sun Workstation':2000
          }

#Objective Function

# 10% discount on SGI, 25 % discount from Sun 
prob += 2500*x1 + 5000*x2 + 10000 * x3 + 25000 *x4
budget = 9500

#Constraints
#prob += x1 + x2 + x3 + x4 <= budget #Overall budget for month 1 and 2
#prob += x1 + x2 +x3 +x4 >= employees
#prob += x2 >= 1 # We have already purchased an enhanced pentium
prob += 30*x1 + 80 * x2 + 200 * x3 + 2000 * x4 >= support_needed

print(prob)


prob.solve()
print("status:" + LpStatus[prob.status]) #Tells if optimal or infeasible

#Loop through our model variables and display
for variable in prob.variables():
    print("{}* = {}".format(variable.name,variable.varValue))

#Prints the value of the problem objective value     
print(value(prob.objective)) 

total_cost += value(prob.objective)

################################## Month 5 ##################################
from pulp import *

prob = LpProblem("CommuniCorp. Month 5", LpMinimize)

#Decision Variables - servers must be integers (cannot buy part of a server)
x1 = LpVariable('Standard Intel Pentium PC', lowBound = 0, cat = "Integer")
x2 = LpVariable('Enhanced Intel Pentium PC', lowBound = 0, cat = "Integer")
x3 = LpVariable('SGI Workstation',           lowBound = 0, cat = "Integer")
x4 = LpVariable('Sun Workstation',           lowBound = 0, cat = "Integer")


support_needed = 50 # Marketing has 70 employees, 20 of which can be covered from our current setup

#Objective Function
prob += 2500*x1 + 5000*x2 + 10000 * x3 + 25000 *x4

#Constraints
prob += 30*x1 + 80 * x2 + 200 * x3 + 2000 * x4 >= support_needed
prob += x1 <= 1
prob += x3 <= 1

print(prob)


prob.solve()
print("status:" + LpStatus[prob.status]) #Tells if optimal or infeasible

#Loop through our model variables and display
for variable in prob.variables():
    print("{}* = {}".format(variable.name,variable.varValue))

#Prints the value of the problem objective value     
print(value(prob.objective)) 

#Slack and Shadow Price
for name, c in prob.constraints.items():
    print("\n", name, ":",c, ", Slack=", c.slack, ", Shadow Price=", c.pi)

#Reduced Cost
for v in prob.variables():
    print("\n", v.name, "=", v.varValue, ", Reduced Cost=", v.dj)
    
total_cost += value(prob.objective)




################################## Q2 All Months ##################################

from pulp import *

prob = LpProblem("CommuniCorp. Part 2 - Entire Planning Period", LpMinimize)

#Decision Variables - servers must be integers (cannot buy part of a server)
x1 = LpVariable('Standard Intel Pentium PC', lowBound = 0, cat = "Integer")
x2 = LpVariable('Enhanced Intel Pentium PC', lowBound = 0, cat = "Integer")
x3 = LpVariable('SGI Workstation',           lowBound = 0, cat = "Integer")
x4 = LpVariable('Sun Workstation',           lowBound = 0, cat = "Integer")
x11 = LpVariable('Months 3-5 Standard Intel Pentium', lowBound = 0, cat = "Integer")
x22 = LpVariable('Months 3-5 Enhanced Intel Pentium ', lowBound = 0, cat = "Integer")
x33 = LpVariable('Months 3-5 SGI Workstation', lowBound = 0, cat = "Integer")
y1 =  LpVariable('Enhanced vs SGI', lowBound =0, upBound = 1, cat = "Integer")

#y1 = LpVariable('Standard vs Enhanced', lowBound = 0, cat = "Integer")
#Add y1 2 and 3 to pick one enhanced pc

#Objective Function
# 10% discount on SGI, 25 % discount from Sun 
prob += 2500*x1 + 5000*x2 + 9000 * x3 + 18750 * x4 + 2500*x11 + 5000*x22 + 10000 * x33, 'Obj'

m = 1000000

#Constraints
prob += 30 * x1 + 80 * x2 + 200 * x3 + 2000 * x4 + 30 * x11 + 80 * x22 + 200 * x33 >= 330
prob += 2500* x1 + 5000 * x2 +  9000 * x3 + 18750 *x4 <= 9500 # Used discounted values for SGI and Sun
prob += 30*x1 + 80 * x2 + 200 * x3 + 2000 * x4 >= 50
prob += x2 == 2 * m * y1 # If x2 is equal to 2 we do not purchase because it is worse value than buying the SGI server


print(prob)

prob.solve()
print("status:" + LpStatus[prob.status]) #Tells if optimal or infeasible

#Loop through our model variables and display
for variable in prob.variables():
    print("{}* = {}".format(variable.name,variable.varValue))

#Slack and Shadow Price
for name, c in prob.constraints.items():
    print("\n", name, ":",c, ", Slack=", c.slack, ", Shadow Price=", c.pi)

#Reduced Cost
for v in prob.variables():
    print("\n", v.name, "=", v.varValue, ", Reduced Cost=", v.dj)
    
#Prints the value of the problem objective value     
print(value(prob.objective)) 

#Slack and Shadow Price
for name, c in prob.constraints.items():
    print("\n", name, ":",c, ", Slack=", c.slack, ", Shadow Price=", c.pi)

#Reduced Cost
for v in prob.variables():
    print("\n", v.name, "=", v.varValue, ", Reduced Cost=", v.dj)
    
total_cost = value(prob.objective)


#The budget for the first two months is 9500 dollars. With the discount Emily's best option is to buy one SGI workstation. This will support
# up to 200 employees which is enough for the first month - this also satisfies manufacturings requirement of needed an enhanced server.

