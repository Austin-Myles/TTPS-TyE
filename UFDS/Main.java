/*
	By: facug91
	Name: UnionFindDisjointSet
	Date: 15/10/2014
*/

import java.io.*;
import java.util.*;

public class Main {
	
	static class UFDS {
		ArrayList<Integer> p, rank; //también pueden usarse arreglos estáticos
		
		public UFDS (int size) {
			p = new ArrayList<Integer>();
			rank = new ArrayList<Integer>();
			for (int i=0; i<size; i++) {
				p.add(i);
				rank.add(0);
			}
		}
		
		public int find_set (int i) {
			return (i == p.get(i)) ? i : (p.set(i, find_set(p.get(i))));
		}
		public boolean same_set (int i, int j) {
			return (this.find_set(i) == this.find_set(j));
		}
		public void union_set (int i, int j) {
			if (!same_set(i, j)) {
				int x = find_set(i);
				int y = find_set(j);
				if (rank.get(x) > rank.get(y)) {
					p.set(y, x);
				} else {
					p.set(x, y);
					if (rank.get(x) == rank.get(y)) rank.set(y, y+1);;
				}
			}
		}
	}
	
	public static void main (String[] args) throws IOException {
		//Para poder probar la estructura
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int n;
		System.out.print("Ingrese la cantidad de elementos\n");
		n = in.nextInt();
		UFDS ds = new UFDS(n);
		System.out.print("\nIngrese 0 para unir, seguidos los elementos a unir\n");
		System.out.print("Ingrese 1 para imprimir conjunto, seguido el conjunto a imprimir\n");
		System.out.print("Ingrese 2 para checkear conjuntos, seguido los conjuntos a checkear\n");
		System.out.print("Ingrese -1 para terminar la ejecución\n\n");
		int op, s1, s2;
		System.out.print("Operación a realizar: ");
		op = in.nextInt();
		while (op != -1) {
			switch (op) {
				case 0:
					s1 = in.nextInt();
					s2 = in.nextInt();
					ds.union_set(s1, s2);
					System.out.print("Union completa\n\n");
					break;
				case 1:
					s1 = in.nextInt();
					System.out.print("El elemento "+s1+" pertenece al conjunto "+ds.find_set(s1)+"\n\n");
					break;
				case 2:
					s1 = in.nextInt();
					s2 = in.nextInt();
					if (ds.same_set(s1, s2)) System.out.print("Están en el mismo conjunto\n\n");
					else System.out.print("No están en el mismo conjunto\n\n");
					break;
			}
			System.out.print("Operación a realizar: ");
			op = in.nextInt();
		}
		System.out.print("\n");
		in.close();
	}
}
