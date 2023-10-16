#calculate interest

ending_balance = 0
year = 0
accumulated = 0

original_amount = float(input("Enter principle amount: $"))
print("")
interest_rate = float(input("Enter the interest rate (decimals number): "))
print("")

for i in range(0,5):
    annual_interest = original_amount * interest_rate
    ending_balance = original_amount + annual_interest
    year += 1

    print(year , format(original_amount , ".2f") , format(ending_balance , ".2f"))
    original_amount = ending_balance
    accumulated += annual_interest

print("")
print("Total interest earned: $" , format(accumulated , ".2f"))