class GeniusPrinter:
    def __init__(self):
        self.geniuses = ["Walter", "Jarmauri", "Carl", "Ollie"]

    def print_list(self):
        for genius in self.geniuses:
            print(genius)

    def run(self):
        # Initial print
        self.print_list()

        # Ask if user wants to print again
        answer = input("Do you want me to print the list again? (Y/N): ").strip().upper()
        while answer == "Y":
            self.print_list()
            answer = input("Do you want me to print the list again? (Y/N): ").strip().upper()

# Create an instance and run the logic
printer = GeniusPrinter()
printer.run()
