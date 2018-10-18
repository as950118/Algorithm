#include <stdio.h>

int func(int l, int r);
int min(int a, int b);
long long arr[501][2];
long long dp[501][501];
int main(void) {
	int n;
	int i;
	scanf("%d", &n);



	for(i=0; i<n; i++){
		scanf("%lld %lld", &arr[i+1][0], &arr[i+1][1]);
	}

	func(1, n);
	printf("%lld", dp[1][n]);

	return 0;
}

int min(int a, int b){
	if(a>b){
		return b;
	}
	else{
		return a;
	}
}

int func(int l, int r){
	if(l==r-1){
		return dp[l][r] = arr[l][0] * arr[l][1] * arr[r][1];
	}
	if(l==r){
		return dp[l][r] = 0;
	}
	if(dp[l][r]){
		return dp[l][r];
	}

	dp[l][r] = func(l+1,r) + arr[l][0]*arr[l][1]*arr[r][1];

	for (int i=l+1; i<r; i++){
    	dp[l][r] = min(func(l,i) + func(i+1,r) + arr[l][0]*arr[i][1]*arr[r][1], dp[l][r]);
	}
	return dp[l][r];
}
