#include<stdio.h>

int main(){
	int n,i,j;
	scanf("%d", &n);
	int num[n];
	for(i=0; i<n; i++){
		scanf("%d", &num[i]);
	}
	int buf;
	
	for(j=n-1; j>0; j--){
		for(i=0; i<j; i++){
			if(num[i]>num[i+1]){
				buf=num[i+1];
				num[i+1]=num[i];
				num[i]=buf;
			}
			else{
			}
		}
	}
	
	for(i=0; i<n; i++){
		printf("%d\n", num[i]);
	}
}

