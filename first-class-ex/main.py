class User:

    def __init__(self, username, id):
        self.username = username
        self.id = id


user = User("angela", "001")
print(user.username)
print(user.id)
