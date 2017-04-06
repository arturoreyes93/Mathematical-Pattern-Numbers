# print all 3 digit emirps
  # an emirp is a non-palindromic prime which when reversed is prime
num = 100
while (num <= 999):
    if (is_prime(num) and not is_palindromic(num)):
        if (is_prime (rev_num(num))):
            print (num)
