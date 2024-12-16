# Creating a hash table using a Python dictionary
hash_table = {}

# Insert key-value pairs
hash_table["name"] = "Alice"
hash_table["age"] = 25

# Retrieve a value by key
print(hash_table["name"])  # Output: Alice

# Update a value
hash_table["age"] = 26

# Delete a key-value pair
del hash_table["name"]

# Check if a key exists
if "name" in hash_table:
    print("Key exists")
else:
    print("Key does not exist")  # Output: Key does not exist

# Iterate over key-value pairs
for key, value in hash_table.items():
    print(f"{key}: {value}")
