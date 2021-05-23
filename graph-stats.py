import sys
import pandas

# input from the command line
targetFile = sys.argv[1]

# uses a space as the seperator (so seperates into columns based on the spaces)
data = pandas.read_csv(targetFile, sep = " ")

# setting the column names
data.columns = ['firstNode', 'secondNode']

# getting the nodes and stacking them
nodes = data.stack()

# setting variable for the first node
first = data.firstNode

# drops the duplicate nodes
noDup = nodes.drop_duplicates()

# gets the count of how many nodes there are
numNodes = noDup.count()

# gets the nummer of edges by getting the firstNode and counting how many connections in the data
numEdges = first.count()

print("#nodes:" + str(numNodes) + " #edges:" + str(numEdges))

# get the average node degrees for the graph

# getting the values count and resetting the indexes
numNodes = nodes.value_counts().reset_index()
# setting the column names. Have to reset index first to do this
numNodes.columns = ['node', 'degree']
#calculates the mean for all the unique nodes to get the avgNodeDegree
numNodesAvg = numNodes.degree.mean()

# below is to get the degree for the nodes

# mapping to a str
numNodes = numNodes.applymap(str)
# so that there's no space and it has a:b instead of a : b (combining two columns of text)
numNodes = numNodes.apply(lambda x: ':'.join(x), axis=1)
# getting rid of the index and setting to_string so that it prints all of them
numNodesToPrint = numNodes.to_string(index=False)


# printing statistics
print(numNodesToPrint)
print("avgNodeDegree:" + str(numNodesAvg))
