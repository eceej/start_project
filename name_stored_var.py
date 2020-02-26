first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name # concatenating names with a blank space in middle
message = "Hello, " + full_name.title() + "!" # message is used as a variable to store greeting
print(message)

print ("\tPython") #to add whitespacing use \t

print("Languages:\nPython\nC\nJavaScript") # newline \n 

# tabs and newline \n\t can be used also see below
print("Languages:\n\tPython\nC")

#stripping whitespacing good for data entry to remove spaces at end of name etc.

favorite_language = " python "
favorite_language = favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()
print(favorite_language)
