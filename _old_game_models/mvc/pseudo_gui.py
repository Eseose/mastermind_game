class Display:

    def __init__(self):

        self.input = None
        self.output = None

    def get_int(self, msg):
        choice = None
        while choice not in options:
            try:
                choice = int(input("Choose Option Number: "))
            except:
                print("Please choose the option number (e.g 1)")
        return choice

    def get_str(self, options):
        choice = None
        while choice not in options:
            choice = input("Your Choice: ")
        return choice

    def display_msg(self, msg):
        print(msg)
        return
