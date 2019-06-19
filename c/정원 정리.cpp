#include<stdio.h>

int main(){
	int n, m;
	scanf("%d %d", &n,&m);
	
	int leaf[n+1][n+1];
	int j=0, k=0;
	while(k!=n){
		scanf("%d %d", &j,&k);
		leaf[j][k]=1;
	}
	
	
}
