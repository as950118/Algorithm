#include<stdio.h>

int main(){
	unsigned long long n;
	scanf("%d", &n);
	unsigned long long pib1,pib2,pib3;
	pib1=0;
	pib2=1;
	for(int i=2; i<n+1; i++){
		pib3=pib1+pib2;
		pib1=pib2;
		pib2=pib3;
	}
	
	printf("%d", pib3%1000000);
	return 0;
}
