/*
	By: facug91
	Name: UnionFindDisjointSet
	Date: 15/10/2014
*/
#include <vector>
#include <iostream>
using namespace std;

struct UFDS {
	vector<int> p, rank; //también pueden usarse arreglos estáticos
	
	UFDS (int size) {
		p.clear(); rank.clear();
		for (int i=0; i<size; i++) {
			p.push_back(i);
			rank.push_back(0);
		}
	}
	
	int find_set (int i) {
		return (i == p[i]) ? i : (p[i] = find_set(p[i]));
	}
	bool same_set (int i, int j) {
		return find_set(i) == find_set(j);
	}
	void union_set (int i, int j) {
		if (!same_set(i, j)) {
			int x = find_set(i);
			int y = find_set(j);
			if (rank[x] > rank[y]) {
				p[y] = x;
			} else {
				p[x] = y;
				if (rank[x] == rank[y]) rank[y]++;
			}
		}
	}
};

int main () {
	//Para poder probar la estructura
	int n;
	cout<<"Ingrese la cantidad de elementos"<<endl;
	cin>>n;
	UFDS ds = UFDS(n);
	cout<<endl<<"Ingrese 0 para unir, seguidos los elementos a unir"<<endl;
	cout<<"Ingrese 1 para imprimir conjunto, seguido el conjunto a imprimir"<<endl;
	cout<<"Ingrese 2 para checkear conjuntos, seguido los conjuntos a checkear"<<endl;
	cout<<"Ingrese -1 para terminar la ejecución"<<endl<<endl;
	int op, s1, s2;
	cout<<"Operación a realizar: ";
	while (cin>>op, op != -1) {
		switch (op) {
			case 0:
				cin>>s1>>s2;
				ds.union_set(s1, s2);
				cout<<"Union completa"<<endl<<endl;
				break;
			case 1:
				cin>>s1;
				cout<<"El elemento "<<s1<<" pertenece al conjunto "<<ds.find_set(s1)<<endl<<endl;
				break;
			case 2:
				cin>>s1>>s2;
				if (ds.same_set(s1, s2)) cout<<"Están en el mismo conjunto"<<endl<<endl;
				else cout<<"No están en el mismo conjunto"<<endl<<endl;
				break;
		}
		cout<<"Operación a realizar: ";
	}
	cout<<endl;
	return 0;
}
