#include<stdio.h>

int main(){
	int n,i=1,j,k,m;
	scanf("%d", &n);
	//1 7 19 37
	//i=6*j;
	//i=6*j;
	/*
	k=for(j=0; j<n; j++){
		i+=6*j-5;
	};
	*/
	while(1){
		k=1+(i-1)*i*3;
		if(n<=k){
			printf("%d", i);
			break;
		}
		else{
			i++;
		}
		
	}
}
