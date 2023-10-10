import random


complexity = {
    1: "Only letters (lowercase)",
    2: "Only letters (uppercase)",
    3: "Only letters (lowercase and uppercase)",
    4: "Only numbers",
    5: "Only letters and numbers",
    6: "Only letters, numbers and special characters",
}

class PasswordGenerator:
    password = ""
    password_characters = ""
    password_complexity_int = 0
    password_length_int = 0
    uppercase_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_characters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special_characters = "!@#$%&*()_+-=[]{};:,./<>?|"


    def __init__(self, password_length, password_complexity):
        self.password_length_int = password_length
        self.password_complexity_int = password_complexity

    def generate_password(self):
        for i in range(self.password_length_int):
            self.password += self.generate_password_character()
    
    def generate_password_character(self) -> str:
        self.get_characteres()

        if self.password_characters:
            return random.choice(self.password_characters)
        return ""

    def get_characteres(self):
        if "uppercase" in self.get_complexity():
            self.password_characters += self.uppercase_characters
        if "lowercase" in self.get_complexity():
            self.password_characters += self.lowercase_characters
        if "numbers" in self.get_complexity():
            self.password_characters += self.numbers
        if "special characters" in self.get_complexity():
            self.password_characters += self.special_characters

    def get_complexity(self) -> str:
        return complexity.get(self.password_complexity_int, "Invalid complexity").lower()


if __name__ == "__main__":
    print("Password Generator")
    print("------------------")
    print()

    print("Inform the password length: ")
    password_length = int(input())
    print()

    print("Inform the password complexity: ")
    print("1 - Only letters (lowercase)")
    print("2 - Only letters (uppercase)")
    print("3 - Only letters (lowercase and uppercase)")
    print("4 - Only numbers")
    print("5 - Only numbers and letters (lowercase and uppercase)")
    print("6 - Only numbers, special characters and letters (lowercase and uppercase)")
    password_complexity = int(input())
    print()

    password_generator: PasswordGenerator = PasswordGenerator(
        password_length,
        password_complexity,
    )
    password_generator.generate_password()

    print("Password Generator")
    print("------------------")
    print()
    print("Password: ", password_generator.password)
