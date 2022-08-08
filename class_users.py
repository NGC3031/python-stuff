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
    def find_user(self, users, key):
        """Method to find user"""
        count=0
        for user in users:
            if user.first_name==key or user.first_name==key.title():
                print("We have found " + key.title())
                count+=1
        if count==0:
            print("User "+ key.title()+" not found")

"""Assuming this would really come from a DB of some sort"""
#user_list =[['bob','smith','1000','26'],['wendy','tan','1001','19']]

user_list = [
	{
		'first_name':'bob',
		'last_name':'smith',
        'userID':'1000',
        'age':'26'
	},
	{
	    'first_name':'wendy',
		'last_name':'tan',
        'userID':'1001',
        'age':'19'
	},
	{	'first_name':'steve',
		'last_name':'black',
        'userID':'1002',
        'age':'41'
    }
]

"""Now just creating multiple objects"""
users = [User(first_name=user['first_name'], last_name=user['last_name'], userID=user['userID'], age=user['age']) for user in user_list]

for user in users:
    user.print_name()

user.find_user(users,key="wendy")
user.find_user(users,key="Micheal")
"""Find a user - will update to a method but going to bed"""
#for user in users:
#    if user.first_name=='wendy':
#        print("We have found Wendy")