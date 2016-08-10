# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def cumulative_sum(list_name):
	# Calls empty list to store cumulative numbers
	sum_list = []
	for idx,n in enumerate(list_name):
		# First number stays the same in the new list
		if idx == 0:
			sum_list.append(n)
		else:
			sum_list.append(n + sum_list[idx-1])
	return sum_list

def main():
	pass

if __name__ == '__main__':
    main()