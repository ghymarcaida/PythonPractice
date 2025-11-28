name1 = input("What is your name first person? \n")
name2 = input("What is your name second person? \n")

combined_names = name1 + name2

def love_score (name1, name2):
    combined_names = name1 + name2
    lower_case_names = combined_names.lower()

    true_count = 0
    for letter in "true":
        true_count += lower_case_names.count(letter)

    love_count = 0
    for letter in "love":
        love_count += lower_case_names.count(letter)

    score = int(str(true_count) + str(love_count))
    print(f"Your love score is: {score}")