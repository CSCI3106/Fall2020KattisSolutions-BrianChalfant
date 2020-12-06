/*
# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
*/

import java.util.BitSet;
import java.util.Scanner;

public class primesieve {

public static final Scanner sc = new Scanner(System.in);

    public static void main(String[] args){
        int n = sc.nextInt();
        int q = sc.nextInt();
        sc.nextLine();
        BitSet sieve;
        int numPrimes;
        sieve = new BitSet(n); // use bitset otherwise will give Memory Exceeded Error
        sieve.set(1, n, true);
        numPrimes = n - 1;

        // Sieve
        for (int p = 2; p <= (int) Math.ceil(Math.sqrt(n)); p++) {
            if (sieve.get(p - 1)) {
                for (int j = p * p; j <= n; j += p) {
                    if (sieve.get(j - 1)) {
                        numPrimes--;
                    }
                    sieve.set(j - 1, false);
                }
            }
        }
        System.out.println(numPrimes);
    for(int i=0; i<q; i++){
        int query = sc.nextInt();
        System.out.println(sieve.get(query-1) ? 1: 0);
        sc.nextLine();
    }

    }
}