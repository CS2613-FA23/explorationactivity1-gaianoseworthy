import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os.path

print("Welcome to the NetwokX Demonstrator!")
while(True):
    decision = -1
    while(decision not in [1, 2, 0]):
        if(decision != -1):
            print("Input not recognized, pelase try again!")
        decision = input("Pick your desired option:\n1. Demonstrate a few NetworkX graphs\n2. Get network details using NetworkX\nq. Quit\n")

        if(decision == 'q'):
            decision = 0
        elif(decision.isdigit()):
            decision = int(decision)

    if(decision == 1):
        print("Generating 4 major graph types! Each will have 15 nodes (Barbell will have 14).")
        ba = nx.barabasi_albert_graph(15, 3)
        er = nx.erdos_renyi_graph(15, 3/15)
        bb = nx.barbell_graph(7, 1)
        ws = nx.watts_strogatz_graph(15, 3, 0.5)

        fig, axs = plt.subplots(2,2)

        nx.draw_kamada_kawai(ba, ax=axs[0,0], node_size = 5)
        axs[0,0].set_title("Barabasi Albert")

        nx.draw_kamada_kawai(er, ax=axs[0,1], node_size = 5)
        axs[0,1].set_title("Erdos Renyi")

        nx.draw_kamada_kawai(bb, ax=axs[1,0], node_size = 1)
        axs[1,0].set_title("Barbell")

        nx.draw_kamada_kawai(ws, ax=axs[1,1], node_size = 5)
        axs[1,1].set_title("Watts Strogatz")

        plt.show()

        print("Graph Stats:\n1. Barabasi Albert - Average of 3 connections per node")
        print("2. Erdos Renyi - Connectivity percentage of 10%")
        print("3. Barbell - Distance of 2 between each clump")
        print("4. Watts Strogatz - Average of 3 connections with a rewiring of 50%\n")

    elif(decision == 2):
        readflag = 0
        decision = input("Would you like to import a network? (y/n): ")
        while decision not in ["y", "n"]:
            decision = input("Input not recognized. Please try again: ")

        g = 0
        if(decision == "y"):
            decision = input("Please input file path: ")
            while(not os.path.isfile(decision)):
                decision = input("File not found. Please try again: ")
            g = nx.read_edgelist(path = decision, delimiter = ":")
        else:
            decision = input("Please select a network generation type:\n1. Barabasi Albert\n2. Erdos Renyi\n3. Barbell\n4. Watts Strogatz\n")
            if(decision.isdigit()):
                decision = int(decision)

            while decision not in [1,2,3,4]:
                if(decision == "q"):
                    break
                elif(not decision.isdigit()):
                    decision = input("Input must be a digit or q. Please try again: ")
                else:
                    decision = int(decision)
                    decision = input("Input not recognized. Please try again: ")

            if(decision == 1):
                nodes = input("Barabasi Albert chosen! Please input number of nodes: ")
                while(not nodes.isdigit() and int(nodes) < 1):
                    nodes = input("Error, please enter a positive integer: ")

                conn = input("Please input average number of connections per node: ")
                while(not conn.isdigit() and int(conn) < 0):
                    conn = input("Error, please enter a positive integer: ")

                g = nx.barabasi_albert_graph(int(nodes), int(conn))

            elif(decision == 2):
                nodes = input("Erdos Renyi chosen! Please input number of nodes: ")
                while(not nodes.isdigit() and int(nodes) < 1):
                    nodes = input("Error, please enter a positive integer: ")

                conn = input("Please input percent chance for an edge between any two nodes: ")
                while(not conn.isdigit() and float(conn) <= 1/nodes):
                    conn = input("Error, please enter a positive number: ")
                if(float(conn) > 1):
                    conn = 1

                g = nx.erdos_renyi_graph(int(nodes), float(conn))

            elif(decision == 3):
                nodes = input("Barbell chosen! Please input number of nodes per Barbell group: ")
                while(not nodes.isdigit() and int(nodes) < 1):
                    nodes = input("Error, please enter a positive integer: ")

                conn = input("Please input number of nodes between Barbell groups: ")
                while(not conn.isdigit() and int(conn) < 0):
                    conn = input("Error, please enter a positive integer: ")

                g = nx.barbell_graph(int(nodes), int(conn))

            else:
                nodes = input("Watts Strogatz chosen! Please input number of nodes: ")
                while(not nodes.isdigit() and int(nodes) < 1):
                    nodes = input("Error, please enter a positive integer: ")

                conn = input("Please input average number of connections for each node:")
                while(not conn.isdigit() and int(conn) < 1):
                    conn = input("Error, please enter a positive integer: ")

                rew = input("Please input percent chance of rewiring per edge: ")
                while(not rew.isdigit() and float(rew) < 0):
                    rew = input("Error, please enter a positive number: ")

                if(float(rew) > 1):
                    rew = 1

                g = nx.watts_strogatz_graph(int(nodes), int(conn), float(rew))

        if(not nx.is_connected(g)):
            print("Graph is not connected! No statistics can be calculated.")
        else:
            print("Generating graph details...")
            aspl = nx.average_shortest_path_length(g)
            print("Average Shortest Path Length: ", aspl)

            clus = nx.average_clustering(g)
            print("Average Clustering Coefficient: ", clus)

            conn = nx.average_node_connectivity(g)
            print("Average Node Connectivity: ", conn)

            wie = nx.wiener_index(g)
            print("Wiener Index: ", wie)

            print("Drawing graph!")
            nx.draw(g)
            plt.show()

            decision = input("Would you like to save the network in a text file? (y/n): ")
            while decision not in ["y", "n"]:
                decision = input("Input not recognized. Please try again: ")

            if(decision == "y"):
                nx.write_edgelist(g, path = "network.txt")
                print("Network saved as network.txt")

        print()

    else:
        print("Goodbye!")
        break
