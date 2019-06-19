#include<iostream>
#define DEBUG
#define FOR(i, n) for(int i=0; i<n; i++)
using namespace std;

//int min_4(int a, int b, int c, int d){
//	int ret;
//	
//	ret = min(a, b);
//	ret = min(ret, c);
//	ret = min(ret, d);
//	
//	return a+b+c-ret;
//}
//int min_3(int a, int b, int c){
//	int ret;
//	
//	ret = min(a, b);
//	ret = min(ret, c);
//	
//	return a+b-ret;
//}

int main(){
	int n;
	int stair[301]={0,};
	int map[301]={0,};
	int dp[301]={0, };
	int ret=0;
	#ifdef DEBUG
	while(1){
	#endif
	cin>>n;
	
	for(int i=0; i<n; i++){
		cin>>stair[i];
	}
	
	if(n<4){
		cout<<stair[0]+stair[1]+stair[2]+stair[3]<<endl; 
	}
	else{
		dp[0]=stair[0];
		dp[1]=dp[0]+stair[1];
		dp[2]=max(dp[0]+stair[2], stair[1]+stair[2]);
		
		for(int i=3; i<n; i++){
			dp[i] = max(stair[i] + dp[i-2], stair[i] + stair[i-1] + dp[i-3]);
		}
	}
	
	cout<<dp[n-1]<<endl;

	#ifdef DEBUG
	}
	#endif
}
