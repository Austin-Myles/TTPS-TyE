import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;

public class p11690 {

    	//COMPILATION ERROR
	
    
    static class UFDS {
		ArrayList<Integer> p, rank, balance; //también pueden usarse arreglos estáticos
		
		public UFDS (int size) {
			p = new ArrayList<Integer>();
			rank = new ArrayList<Integer>();
            balance = new ArrayList<Integer>();
			for (int i=0; i<size; i++) {
				p.add(i);
				rank.add(0);
                balance.add(0);
			}
		}
		
		public int find_set (int i) {
			return (i == p.get(i)) ? i : (p.set(i, find_set(p.get(i))));
		}
		public boolean same_set (int i, int j) {
			return (this.find_set(i) == this.find_set(j));
		}
        public void union_set(int i, int j) {
            if (!same_set(i, j)) {
                int x = find_set(i);
                int y = find_set(j);

                // Une los dos conjuntos y actualiza el balance total
                if (rank.get(x) > rank.get(y)) {
                    p.set(y, x);
                    balance.set(x, balance.get(x) + balance.get(y)); // Suma los balances
                } else {
                    p.set(x, y);
                    balance.set(y, balance.get(x) + balance.get(y)); // Suma los balances
                    if (rank.get(x).equals(rank.get(y))) {
                        rank.set(y, rank.get(y) + 1);
                    }
                }
            }
        }

        public int get_balance(int i) {
            return balance.get(find_set(i)); // Devuelve el balance del conjunto al que pertenece i
        }

        public void print_set(int i){
            System.out.println(rank.get(i));
        }
	}

    public static void main (String[] args) throws IOException {
        		//Para poder probar la estructura
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int r, n, m, bal, s1, s2;
        r = in.nextInt();
        for(int j = 0; j < r; j++) {
            n = in.nextInt();
            m = in.nextInt();
            UFDS ds = new UFDS(n);
            for(int i = 0; i < n; i++) {
                bal = in.nextInt();
                ds.balance.set(i, bal);
            }
            for(int i = 0; i < m; i++) {
                s1 = in.nextInt();
                s2 = in.nextInt();
                ds.union_set(s1, s2);
            }
            
            boolean possible = true;
            for (int i = 0; i < n; i++) {
                if (ds.get_balance(i) != 0) {
                    possible = false;
                    break;
                }
            }

            if (possible) {
                System.out.println("POSSIBLE");
            } else {
                System.out.println("IMPOSSIBLE");
            }
        }

        in.close();
    }
}
