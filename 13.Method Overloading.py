# ---------------- Question 1 ----------------
# Write two methods with the same name but different number of parameters of same type

class Demo1:
    def add(self, *args):   # variable arguments
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            return "Unsupported number of parameters"

# Example usage
obj1 = Demo1()
print("Q1 - add(10, 20):", obj1.add(10, 20))        # 30
print("Q1 - add(10, 20, 30):", obj1.add(10, 20, 30)) # 60


# ---------------- Question 2 ----------------
# Write two methods with the same name but different number of parameters of different data type

class Demo2:
    def show(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            return f"Integer: {args[0]}"
        elif len(args) == 1 and isinstance(args[0], str):
            return f"String: {args[0]}"
        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], str):
            return f"Integer: {args[0]}, String: {args[1]}"
        else:
            return "Unsupported combination"

# Example usage
obj2 = Demo2()
print("Q2 - show(100):", obj2.show(100))          # Integer
print("Q2 - show('Hello'):", obj2.show("Hello"))  # String
print("Q2 - show(25, 'World'):", obj2.show(25, "World"))  # Integer + String


# ---------------- Question 3 ----------------
# Write two methods with the same name and same number of parameters of same type
# In Python, the last definition overrides the previous one.

class Demo3:
    def greet(self, name):
        return f"Hello, {name}!"   # This will be overridden

    def greet(self, name):         # Overrides the previous greet
        return f"Hi, {name}!"

# Example usage
obj3 = Demo3()
print("Q3 - greet('Alice'):", obj3.greet("Alice"))  # Output: Hi, Alice!
