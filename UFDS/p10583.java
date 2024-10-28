import java.io.*;
import java.util.*;

public class p10583 {
	//COMPILATION ERROR
	static class UFDS {
		ArrayList<Integer> p, rank, belief; //también pueden usarse arreglos estáticos
		
		public UFDS (int size) {
			p = new ArrayList<Integer>();
			rank = new ArrayList<Integer>();
            belief = new ArrayList<Integer>();
			for (int i=0; i<size; i++) {
				p.add(i);
				rank.add(0);
                belief.add(1);
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
                    belief.set(y, 0);
				} else {
					p.set(x, y);
                    belief.set(x, 0);
					if (rank.get(x) == rank.get(y)) rank.set(y, rank.get(y) + 1);;
				}
			}
		}
        public int get_sum_belief() {
			int sum = 0;
			for (int b : belief) {
				sum += b;
			}
			return sum;
        }
	}
	
    public static void main (String[] args) throws IOException {
    Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    int c, n, m, s1, s2;
	c = 1;
	n = in.nextInt();
	m = in.nextInt();
	String output = "";
    while(n != 0 && m != 0) {
        UFDS ds = new UFDS(n);
        for(int i = 0; i < m; i++) {
            s1 = in.nextInt() - 1;
            s2 = in.nextInt() - 1;
            ds.union_set(s1, s2);
        }
		output += "Case " + c + ": " + ds.get_sum_belief() + "\n";
        //System.out.println("Case " + c + ": " + ds.get_sum_belief());
		c++;
		n = in.nextInt();
        m = in.nextInt();
    }
	System.out.print(output);
    in.close();
    }
}
