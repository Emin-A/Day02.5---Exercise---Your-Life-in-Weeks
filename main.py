age = input("What is your current age? ")

years = 90
# age = 90 end - 32 current = 58 years left
years_left = int(years) - int(age)
# months =  58 years left * 12 = 696 months left
months = round(years_left * 12)
# weeks =  696 months left * 52 = 36,192 weeks left
weeks = round(months * 52)
# days = 36,192 weeks left * 365 = 13,210,080 days left
days = round(weeks * 365)


print(f"You have {days} days, {weeks} weeks, and {months} months left!!!")