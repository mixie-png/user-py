class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("First Name:" , self.first_name , "Last Name:" , self.last_name , "Email:" , self.email , "Age:" , self.age, "Enrolled:", self.is_rewards_member, "Gold Points:", self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member != False:
            print("Already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200


    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("Insufficient points")


user1 = User("Beyonce", "Knowles", "beyonce@gmail.com", 42)

user1.display_info()

user1.enroll()
print(user1.is_rewards_member)
print(user1.gold_card_points)

user2 = User("Rihanna", "Fenty", "rihanna@gmail.com", 35)
user3 = User("Lori", "Harvey", "lori_harvey@gmail.com", 26)

user1.spend_points(50)
print(user1.gold_card_points)

user2.enroll()
user2.spend_points(80)
print(user2.gold_card_points)

user1.display_info()
user2.display_info()
user3.display_info()

user1.enroll()
user1.display_info()
user3.spend_points(40)