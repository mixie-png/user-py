class User:
    # Attributes
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # Methods
    def display_info(self):
        print("First Name:" , self.first_name , "Last Name:" , self.last_name , "Email:" , self.email , "Age:" , self.age, "Enrolled:", self.is_rewards_member, "Current Gold Points:", self.gold_card_points)
        return self

    def enroll(self):
        if self.is_rewards_member != False:
            print("Already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("Insufficient points")
        return self

user1 = User("Beyonce", "Knowles", "beyonce@gmail.com", 42)

user1.display_info().enroll().display_info()

user2 = User("Rihanna", "Fenty", "rihanna@gmail.com", 35)
user3 = User("Lori", "Harvey", "lori_harvey@gmail.com", 26)

user1.spend_points(50).display_info()

user2.enroll().spend_points(80).display_info()

user1.display_info().enroll().display_info()
user2.display_info()
user3.display_info().spend_points(40)