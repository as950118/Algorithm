#include <iostream>
#include <algorithm>
using namespace std;
const int INF = 1<<21;

struct segtree{
	int start;
	long long arr[INF], lazy[INF];
	
	//생성자 
	segtree(){
		start = INF/2;
		fill(arr, arr+INF, 0);
		fill(lazy, lazy+INF, 0);
	}
	
	//leaf를 먼저 입력후 전체 segment tree 구축 
	void construct(){
		for(int i=start-1; i>0; i--){
			arr[i] = arr[i*2] + arr[i*2+1];
		}
	}
	
	//구간(ns, ne)인 node의 lazy값을 전파
	void propagate(int node, int ns, int ne){
		//lazy가 존재하면
		if(lazy[node]){
			//leaf node가 아니면 자식들에게 lazy 전파 
			if(node < start){
				lazy[node*2] += lazy[node];
				lazy[node*2 + 1] += lazy[node];
			}
			//해당하는 값만큼 더하기 
			arr[node] += lazy[node] * (ne-ns);
			lazy[node] = 0;
		}
	}
	
	//구간 (s, e)에 k 더하기 
	void add(int s, int e, int k){
		return add(s, e, k, 1, 0, start);
	}
	
	void add(int s, int e, int k, int node, int ns, int ne){
		//전파 
		propagate(node, ns, ne);
		
		if(e <= ns || ne <= s)
			return;
		if(s <= ns && ne <= e){
			//lazy 부여후 전파 
			lazy[node] += k;
			propagate(node, ns, ne);
			return; 
		}
		
		int mid = (ns + ne) / 2;
		add(s, e, k, node*2, ns, mid);
		add(s, e, k, node*2 + 1, mid, ne);
		
		//마지막에 자식들의 값을 사용해 자신의 값 갱신
		arr[node] = arr[node*2] + arr[node*2 + 1];
	}
	
	//구간 (s, e)의 합 구하기 
	long long sum(int s, int e){
		return sum(s, e, 1, 0, start);
	}

	long long sum(int s, int e, int node, int ns, int ne){
		//전파
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
