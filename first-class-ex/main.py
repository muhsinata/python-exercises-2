class User:

    def __init__(self, username, id):
        self.username = username
        self.id = id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("Mike", "001")
user2 = User("Steve", "002")

user1.follow(user2)

print(f"user1 is following {user1.following} people.")
print(f"user2 is being followed by {user2.followers} people.")