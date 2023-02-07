import random

def fake_table(number):
    table = [number*i for i in range(1, 11)]
    # for i in range(1, 11):
    #     number = number
    #     number1 = number*i
    #     b = table.append(number1)

    table1 = random.choice(table[1:9])
    table2 = table.index(table1)
    table[table2] += 1
    # print(table2)

    return table


def right_table(table, number1):
    table10 = [number1*i for i in range(1, 11)]

    # print(table10)
    # print(table)

    for i in table:
        if i not in table10:
            return f"on {table.index(i)} index rohan function give a wrong value the right value is {table10[table.index(i)]}"

    else:
        return None


enter_table = int(input("enter number: "))
a = fake_table(enter_table)
print(a)
print(right_table(a, enter_table))
