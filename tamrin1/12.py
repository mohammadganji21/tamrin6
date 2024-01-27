def convert_to_binary_string(n):
    return "{:032b}".format(int(n))

def check_binary_digit(binary_str, position):
    return 'yes' if binary_str[-position - 1] == '1' else 'no'

def main():
    rightside = convert_to_binary_string(input())
    leftside = convert_to_binary_string(input())

    num_of_elements = int(input())

    binary_tamam_afrad = leftside + rightside

    results = [check_binary_digit(binary_tamam_afrad, int(input())) for _ in range(num_of_elements)]

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
