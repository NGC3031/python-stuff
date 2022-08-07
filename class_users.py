class User():
    """A simple attempt to model users."""

    def __init__(self, first_name,last_name, userID, age):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.userID = userID
        self.age = age
    def print_name(self):
        """Display the users name."""
        print(self.first_name.title() +" "+ self.last_name.title())

"""Assuming this would really come from a DB of some sort"""
user_list =[['bob','smith','1000','26'],['wendy','tan','1001','19']]

"""Now just creating multiple objects"""
users = [User(first_name=user[0], last_name=user[1], userID=user[2], age=user[3]) for user in user_list]

for user in users:
    user.print_name()