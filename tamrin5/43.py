class MrCrab:
    def __init__(self, input_string):
        self.data = input_string

    def process_data(self):
        if self.data.startswith("m"):
            self.data += self.data[:10]
            self.data = self.data.replace("tt", "o")
        else:
            reversed_data = self.data[::-1]
            if reversed_data.startswith("m"):
                self.data = reversed_data.replace("tt", "o")
                self.data += self.data[:10]
            else:
                self.data = None

    def get_output(self):
        return self.data


class SpongeBob:
    def __init__(self, input_string):
        self.data = input_string

    def repeat_first_ten_characters(self):
        self.data += self.data[:10]

    def merge_sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1

    def process_data(self):
        self.repeat_first_ten_characters()

        if self.data is not None and self.data.startswith("sb"):
            length_str = str(len(self.data))
            length_array = list(length_str)
            self.merge_sort(length_array)
            self.
