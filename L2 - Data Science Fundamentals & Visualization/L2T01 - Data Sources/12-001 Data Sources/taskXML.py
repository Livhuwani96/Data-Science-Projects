#import the needed modules, in this case it is the ElementTree.
import xml.etree.ElementTree as ET

# Load and parse the XML file
# Parses the XML file and returns an ElementTree object
# Gets the root element of the XML tree

tree = ET.parse('movie.xml')
root = tree.getroot()

#Use the iter()function to list all the child tags of the movie element.
# Iterates over all 'movie' elements in the XML
# Prints the movie title and favorite status
# Iterates over all child elements of each 'movie' element
print("The child tags of all movie element: ")
for movie in root.iter('movie'):
    print(f"movie title: {movie.get('title')}, Favorite: {movie.get('favorite')}" )
    for child in movie:
        print(f" {child.tag}: {child.text.strip() if child.text else 'No text'}")
print()


#Use the iter() function to list all the child tags of the movie element.
# Iterates over all 'movie' elements in the XML
# Finds the 'description' child element within each 'movie' element
# Checks if the 'description' element exists
print("Movie Descriptions")
for movie in root.iter('movie'):
    description = movie.find('description')
    if description is not None:

        #Here we are going to join all the text pieces from itertext().

        description_text = ''.join(description.itertext()).strip()
        print(f"{movie.get('title')}: {description_text}")
    print()

# Find the number of movies that are favorites and the number that are not
# Checks if the 'favorite' attribute is 'true' (case insensitive)
# Increments the favorite movies count

favorite_count = 0
non_favorite_count = 0

for movie in root.iter('movie'):
    if movie.get('favorite').lower() == 'true':
        favorite_count += 1
    else:
        non_favorite_count += 1

# Prints the counts of favorite and non-favorite movies
print(f"The number of favorite movies: {favorite_count}")
print(f"The number of non-favorite movies: {non_favorite_count}")




