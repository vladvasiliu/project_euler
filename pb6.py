# https://projecteuler.net/problem=6

def sum_of_squares(n):
    result = 0
    for x in range (1, n+1):
        result += x * x
    return result


def square_of_sums(n):
    result = 0
    for x in range( 1, n+1):
        result += x
    return result * result


if __name__ == '__main__':
    print(square_of_sums(100) - sum_of_squares(100))
