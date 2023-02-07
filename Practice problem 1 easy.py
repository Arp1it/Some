def years(age, current_year):
    if age < 0:
        return "You are not yet born"

    if age > current_year:
        return "You are not yet born"

    else:
        if age > 999:
            k = int(input("Please enter when you will turn: "))
            if k > 999:
                if k >= current_year:
                    while age != k:
                        age += 1
                        g += 1

                    return(f"In {age} your age will {g}")

                if k < current_year:
                    g = int(input("Please enter current age: "))
                    while current_year != k:
                        current_year -= 1
                        g -= 1

                    return(f"In {k} your age was {g}")
                    
            if k <= 199:
                if k > age:
                    while g != k:
                        age += 1
                        g += 1

                    return(f"If your age will {g} then the year will be {age}")

                if k < age:
                    while g != k:
                        age -= 1
                        g -= 1

                    return(f"If your age was {g} then the year was {age}")

                if k < 0.1:
                    return "Your not born on this time"



        if age <= 199:
            p = int(input("Please enter when you will turn: "))
            if p > 999:
                if p >= current_year:
                    while current_year != p:
                        age += 1
                        current_year += 1

                    return f"In {current_year} your age will be {age}"

                if p < current_year:
                    while current_year != p:
                        age -= 1
                        current_year -= 1

                    return f"In {current_year} your age was {age}"

            if p <= 199:
                if p > age:
                    while age != p:
                        age += 1
                        current_year += 1

                    return(f"If your age will {age} then the year will be {current_year}")

                if p < age:
                    while age != p:
                        age -= 1
                        current_year -= 1

                    return(f"If your age was {age} then the year was {current_year}")

            if p < 0.1:
                return "Your not born on this time"



        if age > 199 and age < 999:
            return "You seem to be the oldest person alive"

try:
    year = int(input("What is your Age/Year of birth: "))
except Exception as e:
    print("There was some problem with your age/year of birth")
    exit()

try:
    currentyear = int(input("Please enter current year: "))
except Exception as e:
    print("There was some problem with your current year")
    exit()

try:
    print(years(year, currentyear))
except Exception as e:
    print("please enter valid numbers")