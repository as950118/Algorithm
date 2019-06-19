#include<stdio.h>



int main(){
	int n;
	int i,j;
	scanf("%d", &n);
	
	int arr1[n];
	int arr2[n];
	
	int ARR1[n][n];
	int ARR2[n][n];
	
	int ARR[n][n];
	
	for(i=0; i<n; i++){
		scanf("%d", &arr1[i]);
	}
	
	for(i=0; i<n; i++){
		scanf("%d", &arr2[i]);
	}
	
	for(i=0; i<n; i++){
		for(j=0; j<n; j++){
			if(arr1[i]%2==1 || arr2[i]%2==1){
				ARR[i][n-1-j]=1;
				arr1[i]/=2;
				arr2[i]/=2;
			}
			else{
				ARR[i][n-1-j]=0;
				arr1[i]/=2;
				arr2[i]/=2;
			}
		}
	}
	
	
	
	
	for(i=0; i<n; i++){
		for(j=0; j<n; j++){
			if(ARR[i][j]==1){
				printf("#");
			}
			else{
				printf(" ");
			}
		}
		printf("\n");
	}
	
}
