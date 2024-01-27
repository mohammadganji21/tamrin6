import math
import functools

tarps = {
    'sum': lambda x: sum(x),
    'average': lambda x: round(sum(x) / len(x), 2),
    'gcd': lambda x: functools.reduce(math.gcd, x),
    'lcd': lambda x: functools.reduce(lambda a, b: a * b // math.gcd(a, b), x),
    'min': lambda x: min(x),
    'max': lambda x: max(x)
}

def perform_operation(operation, data):
    try:
        result = tarps[operation](data)
        print(result)
    except KeyError:
        print("Invalid operation")

def get_input_values():
    values = []
    while True:
        data = input()
        if data.lower() == 'end':
            break
        values.append(int(data))
    return values

def main():
    operation = input()
    input_values = get_input_values()
    perform_operation(operation, input_values)

if __name__ == "__main__":
    main()