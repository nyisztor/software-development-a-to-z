part1 = "Stay hungry." 
part2 = "Stay foolish."
quote = part1 + part2
print(quote)

quote = part1 + " " + part2
print(quote)

quote = f"{part1} {part2}"
print(quote)

quote = f"Stay hungry, {part2}"
print(quote)

name = "Michael"
age = 32
message = f"Your name is {name}, and you are {age} years old"
print(message)

car = "Tesla Roadster"
acceleration = 1.9
message = f"The {car} goes 0-60 mph in {acceleration} seconds"
print(message)

pi = 3.14159265359
message = f"The number pi is approximately equal to {pi}"
print(message)

message = f"The number pi is approximately equal to {pi:.2f}"
print(message)

message = "Stay hungry. Stay foolish."
print(len(message))

message = "起死回生"
print(len(message))

message = "♔♕♖♗♘♙♚♛♜♝♞♟"
print(f"String {message} has a length of {len(message)}")

message = "Stay hungry. Stay foolish."
uppercase_message = message.upper()
print(uppercase_message)

lowercase_message = uppercase_message.lower()
print(lowercase_message)

swappedcase_message = message.swapcase()
print(swappedcase_message)

o_count = "Stay hungry. Stay foolish.".count("o")
print(f"Count of o in {message} is {o_count}")

stay_count = "Stay hungry. Stay foolish.".count("Stay")
print(f"Count of Stay in {message} is {stay_count}")
