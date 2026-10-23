
print('''============== WELCOME IN SMART DATA ANALYZER===============
======================== VERSION 1.0 =======================''')


class SmartDataAnalyzer:

    def __init__(self):
        self.numlist = []

    def get_input(self):
        try:
            raw_data = input(
                "ENTER YOU'RE NUMBERS(use comma to separate) :  "
            )

            # Checking for empty input
            if not raw_data.strip():
                print("Please input valid numbers!")
                return False

            # Converting input into integers
            self.numlist = list(map(int, raw_data.split(",")))
            return True

        except ValueError:
            print("Please enter valid numbers!")
            return False

    def count_numbers(self):
        return len(self.numlist)

    def calculate_sum(self):
        return sum(self.numlist)

    def calculate_average(self):
        return self.calculate_sum() / self.count_numbers()

    def find_maximum(self):
        return max(self.numlist)

    def find_minimum(self):
        return min(self.numlist)

    def display_results(self):
        print("\n=====HERE'S YOUR ANALYZED DATA=====\n")

        print(f"length of the given DATA is : {self.count_numbers()}\n")
        print(f"sum of the given DATA is : {self.calculate_sum()}\n")
        print(f"average of the given DATA is : {self.calculate_average():.2f}\n")
        print(f"largest integer of the given DATA is : {self.find_maximum()}\n")
        print(f"smallest integer of the given DATA is : {self.find_minimum()}")


def main():
    analyzer = SmartDataAnalyzer()

    if analyzer.get_input() and analyzer.count_numbers() > 0:
        analyzer.display_results()


if __name__ == "__main__":
    main()
