class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1

User1 = User("001", "Smith")
User2 = User("002", "John")

User1.follow(User2)

print(User1.followers)
print(User1.following)
print(User2.followers)
print(User2.following)