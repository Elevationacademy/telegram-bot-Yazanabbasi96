def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return "Not Prime"
                break
        else:
            return "is Prime"


def factorial(num):
    return 1 if num == 1 or num == 0 else num * factorial(num - 1)


functions_dict = {"check": is_prime, "factorial": factorial}
