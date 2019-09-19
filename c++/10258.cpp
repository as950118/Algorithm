#include <iostream>
#include <cstring>
#include <cmath>
#include <queue>
using namespace std;

int arr;
int n;
int dp;

int func(cur, ret){
	if(cur == 0)
		return ret
	
	if
	if(arr[n])
		func( ret+1);
}

int set_arr(){
	int tmp;
	cin>>tmp;
	int i = 0;
	while(++i){
		if(tmp%10)
			arr |= 1<<(i-1);
		if( (tmp / 10) == 0 ) break;
		tmp = tmp/10;
	}
	n = i;
	return 1;
}

int set_dp(){
	for(int i=1; i<=n; i++){
		if(arr[i])
			dp |= (1<<(i-1));
	}
	cout<<dp<<endl;
}

int main() {
	int t;
	cin>>t;
	while(t--){
		arr=0;
		dp=0;
		n=0;
		set_arr();
		set_dp();
	}
	return 0;
}
