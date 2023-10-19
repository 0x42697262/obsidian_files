elven_calories = list()
with open("input") as file:
    total = 0
    for num in file.readlines():
        n = num.replace('\n', '')
        if n == '':
            elven_calories.append(total)
            total = 0
        else:
            total += int(n)


# --- Part One ---
print(max(elven_calories))

# --- Part Two ---
elven_calories_sorted = sorted(elven_calories)
print(elven_calories_sorted[-1]+elven_calories_sorted[-2]+elven_calories_sorted[-3])
