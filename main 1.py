# class Car:
#     def __init__(self,car_brand, car_seats):
#         self.brand = car_brand
#         self.seats = car_seats
#
#
# car_1 = Car("BMW",2)
# car_2 = Car("BYD",5)
# car_3 = Car("toyota",6)
# print(car_3.brand)



# class User:
#     def __init__(self,user_id , username):
#         self.id = user_id
#         self.username = username
#         self.following = 0
#         self.followers = 0
#     def follow(self,user):
#         user.followers += 1
#         self.following += 1
#
# user1 = User("01","andi")
# user2 = User("02","budi")
#
#
# user1.follow(user2)
# print(user1.followers)
# print(user1.following)
# print(user2.followers)
# print(user2.following)


class Car:
    def __init__(self,car_brand, car_seats):
        self.brand = car_brand
        self.seats = car_seats

    def car_info(self):
        print("brand:",self.brand)
        print("seats",self.seats)
    def add_passenger(self,number):
        self.seats += number

car_1 = Car("BMW",2)
car_2 = Car("BYD",5)

print(car_1.car_info())
print(car_2.car_info())
car_1.add_passenger(1)
print("seats car_1 setelah ditambah:",car_1.seats)
