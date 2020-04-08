def solve_equation(a: float, b: float, c: float) -> float:
    try:
        return (float(c) - float(b)) / float(a)
    except ZeroDivisionError:
        print("Error! 'a' can't be zero. Enter a valid value.")
    except ValueError:
        print("Error! Make sure you enter numeric values.")
    finally:
        print("Leaving solve_equation()")


print("ax + b = c linear equation solver")

a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

try:
    x = solve_equation(a, b, c)
except Exception:
    print("Something bad happened.")
else:
    print(f"x is {x}")