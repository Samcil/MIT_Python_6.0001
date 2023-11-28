#%%
current_savings, portion_down_payment, r = 0.0, 0.25, 0.04


annual_salary = float(input("Enter your Starting Annual Salary: "))
portion_saved = float(
    input("Enter the portion of your Annual Salary you want to save as decimals: "))
total_cost = float(input("Enter the cost of your Dream Home: "))
monthly_salary = annual_salary/12

#%%
amt_down_payment = portion_down_payment * total_cost
number_of_months = 0
while (amt_down_payment - current_savings) >= 0:
    if number_of_months != 0:
        current_savings = (current_savings + portion_saved *
                           monthly_salary) * (1+r/12)
    else:
        current_savings = current_savings + portion_saved * monthly_salary
    number_of_months += 1

print(f"Number of months: {number_of_months}")

# %%
