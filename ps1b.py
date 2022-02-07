## 6.0001 Pset 1: Part b
## Name: Brooke Pulling
## Time Spent: 30 minutes
## Collaborators: None

##########################################################################################
## Get user input for annual_salary, portion_saved, total_cost, semi_annual_raise below ##
##########################################################################################

annual_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
current_savings = 0 
months = 0 

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

#down payment is equal to 20% of total cost 
portion_down_payment = 0.2*(total_cost)

while current_savings <= portion_down_payment:
    months += 1
    if months % 6 == 0:
        annual_salary = (1 + semi_annual_raise)*(annual_salary)
    current_savings += (current_savings)*(0.04/12)
    current_savings += (portion_saved*annual_salary)/12
print('Mumber of months: ', months)
