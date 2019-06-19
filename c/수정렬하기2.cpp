#include<stdio.h>

int main(){
	int n,i,j;
	scanf("%d", &n);
	int num[n+1];
	for(i=1; i<n+1; i++){
		scanf("%d", &num[i]);
	}
	int buf, max;
	
	for(i=n+1; i<2; i--){
		if(num[i]>num[i/2]){
			buf = num[i];
			num[i] = num[i+1];
			num[i+1] = buf;
		}
		else{
		}
	}
	
	for(i=1; i<n+1; i++){
		printf("%d\n", num[i]);
	}
}

