#include<stdio.h>

int main(){
	int m[9];
	int i,j,k;
	for(i=0; i<8; i++){
		scanf("%d", &m[i]);
	}
	k=m[0]-m[1];
	for(i=1; i<7; i++){
		if(k!=1 && k!=-1){
			printf("mixed");
			return 0;
		}
		j=m[i]-m[i+1];
		if(k!=j){
			printf("mixed");
			return;
		}
	}
	if(k==-1){
		printf("ascending");
	}
	else if(k==1){
		printf("descending");
	}
}
