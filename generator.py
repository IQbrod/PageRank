import sys
import random
import math

class ArgError(Exception):
	pass

gEXT = ".txt"

# Checking Arguments size
if (len(sys.argv) != 3):
	raise ArgError("usage : generator.py [Page] [FileName]")

# Getting Arguments
gPage = sys.argv[1]
gFName = sys.argv[2]

# Conformity of Arguments
try:
	gPage = int(gPage)
except:
	raise ArgError("[Page] must be an integer")

if not ((gFName.endswith(gEXT) and ("." not in gFName[:-4])) or ("." not in gFName)):
	raise ArgError("[FileName] has unsupported extension => use "+gEXT)
if ("." not in gFName):
	gFName = gFName + gEXT

gFName = "files/" + gFName

## MAIN ##
random.seed()

with open(gFName, "w") as graph:
	# PAGE AMOUNT
	graph.write("%s\n" % gPage)
	for i in range(0,gPage):
		# PAGE ID
		graph.write("%s" % i)
		# OUT PAGES
		for j in range(0,gPage):
			if i!=j: # Ignore self redirect
				p = random.randint(1,gPage)
				if p <= int(math.log(gPage,2)):
					graph.write(" %s" % j)
		graph.write("\n")
