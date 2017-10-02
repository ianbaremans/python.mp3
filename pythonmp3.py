# importing the necessary modules
import stagger
import sys

# user inputs the path to the mp3
path = input("Enter the path to your MP3: ")

# reading and printing the existing tags
tag = stagger.read_tag(path)
print("Title: ", tag.title)
print("Artist: ", tag.artist)
print("Album: ", tag.album)
print("Track: ", tag.track)
print('To change a tag type tag:value (example: title:Champions)')


# function to change the tags
def tagchange():
    print("If you're done enter exit")
    changes = input("Enter change: ")
    if changes == "exit":
        sys.exit()
    else:
        temp_changes = changes[:5]
        if (temp_changes == "Title") or (temp_changes == "title"):
            new_tag = changes[6:]
            tag.title = new_tag
            tag.write()
            print("Title changed!")
            tagchange()
        elif (temp_changes == "Artis") or (temp_changes == "artis"):
            new_tag = changes[7:]
            tag.artist = new_tag
            tag.write()
            print("Artist changed!")
            tagchange()
        elif (temp_changes == "Album") or (temp_changes == "album"):
            new_tag = changes[6:]
            tag.album = new_tag
            tag.write()
            print("Album changed!")
            tagchange()
        elif (temp_changes == "Track") or (temp_changes == "track"):
            new_tag = changes[6:]
            tag.track = new_tag
            tag.write()
            print("Track changed!")
            tagchange()

tagchange()
