#MY CODE SOLUTION
print("starwars name generator. Let us find out what is your starwars name!")
fName = input("Input your first name >") 
lName = input("Inpput your last name >")
motherName = input("Input mothers maiden  name >")
cityName = input("input city name >")
starwarsName = f"{fName[:3].title()}{lName[:3].lower()} {motherName[:2].title()}{cityName[-3:].lower()}"

print(f"Your starwars name is  {starwarsName}")



#This is the challenge you're looking for. This program will generate your Star Wars Name.

#Ask the user to input their first & last names.
#Slice the first 3 letters of the first name.
#Slice the first 3 letters of the last name (surname).
#Join them together. Ideally change the case so that it looks good - think fStrings or .upper()/.lower(). This is the user's Star Wars first name.
#Now ask the user for their mother's maiden name and the city where they were born. (Maiden name is the last name they had before they got married. If you are not sure, make up a last name.)
#Combine the first two letters of the maiden name with the last 3 letters of the city to make the user's Star Wars last name. Remember, fStrings and .upper()/.lower().
#Finally, print them both as part of a sentence.
#🥳 Extra points for getting all the inputs #with just one input command and the split function.

#Example:

#🌟Star Wars Name Generator🌟
#Input your first name > David
#Input your lastname > Morgan
#Input your mother's maiden name > Jones
#Input the city where you were born > Cardiff
#Your Star Wars name is Davmor Joiff



  #🌟Star Wars Name Generator🌟

  #Input your first name > David

  #Input your lastname > Morgan

  #Input your mother's maiden name > Jones

  #Input the city where you were born > Cardiff

  #Your Star Wars name is Davmor Joiff


  #To get charaters from the beginning of a string, leave the first argument blank. ex: [:3] gets the first 3 characters.
  #To get charaters from the end of a string, make the first argument a negative number for how many charaters to get. Leave the last argument blank. ex: [-5:] gets the last 5 characters.
  #fString formatting uses .title for first character capitalization and .lower for all lower case.
  #Use fStrings to join the sliced characters to a new variable as you get the correct characters from each string.
  #For extra points, get the user to input all info at once separated by spaces.


#instructor solution


#print("STAR WARS NAME GENERATOR")

#all = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()
#
#first = all[0].strip()
#last = all[1].strip()
#maiden = all[2].strip()
#city = all[3].strip()

#name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

#print(f"Your Star Wars name is {name}")


      

