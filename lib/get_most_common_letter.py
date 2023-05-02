def get_most_common_letter(text):
    print(f"initial input is the text {text}")
    counter = {}
    for char in text:
        if char != " ":
            counter[char] = counter.get(char, 0) + 1
            print(f" counter[char]: { counter[char]} = counter.get(char, 0): {counter.get(char, 0) +1 }")
    letter = sorted(counter.items(), key=lambda item: item[1], reverse= True)[0][0]

    print(f"the letter: {letter}, counter item = {counter.items()}")
    # print(f"printing the function that letter is assigned to {sorted(counter.items(), key=lambda item: item[-1])[1][0]}")
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")

# print(get_most_common_letter("a a a a b c d !"))