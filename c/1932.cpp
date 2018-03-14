#include<stdio.h>

int main(){
	int n;
	int i,j,k;
	scanf("%d", &n);
	int num[n][n] = {0,};
	int ret[n][n] = {0,};
	
	for(i=0; i<n; i++){
		for(j=0; j<i+1; j++){
			scanf("%d", &num[i][j]);
		}
	}
	
	ret[0][0] = num[0][0];
	for(int i = 0 ; i < n-1 ; i++){
		for(int j=0; j <i + 1 ;j++){
			if( ret[i+1][j] < ret[i][j] + num[i+1][j])
				ret[i+1][j] = ret[i][j] + num[i+1][j];
			if( ret[i+1][j+1] < ret[i][j] + num[i+1][j+1])
				ret[i+1][j+1] = ret[i][j] + num[i+1][j+1];
		}
	}
	
	int max=0;
	for(i=0; i<n; i++){
		if(ret[n-1][i]>max){
			max = ret[n-1][i];
		}
	}
	printf("%d", max);
	
}
