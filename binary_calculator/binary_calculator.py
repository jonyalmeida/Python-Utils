import os


class Binary_Calculator(object):
    def __init__(self, string_length):
        self.string_length = string_length
        self.binary_array = self.binary_string()
        self.digit_array = self.calculate_bin_str()
        self.added_bytes = sum(self.digit_array)
