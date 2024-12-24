import random
print("Welcome to Bank Roulette! Where we'll decide who will pay the bill!!")
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# random_choice = random.randint(0,4)
# print(friends[random_choice])
a = [] #created an empty list
friends = int(input("Enter the total number of friends: ")) 
#took total number of friends as an input
for i in range(friends):
    element = input(f"Enter the friend {i+1}: ")
    a.append(element)
print("Friends = ",a )
print(random.choice(a), "will pay the bill!!!!")