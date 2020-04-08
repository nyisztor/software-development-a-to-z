temperature = 68
text = "Done"
is_authenticated = False

restaurants = "Republique" + ", " + "Petit Trois" + ", " + "Majordomo" + ", " + "Sushi Gen"
restaurants = "Republique, Petit Trois, Majordomo, Sushi Gen"

# followers = "Xing Zheng" + ", " + "Sara Scholz" + ", " + "Quinten Kortum" + ...
list()

primes = list()
print(primes)

# append a few prime numbers 2 3 5 7 11 to the list
primes.append(2)
primes.append(3)
primes.append(5)
primes.append(7)
primes.append(11)
print(primes)

primes = [2, 3]
print(primes)

primes = [2, 3, 5, 7, 11]
primes.append(13)
primes.append(17)
print(primes)

# Validates the index of a given list
def is_valid_index(index: int, list: list) -> bool:
    result = False
    if 0 <= index and index < len(list):
        result = True
    
    return result

names = ["Michael", "Dwight", "Pam"]

index = 3
print(f"Index {index} is valid" if is_valid_index(3, names) else f"Index {index} is out of range")
#name = names[3]




values = [True, False, False, True]

bag = [1, 2, 3]
bag.append(True)
bag.append("Pam")
bag.append(4)
bag.append(False)
print(bag)
