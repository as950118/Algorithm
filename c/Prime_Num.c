#include<stdio.h>

int main(){
	int i,j,k,l,n,m;
	int prime[100001]={0 ,}; //소수 == 0, 소수 != 1
	scanf("%d", &n);
	for(i=2; i<n; i++){
		
		if(prime[i]==1){
			continue;
		} 
		
		for(j=i*2; j<n; j+=i){
			prime[j]=1;
		}
	}
	for(i=2; i<n; i++){
		if(prime[i]==0){
		
			printf("%d\n", i);
		}
	}
}
