#Quiz: Fix the Quote
#The line of code in the following quiz will cause a SyntaxError, thanks to the misuse of quotation marks. First run it with Test Run to view the error message. Then resolve the problem so that the quote (from Henry Ford) is correctly assigned to the variable ford_quote.
# TODO: Fix this string!
#ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
#print(ford_quote)
#--------------------------
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"
message = f"{username} accessed the site {url} at {timestamp}"
print(message)
#------------------------
given_name = 'William'
middle_names = 'Bradley'
family_name = 'Pitt'

name_length =len(given_name + middle_names + family_name) #todo: calculate how long this name is
#name_length = len(given_name) + len(middle_names) + len(family_name) + 2
#name_length = len(given_name) + len(middle_names) + len(family_name) + 2
print(name_length)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)


