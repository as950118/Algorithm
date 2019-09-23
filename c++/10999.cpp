#include <iostream>
#include <algorithm>
using namespace std;
const int INF = 1<<21;

struct segtree{
	int start;
	long long arr[INF], lazy[INF];
	
	//������ 
	segtree(){
		start = INF/2;
		fill(arr, arr+INF, 0);
		fill(lazy, lazy+INF, 0);
	}
	
	//leaf�� ���� �Է��� ��ü segment tree ���� 
	void construct(){
		for(int i=start-1; i>0; i--){
			arr[i] = arr[i*2] + arr[i*2+1];
		}
	}
	
	//����(ns, ne)�� node�� lazy���� ����
	void propagate(int node, int ns, int ne){
		//lazy�� �����ϸ�
		if(lazy[node]){
			//leaf node�� �ƴϸ� �ڽĵ鿡�� lazy ���� 
			if(node < start){
				lazy[node*2] += lazy[node];
				lazy[node*2 + 1] += lazy[node];
			}
			//�ش��ϴ� ����ŭ ���ϱ� 
			arr[node] += lazy[node] * (ne-ns);
			lazy[node] = 0;
		}
	}
	
	//���� (s, e)�� k ���ϱ� 
	void add(int s, int e, int k){
		return add(s, e, k, 1, 0, start);
	}
	
	void add(int s, int e, int k, int node, int ns, int ne){
		//���� 
		propagate(node, ns, ne);
		
		if(e <= ns || ne <= s)
			return;
		if(s <= ns && ne <= e){
			//lazy �ο��� ���� 
			lazy[node] += k;
			propagate(node, ns, ne);
			return; 
		}
		
		int mid = (ns + ne) / 2;
		add(s, e, k, node*2, ns, mid);
		add(s, e, k, node*2 + 1, mid, ne);
		
		//�������� �ڽĵ��� ���� ����� �ڽ��� �� ����
		arr[node] = arr[node*2] + arr[node*2 + 1];
	}
	
	//���� (s, e)�� �� ���ϱ� 
	long long sum(int s, int e){
		return sum(s, e, 1, 0, start);
	}

	long long sum(int s, int e, int node, int ns, int ne){
		//����
		propagate(node, ns, ne);
		
		if(e <= ns || ne <= s)
			return 0;
		if(s <= ns & ne <= e)
			return arr[node];
			
		int mid = (ns+ne)/2;
		return sum(s, e, node*2, ns, mid) + sum(s, e, node*2 + 1, mid, ne);
	}
}segtree;

int main(){
	int n,m,k;
	cin>>n;
	cin>>m;
	cin>>k;
	
	struct segtree st;
	
	for(int i=0; i<n; i++){
		cin>>*(st.arr+st.start+i);
	}
	st.construct();
	
	int a,b,c,d, ret;
	for(int i=0; i<m+k; i++){
		cin>>a;
		if(a==1){
			cin>>b;
			cin>>c;
			cin>>d;
			st.add(b-1, c, d);
		}
		else{
			cin>>b;
			cin>>c;
			ret = st.sum(b-1, c);
		}
		cout<<ret<<endl;
	}
}
