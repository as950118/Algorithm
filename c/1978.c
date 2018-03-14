#include<stdio.h>
//3 5 7 11 13 17 19 23 29 31 37 41 43 47 
int main(){
	int n;
	int i,j,k=0;
	scanf("%d", &n);
	int a[n];
	while(n){
		scanf("%d", &a[n]);
		i=2;
		j=0;
		while(1){
			if(a[n]==1){
				j=0;
				break;
			}
			if(a[n]==2){
				j=1;
				break;
			}
			if(i==1000){
				j=1;
				break;
			}
			if(a[n]%i==0){
				j+=1;
			}
			if(j==2){
				j=0;
				break;
			}
			i++;
		}
		k+=j;
		n--;
	}
	printf("%d", k);
}
