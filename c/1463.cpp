#include<iostream>
#define DEBUG_
using namespace std;

int cal[1000001];

int main(){
	int n;
	#ifdef DEBUG
	while(1){
	#endif
	cin>>n;
	
	cal[1]=0;
	for(int i=2; i<=n; i++){
		cal[i] = cal[i-1] + 1;
		if(i%2 == 0){
			cal[i] = min(cal[i], cal[i/2] + 1);
		}
		if(i%3 == 0){
			cal[i] = min(cal[i], cal[i/3] + 1);
		}
	}
	cout<<cal[n]<<endl;
	#ifdef DEBUG
	}
	#endif
}
