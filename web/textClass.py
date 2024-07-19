class StringSaver:
    def __init__(self, initial_string=""):
        """
        Initializes the StringSaver with an optional initial string.
        """
        self.saved_string = initial_string

    def get_string(self):
        """
        Returns the saved string.
        """
        return self.saved_string

    def update_string(self, new_string):
        """
        Updates the saved string with a new string.
        """
        self.saved_string = new_string

    def display_string(self):
        """
        Prints the saved string.
        """
        print(self.saved_string)

class state:#maybe dont need it
    def __init__(self, initial_string=""):
        """
        Initializes the StringSaver with an optional initial string.
        """
        self.saved_state = initial_string
    def get_state(self):
        """
        Returns the saved string.
        """
        return self.saved_state

    def update_state(self, new_string):
        """
        Updates the saved string with a new string.
        """
        self.saved_state = new_string

class arraySaver:#maybe dont need it
    def __init__(self):
        """
        Initializes the StringSaver with an optional initial string.
        """
        self.saved_array = []
    def get_array(self):
        """
        Returns the saved string.
        """
        return self.saved_array

    def add_to_array(self, new_string):
        """
        Updates the saved string with a new string.
        """
        self.saved_array.append(new_string)   
  