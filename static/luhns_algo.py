# Step 1: Double the value of every second digit, beginning with the first digit
# Step 2: If the result of this doubling is > 9, add the digits of the product, e.g. for 16: (1+6=7)
# Step 3: Take the sum of all the digits
# Step 4: If the total ends in zero, this is a valid card number. If not, it's invalid

import csv

class CreditCard:

    allcards = []

    def __init__(self, nums):
        self.nums = nums
        CreditCard.allcards.append(self)

    @classmethod
    # Can't pass self here becuase instances that it will create haven't been instantiated yet, this is what the method is for
    def instantiate_from_csv(cls):
        with open('cardnumbers.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            CreditCard(
                nums=item.get('cardnumbers'),
            )

    @staticmethod
    def is_valid(numbers):  # Static method receives neither self not cls, i.e. it doesn't receive the object as the first argument

        firstcriteria = False
        if len(numbers) == 16:
            firstcriteria = True

        if not firstcriteria:
            print("Card number is not correct length...")

        if firstcriteria:
            lst = [int(x)*2 if i % 2 == 0 else int(x) for i, x in enumerate(numbers)]
            lst_str = [str(x) for x in lst]
            lst_final = [(int(lst_str[i][0]) + int(lst_str[i][1])) if int(lst_str[i]) > 9 else int(lst_str[i]) for i, x in enumerate(lst_str)]
            final_sum = sum(lst_final)

        print("Final sum:", final_sum)

        str_final_sum = str(final_sum)
        print("Valid card!" if len(str_final_sum) ==
              2 and str_final_sum[-1] == '0' else "Invalid card...")

    def __repr__(self):
        return f"CreditCard('{self.nums}')"


CreditCard.instantiate_from_csv()
print(CreditCard.allcards)
CreditCard.is_valid('4319320016171373')

# Can also iterate through the allcards list and check if each card is valid or not
# I have included one valid card and one invalid card in the csv file
# for item in CreditCard.allcards:
#     strcardnum = str(item.nums)
#     print(CreditCard.is_valid(strcardnum))
