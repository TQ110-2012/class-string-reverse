class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_word(self):
        return self.s[::-1]

user_input = input("Enter the word you want to reverse: ")

obj = Reverse(user_input)

print(f"The reversed string is: {obj.reverse_word()}")
