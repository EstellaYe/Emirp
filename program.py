def check_prime(number_):
    number_ = int(number_)
    for i in range(2, number_):
        # If you can divide it without remainder by any number lower than it,
        # return False, as it's not a prime number
        if number_ % i == 0:
            return False
        # If you didn't return earlier, then it's a prime number
        return True


number = input("Input a number: ")
# check if the number is a prime and also if its reversed version is
# print True if both numbers are prime
print(check_prime(number) & check_prime(number[::-1]))
