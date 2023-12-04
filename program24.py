#graph = a graph data structure is the collection of the node that have data and coonected to other nodes
#eg:insta,facebook
#every relatiionship is the edge from one node to another ,whether u post a photo join a group or liking a page etc.. or new connection is createc for relationsship
#path ,directed graph
#types:null graph,none directed,directed,connected ,discoonmected,regular,compelete,cylic,acyclic,cycle,infinite,simple,multi,sudocode
#wapp ot create simple graph
class SimpleGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = set()
    def insert_node(self,node):
        if node not in self.nodes:
            self.nodes[node]=set()
            print(f"Node {node} inserted.")
        else:
            print(f"Node {node} already exists.")
    def insert_edge(self,node1,node2):
        if node1 in self.nodes and node2 in self.nodes:
            edge=(node1,node2) if node1<node2 else(node2,node1)
            if edge not in self.edges:
                self.edges.add(edge)
                self.nodes[node1].add(node2)
                self.nodes[node2].add(node1)
                print(f"Edge ({node1},{node2})inserted.")
            else:
                  print(f"Edge ({node1},{node2}) already exists.")
        else:
            print("one or both nodes do not exists.")
    def display_graph(self):
        print("Nodes:",list(self.nodes.keys()))
        print("edges:",list(self.edges))
my_graph = SimpleGraph()
while True:
    print("\nGraph Operation:")
    print("1.Insert Node")
    print("2.Insert Edge")
    print("3.Display Graph")
    print("4.Exit")
    choice = int(input("Enter your choice:"))
    if choice ==1:
        node = input("Enter the node:")
        my_graph.insert_node(node)
    elif choice ==2:
        node1= input("Enter the  first node: ")
        node2= input("Enter the  second node: ")
        my_graph.insert_edge(node1,node2)
    elif choice ==3:
        my_graph.display_graph()
    elif choice ==4:
        print(" Exiting the program.")
        break
    else:
        print("Invalid choice.Please enter a valid option.")
    

        

    




                
