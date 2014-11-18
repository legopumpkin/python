candies = ['snickers', 'smarties', 'peppermints']

def eat_candy(number_of_pieces):
	for treat in candies:
		print "I ate %s pieces of %s" % (number_of_pieces, treat)

answer = raw_input('How many pieces? ')

# Converts to number
answer = int(answer)

# Prints how much candy I ate
eat_candy(answer)

if answer > 10:
	print 'I feel sick.'
