#include<stdio.h>

int num=0;

int fun(int a, int b, int n){
	if(a<=n/b){
		num++;
		fun(a*b, b, n);
	}
	else{
		return 0;
	}
}

int main(){
	long long i,j,k,l,n,m;
	
	scanf("%d %d", &m, &n);
	
	long long prime[100001]={0 ,}; //소수 == 0, !소수 == 1
	
	

	for(i=2; i<=n; i++){
		
		if(prime[i]==1){
			continue;
		} 
		
		for(j=i*2; j<=n; j+=i){
			prime[j]=1;
		}
	}
	for(i=2; i<=n; i++){
		if(i*i>n){
			break;
		}
		else if(prime[i]==0){
			fun(i, i, n);
		}
	}
	printf("%d", num);
}
