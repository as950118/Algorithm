#include<stdio.h>

int main(){
	int jum[6];
	int sum=0,i;
	
	for(i=0; i<5; i++){
		scanf("%d", &jum[i]);
		if(jum[i]<40){
			jum[i]=40;
		}
		sum+=jum[i];
	}
	printf("%d", sum/5);
	
}
