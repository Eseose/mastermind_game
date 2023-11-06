from number_randomizer import NumberRandomizer
from collections import Counter

generator = NumberRandomizer()
num = generator.get()
print("Generated Number:", num)
attempts = 10
valid_input = False
for attempt in range(attempts):
    while not valid_input:
        guess_str = input("Guess a four digit number made up of "
                          "only numbers between 0 and 7 inclusive.\n"
                          f"You have {attempts - attempt} attempts.\n"
                          "Your Guess?... \n")
        # implement try and except to ensure only the right numbers are input
        try:
            # 0234 gives 234 is_valid function needed
            guess_int = int(guess_str)
            valid_input = True  # not checking the 0 - 7 constraints yet
            guess = [int(item) for item in guess_str]
        except:
            print("Please input integers only")

    correct_nums, correct_loc = 0, 0
    num_freq = Counter(num)
    if guess == num:
        print("all correct")
        break
    else:
        valid_input = False
        for i in range(len(guess)):
            if guess[i] == num[i]:
                correct_nums += 1
                correct_loc += 1
            else:
                if guess[i] in num_freq and num_freq[guess[i]] != 0:
                    correct_nums += 1
                    num_freq[guess[i]] -= 1
        print(f"{correct_nums} correct number and"
              f" {correct_loc} correct location")

print("you lose!")
