def is_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1))

def count_primes_in_range(start, end):
    return sum(1 for num in range(start, end + 1) if is_prime(num))

a, b = map(int, input().split())

if a < b:
    count = count_primes_in_range(a, b)
    order_type = 'Main'
else:
    count = count_primes_in_range(b, a)
    order_type = 'Reverse'

print(f'{order_type} order - amount: {count}')
