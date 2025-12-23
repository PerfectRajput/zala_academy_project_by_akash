# ---------------- Question 1 ----------------
# Generate Arithmetic Exception without exception handling
def q1():
    a = 10 / 0   # ZeroDivisionError
    print(a)


# ---------------- Question 2 ----------------
# Handle Arithmetic Exception using try-except
def q2():
    try:
        a = 10 / 0
        print(a)
    except ZeroDivisionError as e:
        print("Caught Arithmetic Exception:", e)


# ---------------- Question 3 ----------------
# Method which throws exception, called without try block
def risky_method():
    raise ZeroDivisionError("Division by zero inside method")

def q3():
    # No try block here → program will crash
    risky_method()


# ---------------- Question 4 ----------------
# Program with multiple except blocks
def q4():
    try:
        arr = [1, 2]
        print(arr[5])   # IndexError
    except ZeroDivisionError:
        print("Caught Arithmetic Exception")
    except IndexError:
        print("Caught Index Error")
    except Exception as e:
        print("Caught General Exception:", e)


# ---------------- Question 5 ----------------
# Throw exception with your own message
def q5():
    try:
        raise Exception("This is my custom message!")
    except Exception as e:
        print("Caught Exception:", e)


# ---------------- Question 6 ----------------
# Create your own exception
class MyException(Exception):
    pass

def q6():
    try:
        raise MyException("This is my own exception!")
    except MyException as e:
        print("Caught MyException:", e)


# ---------------- Question 7 ----------------
# Program with finally block
def q7():
    try:
        a = 10 / 0
    except ZeroDivisionError:
        print("Caught Arithmetic Exception")
    finally:
        print("Finally block always executes")


# ---------------- Question 8 ----------------
# Generate Arithmetic Exception
def q8():
    a = 5 / 0   # ZeroDivisionError


# ---------------- Question 9 ----------------
# Generate FileNotFoundError
def q9():
    with open("nonexistent.txt", "r") as f:
        print(f.read())


# ---------------- Question 10 ----------------
# Generate ClassNotFoundException equivalent
# In Python, ImportError is similar
def q10():
    import importlib
    importlib.import_module("nonexistent_module")  # ImportError


# ---------------- Question 11 ----------------
# Generate IOException equivalent
def q11():
    import os
    # Trying to open a directory as a file → OSError (IOError)
    with open(os.getcwd(), "r") as f:
        print(f.read())


# ---------------- Question 12 ----------------
# Generate NoSuchFieldException equivalent
# In Python, AttributeError is similar
def q12():
    class Demo:
        x = 10
    obj = Demo()
    print(obj.nonexistent_field)  # AttributeError


if __name__ == "__main__":
    # Uncomment one at a time to see behavior
    # q1()
    q2()
    # q3()
    # q4()
    # q5()
    # q6()
    # q7()
    # q8()
    # q9()
    # q10()
    # q11()
    # q12()
