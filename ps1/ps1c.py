#%%
# Getting user input
annual_salary = float(input("Enter your Starting Annual Salary: "))
#%%
# Initializing fixed variables
current_savings, portion_down_payment, annual_return, number_of_months, semi_annual_raise = 0.0, 0.25, 0.04, 3*12, 0.07
portion_saved, total_cost, months_needed_ = 0, 1_000_000, 36
monthly_salary = annual_salary / 12
monthly_rate = annual_return / 12
amt_saving = portion_saved * monthly_salary
amt_down_payment = portion_down_payment * total_cost
error = 100 / amt_down_payment

error_value, high, low, num_guess = 100.0, 1, 0, 0
guess = (high + low) / 2

while abs(amt_down_payment - current_savings) > error_value:
    amt_saving = guess * monthly_salary
    current_savings = 0
    for _ in range(number_of_months):
        if _ % 6 == 0 and _ > 0:
            amt_saving *= (1 + semi_annual_raise) 
        current_savings = amt_saving + (current_savings) * (1 + monthly_rate)
        if current_savings < amt_down_payment:  
            low = guess
        else:
            high = guess
        guess = (high + low) / 2
        num_guess += 1
    if num_guess > 30:
        print("It is not possible to pay the down payment in three years")
        break
    else:
        print(f"Best savings rate: {round(guess,4)}\nSteps in bisection search: {num_guess}")
# %%