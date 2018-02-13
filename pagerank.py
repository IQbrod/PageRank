import math

#ADJ => Adjacency Matrix
#LMB => Visiting Neighbor Probability
#RND => Rounding value
def getTransitionMatrix(adj,lmb,rnd):
	transMatrix = []
	for i in range(0,len(adj)):	
		sum = 0
		line = []
		#Calculus of sum
		for j in range(0,len(adj)):
			sum += adj[i][j]
		for j in range(0,len(adj)):
			#Dead-end page
			if sum == 0:
				line.append(1.0/len(adj))
			#Linked page
			else:
				line.append( round((lmb*adj[i][j]/sum) + (1.0-lmb)/len(adj), rnd) )
		transMatrix.append(line)
	return transMatrix

#TRS => Transition Matrix
#RND => Rounding stop value
#CHECK RND IS AT LEAST EQUAL TO THE PRECISION USED TO CREATE TRANSITION MATRIX => TO GET A REACHABLE PRECISION
def getPageRank(trs,rnd):
	old = []
	#Init Rank0	
	for i in range(0,len(trs)):
		old.append( (1.0/len(trs)) )
	new = []
	#Init Rank1
	for j in range(0,len(trs)):
		sum = 0
		for i in range(0,len(trs)):
			sum += trs[i][j] * old[i]
		new.append(sum)
	#Ri+1 - Ri => Diff
	diff = [(a_elt - b_elt) **2 for a_elt, b_elt in zip(new, old)]
	sm = 0
	for i in diff:
		sm += i
	rnk=1
	print ""
	while ( math.sqrt(sm) > 10**(-rnd) ):
		rnk += 1		
		#Rank i		
		old = new
		#Rank i+1		
		new = []
		for j in range(0,len(trs)):
			sum = 0
			for i in range(0,len(trs)):
				sum += trs[i][j] * old[i]
			new.append(sum)
		#Diff
		diff = [(a_elt - b_elt) **2 for a_elt, b_elt in zip(new, old)]
		sm = 0
		for i in diff:
			sm += i
		print "Diff",rnk,":",diff
		

	return new



gFileName = raw_input("Quel fichier souhaitez vous parser: ")
gFile = open(gFileName,"r")
# Parsing File
nbEtat = int(gFile.readline())
gTransi = []
for i in range(0,nbEtat):
	ligne = gFile.readline().split(" ")
	ligneint = []
	for j in range(1,len(ligne)): 
		ligneint.append(int(ligne[j]))
	gTransi.append(ligneint)
# Create Adjacency Matrix
adjMatrix = []
for i in range(0,nbEtat):
	new = []
	for j in range(0,nbEtat):
		if j in gTransi[i]:
			new.append(1)
		else:
			new.append(0)
	adjMatrix.append(new)
# Print Adjacency Matrix
print ""
print "Adjacency Matrix [",len(adjMatrix),"x",len(adjMatrix[0]),"]:"
for i in range(0,nbEtat):
	print adjMatrix[i]

### Specify Precision : 10 ^ -(prc)
prc = 4
### Specify Lambda
lmd = 0.85
# Create Transition Matrix
print ""
tMatrix = getTransitionMatrix(adjMatrix,lmd,prc*2)
print "Transition Matrix [",len(tMatrix),"x",len(tMatrix[0]),"]:"
for i in range(0,nbEtat):
	print tMatrix[i]

#Create Page Rank
pRank = getPageRank(tMatrix,prc)
print ""
print "Page Rank:",pRank
print "% Rank:",[round(100*i,2) for i in pRank]
