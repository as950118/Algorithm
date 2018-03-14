#include<stdio.h>

int xcng(int *a, int *b);

int main(){
	
	int n;
	scanf("%d", &n);
	
	int num[n];
	int i,j;
	for(i=0; i<n; i++){
		scanf("%d", &num[i]);
	}
	
	for(i=0; i<n; i++){
		for(j=i; j<n; j++){
			if(num[i]>num[j]){
				xcng(&num[i], &num[j]);
			}
		}
	}
	for(i=0; i<n; i++){
		printf("%d\n", num[i]);
	}
}


int xcng(int *a, int *b){
	int buf;
	buf=*a;
	*a=*b;
	*b=buf;
}
