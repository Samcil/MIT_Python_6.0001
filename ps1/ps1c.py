#%%
# Getting user input
annual_salary = float(input("Enter your Starting Annual Salary: "))
#%%
# Initializing fixed variables
current_savings, portion_down_payment, annual_return, number_of_months, semi_annual_raise = 0.0, 0.25, 0.04, 0, 0.07
portion_saved, total_cost, months_needed_ = 0, 1_000_000, 36
monthly_salary = annual_salary / 12
monthly_rate = annual_return / 12
amt_saving = portion_saved * monthly_salary
amt_down_payment = portion_down_payment * total_cost

guess, error, high, low = 0.1, 100, 0, 10_000
while (amt_down_payment - current_savings) >= 0 and guess < portion_down_payment:
    if number_of_months > 0 and number_of_months % 6 == 0:
        amt_saving *= (1 + semi_annual_raise) 
    current_savings = amt_saving + (current_savings) * (1 + monthly_rate)
    number_of_months += 1

print(f"Number of months: {number_of_months}")
# %%