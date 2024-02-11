print("Welcome to Personalized Birthday Wishes Maker 3000")
print("Please enter name of the birthday boy")
birthday_boy = input()
print("Please enter his year of birth")
birth_year = int(input())
print("Please enter short personalized message")
personal_message = input()
print("How would you like to sign?")
sender = input()


import datetime
today = datetime.date.today()
actual_year = today.year

age = (actual_year-birth_year)

print(f"""
{birthday_boy}, let's celebrate your {age} years of awesomeness!
Wishing you a day filled with joy and laughter as you turn {age}!

{personal_message}

With love and best wishes,
{sender}

""")
