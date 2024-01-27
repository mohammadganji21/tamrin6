def process_input():
    data = []
    while True:
        user_input = input()
        if user_input == "-1 -1":
            break
        else:
            n, b = map(int, user_input.split())
            data.append((n, b))
    return data

def find_sum_of_divisors(number):
    divisor_sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum

def convert_to_custom_base(number, base):
    if base < 2 or base > 9:
        return "0"
    result = ""
    while number > 0:
        result = str(number % base) + result
        number //= base
    return int(result) if result else 0

def main():
    data = process_input()
    total_result = 0
    invalid_base = False
    for n, b in data:
        div_sum = find_sum_of_divisors(n)
        base_result = convert_to_custom_base(div_sum, b)

        if base_result != "0":
            total_result += int(base_result)
        else:
            print("Invalid base!")
            invalid_base = True
            break

    if not invalid_base:
        print(total_result)

if __name__ == "__main__":
    main()