import os

# declare class


class Binary_Calculator(object):
    def __init__(self, string_length):
        self.string_length = string_length
        self.binary_array = self.binary_string()
        self.digit_array = self.calculate_bin_str()
        self.added_bytes = sum(self.digit_array)

    # populate the binary string
    def binary_string(self):
        # populate binary string with zeros
        bin_str = [0 for i in range(self.string_length)]
        for idx in range(self.string_length):
            os.system("cls")  # clears terminal
            print("[ Binary Calculator ]\n")
            print(f"Current Binary String: {bin_str}")
            try:
                value = int(
                    input(f"Enter {idx + 1} element (0 - 1) Left to Right: "))
                if value == 0 or 1:
                    bin_str[idx] = value
                else:
                    print("Need binary 0 - 1")
                    break
            except 0 > value > 1:
                print("Need Integer values, 0 - 1")

        print(f"Current String: {bin_str}")
        return bin_str

    def calculate_bin_str(self):
        # revert the list so we calculate from right to left
        binary_string = list(reversed(self.binary_array))
        calculated = []
        for idx, value in enumerate(binary_string):
            if value == 1:
                value += 1
                calculated.append(value**idx)
            elif value == 0:
                calculated.append(0)
            else:
                print("Can only take binary numbers (0-1)")
                break
        return list(reversed(calculated))

    def __repr__(self):
        os.system("cls")
        print(" [Binary Calculator ]\n")
        print(f"Binary String: {self.binary_array}")
        print(f"Digit String: {self.digit_array}")
        print(f"Total Amount of Bits: {self.added_bytes}")
        return str("Program Exited...")


if __name__ == "__main__":
    os.system("cls")
    print("[ Binary Calculator ]\n")
    string_length = int(input("Enter length of binary string\n >> "))
    print(Binary_Calculator(string_length))
