/*
# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
*/
import java.util.*;

public class bookclub {
    public static Scanner scanner = new Scanner(System.in);
    static Vector<Vector<Integer>> adjList = new Vector<>();
    static boolean[] visited;
    static int[] match;
    private static int Aug(int left) {
        if(visited[left]) return 0;
        visited[left] = true;
        Iterator it = adjList.get(left).iterator();
        while(it.hasNext()) {
            Integer right = (Integer)it.next();
            if(match[right] == -1 || Aug(match[right]) == 1) {
                match[right] = left;
                return 1;
            }
        }
        return 0;
    }
    public static void main(String[] args) {

        int V = scanner.nextInt();
        int E = scanner.nextInt();
        for(int i = 0; i < V; i++) adjList.add(new Vector<>());
        for(int i=0; i<E;i++) {
            adjList.get(scanner.nextInt()).add(scanner.nextInt());
        }

        int MCBM = 0;
        match = new int[V];
        Arrays.fill(match, -1);
        for(int i = 0; i < V; i++) {
            visited = new boolean[V];
            MCBM += Aug(i);
        }

        if(MCBM == V) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}