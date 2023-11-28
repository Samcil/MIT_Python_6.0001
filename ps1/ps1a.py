#%%
# Getting user input
annual_salary = float(input("Enter your Starting Annual Salary: "))
portion_saved = float(input("Enter the portion of your Annual Salary you want to save each month as decimals: "))
total_cost = float(input("Enter the cost of your Dream Home: "))
#%%
# Initializing fixed variables
current_savings, portion_down_payment, annual_return, number_of_months = 0.0, 0.25, 0.04, 0

monthly_salary = annual_salary/12
monthly_rate = annual_return/12
amt_saving = portion_saved * monthly_salary
amt_down_payment = portion_down_payment * total_cost
while (amt_down_payment - current_savings) >= 0:
    current_savings = amt_saving + (current_savings) * (1 + monthly_rate)
    number_of_months += 1

print(f"Number of months: {number_of_months}")
# %%