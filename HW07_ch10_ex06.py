# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(list_name):
	for idx,item in enumerate(list_name):
		# First value doesn't have to be checked
		if idx != 0:
			if item < list_name[idx-1]:
				return False
	return True


def main():
	print(is_sorted([1,2,3,4]))

if __name__ == '__main__':
    main()