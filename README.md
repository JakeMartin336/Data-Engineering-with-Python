# Organizing_Data
 
Description:
This Python script allows users to organize a list of databases either alphabetically or based on their similarity. It utilizes hash tables for alphabetical organization and a binary heap for similarity-based organization.

Code Structure:
- Object Class : A class representing a database object with a name attribute.
- calculate_similarity : A function to calculate the similarity of each database object. Currently, it calculates based on the length of the object's name.
- organize_database : A function to organize the databases either alphabetically or by similarity.
- Main Program : The main part of the script where the user inputs the databases and chooses the organization method.

Note:
- If an invalid input is provided for organization method, the script will display an error message and exit.