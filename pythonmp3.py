# importing the necessary modules
import stagger

# user inputs the path to the mp3
path = input("Enter the path to your MP3: ")

# reading and printing the existing tags
tag = stagger.read_tag(path)
print("Title: ", tag.title)
print("Artist: ", tag.artist)
print("Album: ", tag.album)
print("Track: ", tag.track)

# letting the user enter changes
print('To change a tag type tag:"change" (example: title:"Champions")')
print("If you're done enter exit")
changes = input("Enter change: ")

# writing the changes to the file
tag.write()
