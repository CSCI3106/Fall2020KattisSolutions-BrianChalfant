/*
# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
*/
import java.io.*;
import java.util.*;

public class shortestPath {
    static boolean debug = false;                // for tracing

    public static class Edge {
        public Vertex adj;
        public int weight;

        public Edge(Vertex adj, int weight) {
            this.adj = adj;
            this.weight = weight;
        }
    }


    public static class Vertex implements Comparable<Vertex> {

        public final int name;
        public boolean   inTree;           // inTree[u] is true when a shortest path to u has found
        public ArrayList<Edge> adjacent;
        //  public double minDis = Double.POSITIVE_INFINITY;  // use if edge weights are not integers
        public int minDis = Integer.MAX_VALUE;

        public Vertex(int name) {
            this.name = name;
            inTree = false;
            adjacent = new ArrayList<>();  // adjacency list for this node (all nodes connected to it by an edge)
        }
        @Override
        public int compareTo(Vertex other) {
            // return Double.compare(this.minDis, other.minDis);   // use if edges are not integers
            return Integer.compare(this.minDis, other.minDis);
        }
    }


    public static void main(String[]  args) throws IOException {

        Scanner in = new Scanner(System.in);
        int N = in.nextInt();                    // number of nodes in graph (# of cities)
         // loop thru problems
        int E = in.nextInt();                // number of edges
        int numQueries  = in.nextInt();      // number of destination nodes (# of queries)
        int s           = in.nextInt();      // start node
        while (N + E + numQueries + s != 0) {
            int[] queries = new int[numQueries];  // array of node numbers to query
            Vertex[] vertices = new Vertex[N];   // nodes in array to create graph

            for (int j=0; j<N; j++)
                vertices[j] = new Vertex(j);     // create vertices

            int u,v,w;                           // edges u-v and associated weight
            for (int e = 0; e<E; e++) {          // input edges
                u = in.nextInt();
                v = in.nextInt();
                w = in.nextInt();
                Edge edge = new Edge(vertices[v], w);
                vertices[u].adjacent.add(edge);  // add edge u-v (digraph: no v-u unless specified)
            }

            for (int q = 0; q<numQueries;q++){
                queries[q] = in.nextInt();
            }

            //int s = in.nextInt();                // starting node
            dijkstra(vertices[s], vertices[vertices.length-1]);  // find one or all shortest paths (modify Dijkstra to choose)

            for(int i : queries){
                if (vertices[i].minDis == Integer.MAX_VALUE)
                    System.out.println("Impossible");
                else
                    System.out.println(vertices[i].minDis);
            }
            System.out.println();
            N = in.nextInt();                    // number of nodes in graph (# of cities)
            E = in.nextInt();                // number of edges
            numQueries  = in.nextInt();      // number of destination nodes (# of queries)
            s           = in.nextInt();      // start node

        }
    }


    public static void dijkstra(Vertex source, Vertex dest) {
        // argument dest is irrelvant if finding paths to all nodes
        source.minDis = 0;
        PriorityQueue<Vertex> vertexQueue = new PriorityQueue<>();
        vertexQueue.add(source);

        while(!vertexQueue.isEmpty()) {
            Vertex u = vertexQueue.poll();
            if (debug) System.out.println("selected from queue node: " + u.name + "("+ u.minDis + ")");
            u.inTree = true;
            //if(u == dest) return; // commented ==> find paths to all nodes

            for(Edge e : u.adjacent) {
                Vertex v = e.adj;
                if (!v.inTree) {
                    if (debug) System.out.println("    adj: " + v.name + "("+ v.minDis + ")");
                    int distToVthroughU = u.minDis + e.weight;
                    if(distToVthroughU < v.minDis) {
                        vertexQueue.remove(v);       // remove it to update priority and reinsert
                        v.minDis = distToVthroughU;
                        if (debug) System.out.println("       updating " + v.name + " to: " + v.minDis);
                        vertexQueue.add(v);
                    }
                }
            }
        }
    }

}