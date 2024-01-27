def find_indices_for_sum(numbers, target_sum):
    indices_map = {}
    result_indices = []

    for i, num in enumerate(numbers):
        complement = target_sum - num

        if complement in indices_map:
            result_indices.append((indices_map[complement], i))

        indices_map[num] = i

    return result_indices

def main():
    list_of_numbers = list(map(int, input().split()))
    result_we_want = int(input())

    result_indices = find_indices_for_sum(list_of_numbers, result_we_want)

    if result_indices:
        result_indices.sort()
        for indices in result_indices:
            print(indices[0], indices[1])
    else:
        print("Not Found!")

if __name__ == "__main__":
    main()
