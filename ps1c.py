## 6.0001 Pset 1: Part c
## Name: Brooke Pulling
## Time Spent: 1.5 hours
## Collaborators: None

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
months = 36
down_payment = 160000
error = 100
steps = 0
r_low = 0
r_high = 1
guess = (r_low + r_high)/2 #corresponds to r
current_savings = initial_deposit*(1+(guess/12))**months

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

#when you already have enough money 
if initial_deposit > down_payment:
    guess = 0
    print(guess)
#when you will never have enough money (the rate of return is 1)
elif down_payment > initial_deposit*(1+(1/12))**months:
    guess = None
#if neither of the edge cases are true, then there has to be a value of r such that we can make 160,000
else: 
    #while my current savings is not in the range that it needs to be in 
    while abs(current_savings - down_payment) >= error:
        #count the number of times our range for r is halved
        steps += 1
        #check to see if I have too much money or too little
        #for the case when I have too much money
        if current_savings > down_payment:
            #update r_high to be the previous guees (ie. changing the bounds by cutting the range of r in half)
            r_high = guess
            #recalculate guess using the updated value of r high 
            guess = (r_low + r_high)/2
            #recalculate current savings 
            current_savings = initial_deposit*(1+(guess/12))**months
        #we use an else here because every time i update r it needs to check the condition of the while loop
        else:
            #update r_low to be the previous guess (ie. changing the bounds by cutting the range of r in half)
            r_low = guess
            #recalculate guess using the updated value of r low 
            guess = (r_low + r_high)/2
            #recalculate current savings 
            current_savings = initial_deposit*(1+(guess/12))**months
r = guess
print("Best savings rate: ", guess)
print('Steps in bisection search: ', steps)