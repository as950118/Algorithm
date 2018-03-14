#include<stdio.h>

int main(){
	int m,n;
	int i,j,k=0,l,sum=0,avg=0;
	scanf("%d", &m);
	scanf("%d", &n);
	while(m<=n){
		i=1;
		j=0;
		while(1){
			if(m==1 || j>2 ){
				j=0;
				break;
			}
			if(i==n+1){
				j==2;
				break;
			}
			if(m%i == 0){
				j++;
			}
			i++;
		}
		
		if(j==2){
			k++;
			sum+=m;
			if(avg==0){
				avg=m;
			}
		}
		m++;
	}
	
	if(k==0){
		printf("%d", -1);
	}
	else{
		printf("%d\n%d", sum, avg);
	}
	
}
