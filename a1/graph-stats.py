import sys
import pandas

# input from the command line
targetFile = sys.argv[1]

# uses a space as the seperator (so seperates into columns based on the spaces) and no header
data = pandas.read_csv(targetFile, sep = " ", header = None)
# setting the column names
data.columns = ["firstNode", "secondNode"]

# drops the duplicate nodes
nodes = data.stack().drop_duplicates()
# gets the count of how many nodes there are
numNodes = nodes.count()

# gets the nummer of edges by getting the firstNode and counting how many connections in the data
numEdges = data.firstNode.count()

print("#nodes:" + str(numNodes) + " #edges:" + str(numEdges))

# below is to get the degree for the nodes

# stack the columns
listNodes = data.stack()
# getting the values count and resetting the indexes
numNodes = listNodes.value_counts().reset_index()
# mapping to a str
numNodes = numNodes.applymap(str)
# so that there's no space and it has a:b instead of a : b
numNodes = numNodes.apply(lambda x: ':'.join(x), axis=1)
# getting rid of the index and setting to_string so that it prints all of them
numNodesToPrint = numNodes.to_string(index=False)

# get the average node degrees for the graph

# stack the columns
listNodes = data.stack()
# getting the values count and resetting the indexes
numNodes = listNodes.value_counts().reset_index()
# setting the column names
numNodes.columns = ["Node", "NodeDegree"]
#calculates the mean for all the unique nodes to get the avgNodeDegree
numNodes = numNodes.NodeDegree.mean()




# printing statistics
print(numNodesToPrint)
print("avgNodeDegree:" + str(numNodes))
