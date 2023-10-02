# CD's

principle = float(input("Enter the principle amount of the CD: "))
print("")
year = int(input("Enter the year of maturity: "))
print("")

interest_rate = 0

if principle >= 100000 and year == 5:
  interest_rate = 6
elif principle > 50000 and year == 10:
  interest_rate = 5
elif principle > 50000 and year == 5:
  interest_rate = 4
else:
  interest_rate = 2

interest_amount = interest_rate * 0.01
first_year = principle * interest_amount

print("The principle amount is: $" , principle , ".With a interest rate \
of " , interest_rate , "% the first year would \
be: $" , first_year + principle, "includind $" , first_year , "of interest.")