#include<stdio.h>

int main(){
	int n;
	scanf("%d", &n);
	
	int stone[1001];
	
	stone[1] = 1;
	stone[2] = 0;
	stone[3] = 1;
	stone[4] = 1;
	
	for(int i=5; i<=n; i++){
		if(stone[i-1]==1 && stone[i-3]==1 && stone[i-4]==1){
			stone[i]=0;
		}
		else{
			stone[i]=1;
		}
	}
	
	if(stone[n]==1){
		printf("SK");
	}
	else{
		printf("CY");
	}
}
