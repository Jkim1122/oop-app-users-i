class User:
    def __init__(self, username, email_address, drivers_license, phone_number):
        self.username = username
        self.email_address = email_address
        self.drivers_license = drivers_license
        self.phone_number = phone_number
    
my_user = User("jkim1122", "jkimz1122@gmail.com", "K8472975385", "555-555-5555")
brendo_user = User("brendo.ontherocks", "balcala@us.af.mil", "A8675309", "012-345-6789")
harsh_user = User("hvarma467", "hvarma@yahoo.com", "V463463463", "888-888-8888")

print("username", my_user.username)
print("email_address", my_user.email_address)
print("username", brendo_user.username)
print("email_address", brendo_user.email_address)
print("username", harsh_user.username)
print("email_address", harsh_user.email_address)
