my_age = 28

# +, -, /, *

my_result1 = my_age * 2
my_result2 = my_age / 2
my_result3 = my_age + 2
my_result4 = my_age - 2

print(my_result1)
print(my_result2)
print(my_result3)
print(my_result4)

if my_age > 18:
    print("You are an adult!")
elif my_age == 18:
    print("Congrats, you are now an adult!")
else:
    print("You are not an adult!")

for i in range(5):
    my_result1 = my_result1 * 2

print(my_result1)

bank_account_balances1 = [5322.0, 577.35, -100.0]
bank_account_balances2 = [322.0, 8577.35, -80.0]

def print_bank_account_info(bank_account_info):
    for balance in bank_account_info:
        print(balance)

print_bank_account_info(bank_account_balances1)
print_bank_account_info(bank_account_balances2)
