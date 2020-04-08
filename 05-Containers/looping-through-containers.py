primes = [2, 3, 5, 7, 11]

for number in primes:
    # do something with the element
    print(number)


even_numbers = []
odd_numbers = []

for number in primes:
    if number % 2 == 0:
        even_numbers.append(number)        
    else:
        odd_numbers.append(number)

print("Even number(s)")
for i in even_numbers:
    print(i)

print("Odd number(s)")
for j in odd_numbers:
    print(j)

# looping through the elements of a list using while 
# requires more code code and it's not as fail-safe as the for-in counterpart
index = 0
while index < len(primes):    
    print(primes[index])
    index += 1

ssn_name_pairs = {"123-456-789": "John Appleseed", 
                  "000-000-002": "Dwight Schrute",
                  "999-000-005": "Pam Beesly"}

keys = ssn_name_pairs.keys()
values = ssn_name_pairs.values()

for key in keys:
    print(key)

for value in values:
    print(value)


key_value_pairs = ssn_name_pairs.items()

for key_value in key_value_pairs:
    print(key_value[0], key_value[1])

for (key, value) in key_value_pairs:
    print(key, value)