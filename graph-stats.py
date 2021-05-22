import sys
import pandas

#cmdln inputs for file
targetFile = sys.argv[1]

#reads the csv file and seperates into columns by spaces
data = pandas.read_csv(targetFile, sep = " ", header = None)
#adds headers the the columns
data.columns = ["firstNode", "secondNode"]

# drops the duplicate nodes
nodes = data.stack().drop_duplicates()
# gets the count of how many nodes there are
numNodes = nodes.count()

# gets the nummer of edges by getting the firstNode and counting how many connections in the data
numEdges = data.firstNode.count()


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
numNodes.columns = ["Nodes", "NodesDegree"]
#calculates the mean for all the unique nodes to get the avgNodeDegree
numNodes = numNodes.NodesDegree.mean()




# printing statistics
print(numNodesToPrint)
print("avgNodeDegree:" + str(numNodes))



