# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(list_name):
	# Calls empty list to fill with all strings capitalized
	capital_list = []
	for item in list_name:
		# If the list has a list, it will run the function again
		if type(item) == list:
			capital_list.append(capitalize_nested(item))
		# Capitalize first letter of string and adds to the empty list
		else:
			capital_list.append(item.title())
	return capital_list


def main():
   pass

if __name__ == '__main__':
    main()
