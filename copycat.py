import sys
import logging
import os

# copies a string to the clipboard
def copyToClip(string):
	os.system('echo "%s" | xclip -selection clipboard' % string)

#sudo apt-get install xclip -y

counterFile = 0									# counter


logging.basicConfig(level=logging.INFO)			# setting up the logger
logger = logging.getLogger("CopyCat\t")			# setting a logger

logger.info('Getting arguments')

listArgs	= sys.argv							# getting the args
numArgs 	= len(listArgs) 					# getting the number of args passed

numArgs 	= numArgs - 1						# not calculating the name of the file
#listArgs 	= listArgs.pop(0)					# i dont want the name of the file in the array

if numArgs:					
	logger.info('Got some arguments')
else:
	logger.info('We need some arguments')
	logger.info('Use the command: python copycat.py thepathtoyourtxtfile')
	logger.info('To separate the sentences (for now) use || between every sentence.')
	exit(0)

#logger.info(listArgs)
filename = listArgs[1]							# getting the file path						

try:
	fileContent = open(filename, 'r').read()	# reading the content out of it
	#logger.info(fileContent)					# logging the file content
except IOError:
	logger.info("Can't open the file, something went wrong!")
	exit(0)

splitted = fileContent.split('||')				# splitting it after we can modifiy the splitting character
logger.info(splitted) 

for sentence in splitted:						# going through the array
	logger.info("Next sentence: %s", sentence)
	copyToClip(sentence)
	logger.info("Your sentence was copied...")
	raw_input("Press Enter to copy the next sentence...")

logger.info("There are no more sentences left... bye")




