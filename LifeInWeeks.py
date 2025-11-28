age = int(input("How old are you? "))
expected_age = 90 * 52

def life_in_weeks(age):
    print(f"You have {expected_age - (age * 52)} weeks left.")

life_in_weeks(age)