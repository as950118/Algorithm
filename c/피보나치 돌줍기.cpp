#include<stdio.h>

int main(){
	int n;
	scanf("%d", &n);
	int stone[n+1];
	int div;
	
	stone[2] = 0;
	stone[3] = 1;
	for(int i=4; i<=n+1; i++){
		stone[i]=0;
		div=stone[i]/3;
		if(stone[i]%3==0){
			div--;
		}
		else{
		}
		while(div!=0){
			if(stone[i-div]==1){
				i--;
			}
			else{
				stone[i]=1;
				break;
			}
		}
		
	}
	if(stone[n+1]==1){
		printf("SK");
	}
	else{
		printf("CY");
	}
}
