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
            odddigits = numbers[0::2]
            odddigitsint = [int(x) for x in odddigits]
            doublevalue = [x*2 for x in odddigitsint]
            print(f"After doubling the odd digits: {doublevalue}")
            evendigits = numbers[1::2]
            evendigitsint = [int(x) for x in evendigits]

        lst = []
        for value in doublevalue:
            if value > 9:
                sum = 0
                for digit in str(value):
                    sum += int(digit)
                lst.append(sum)
        print(
            f"The list containing product of nums > 9 following doubling: {lst}")

        final = []
        doublevalueammended = []
        count = 0
        for i in doublevalue:
            if i > 9:
                doublevalueammended.append(lst[count])
                count += 1
            else:
                doublevalueammended.append(i)

        for i in range(0, 8):
            final.append(doublevalueammended[i])
            final.append(evendigitsint[i])
        print(f"This is the final list: {final}")

        finalsum = 0
        for integerr in final:
            finalsum += integerr
        print("Final sum:", finalsum)

        strfinalsum = str(finalsum)
        if len(strfinalsum) == 2 and strfinalsum[1] == '0':
            print("Valid card!")
        else:
            print("Invalid card...")

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
