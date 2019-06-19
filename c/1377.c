#include<stdio.h>

int main(){
	int N;
	
	int i,j,temp;
	int *A;
	scanf("%d", &N);
	A=malloc((N+1)*sizeof(int));
	for(i=1; i<=N; i++){
		scanf("%d", &A[i]);
	}
	printf("%d\n",i);
}
