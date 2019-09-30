#include <iostream>
using namespace std;

int main() {
	int a,b,n,w;
	cin>>a>>b>>n>>w;
	//a<b·Î Á¤·Ä
	int tmp = a;
	a = (a<b ? a:b);
	b = (a<b ? b:tmp);

	if(a == b){
		if(n==2){
			cout<<1<<" "<<1<<endl;
			return 0;
		}
		cout<<-1<<endl;
		return 0;
	}

	if(a*n==w || b*n==w){
		cout<<-1<<endl;
		return 0;
	}

	if(w<a*n){
		cout<<-1<<endl;
		return 0;
	}
    
	int dif_w_a = w - (a*n);
	int dif_a_b = b-a;
	
    if(dif_w_a%dif_a_b == 0 && dif_w_a/dif_a_b <n && 0<dif_w_a/dif_a_b){
		if(a==tmp){
			cout<<n-dif_w_a/dif_a_b<<" "<<dif_w_a/dif_a_b<<endl;
			return 0;
		}
		cout<<dif_w_a/dif_a_b<<" "<<n-dif_w_a/dif_a_b<<endl;
		return 0;
	}
	cout<<-1<<endl;
	return 0;
}
