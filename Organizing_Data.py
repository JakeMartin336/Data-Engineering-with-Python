import heapq

#class that creates an object for each database entered by user
class Object:
    def __init__(self, name):
        self.name = name

#function that calculates similarity of each object
def calculate_similarity(obj):
    return len(obj.name) #current calculate is by length of object's name

#function to organize the databases 
def organize_database(database, user_input):
    sorted_objects = [] #initialize sorted array to return
    # Organize alphabetically using a hash table
    if user_input == 'alphabetical':
        hash_table = {} #initialize hash table
        for obj in database:
            hash_table[obj.name] = obj
        for key in sorted(hash_table.keys()):
            sorted_objects.append(hash_table[key])
        return sorted_objects
    # Organize by most similar using a binary heap
    elif user_input == 'similar':
        sorted_objects = heapq.nlargest(len(database), database, key=calculate_similarity)
        # heapq.heapify(database, key=calculate_similarity)
        # for _ in range(len(database)):
        #     obj_temp = heapq.heappop(database)
        #     sorted_objects.append(obj_temp)
        return sorted_objects
    else:
        print("Invalid input. Please enter 'alphabetical' or 'similar'.")
        return []

#prompt the user to input the database
database = []
while True:
    name = input("Enter database name (or 'done' to finish): ")
    if name.lower() == "done":
        break
    database.append(Object(name))


# Prompt the user for input
user_input = input("Enter 'alphabetical' or 'similar': ").lower()

# Organize the database based on user input
sorted_objects = organize_database(database, user_input)

# Display the organized database
print("Organized Database:")
for obj in sorted_objects:
    print(obj.name)