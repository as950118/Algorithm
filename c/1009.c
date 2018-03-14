#include<stdio.h>
#include<math.h>

int main(){
	int t;
	unsigned long long int a,b;
	scanf("%d", &t);
	int i=t;
	int c[t];
	while(t){
		scanf("%d %d", &a, &b);
		if(a==1 || a==5 || a==6 || a%10==0){
			c[t]=a;
			if(a%10==0){
				c[t]=10;
			}
		}
		else if(a==2 || a==9){
			while(b>2){
				b=b-2;
			}
			c[t]=pow(a,b);
			c[t]=c[t]%10;
		}
		else{
			while(b>4){
				b=b-4;
			}
			c[t]=pow(a,b);
			c[t]=c[t]%10;
		}
		
		
		t--;
	}
	while(i){
		printf("%d\n", c[i]);
		i--;
	}
	
}
/*
2 4
3 4
4 2
5 1
6 1
7 4
8 4
9 2
10 1
공통적으로 4마다 반복됨 
*/
