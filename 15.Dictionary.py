# ---------------- Question 1 ----------------
# Create a Dictionary with at least 5 key-value pairs of Student ID and Name
students = {
    101: "Amit",
    102: "Priya",
    103: "Ravi",
    104: "Sneha",
    105: "Arjun"
}
print("Initial Dictionary:", students)


# ---------------- Question 1.1 ----------------
# Adding values in dictionary
students[106] = "Neha"
students[107] = "Vikram"
print("After Adding:", students)


# ---------------- Question 1.2 ----------------
# Updating values in dictionary
students[103] = "Rahul"   # Update Ravi → Rahul
print("After Updating:", students)


# ---------------- Question 1.3 ----------------
# Accessing the value in dictionary
print("Access Student with ID 104:", students[104])


# ---------------- Question 1.4 ----------------
# Create a nested loop dictionary (dictionary inside dictionary)
nested_students = {
    201: {"name": "Kiran", "age": 20, "course": "Math"},
    202: {"name": "Meena", "age": 21, "course": "Science"},
    203: {"name": "Suresh", "age": 22, "course": "History"}
}
print("Nested Dictionary:", nested_students)


# ---------------- Question 1.5 ----------------
# Access the values of nested loop dictionary
print("Access Meena's course:", nested_students[202]["course"])
print("Access Suresh's age:", nested_students[203]["age"])


# ---------------- Question 1.6 ----------------
# Print the keys present in a particular dictionary
print("Keys in students dictionary:", students.keys())
print("Keys in nested_students dictionary:", nested_students.keys())


# ---------------- Question 1.7 ----------------
# Delete a value from a dictionary
del students[102]   # Delete Priya
print("After Deletion:", students)
