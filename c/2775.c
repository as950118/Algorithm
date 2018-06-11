#include<stdio.h>

/*
1 4 1020355684119163==> 
1 3 6 101521283544..==> n*(n+1)/2
1 2 3 4 5 6 7 8 9.. ==> n
*/

int fun(int k, int n);

int main(){
    int t,k,n;
    scanf("%d", &t);
    while(t){
    	scanf("%d %d", &k, &n);
    	printf("%d\n", fun(k,n));
    	t--;
	}
}

int fun(int k, int n){
	int i=n;
	int buf=0;
	if(k==0){
		buf=n;
	}
	else if(k==1){
		buf=n*(n+1)/2;
	}
	else{
		k=k-1;
		while(i>0){
			buf+=fun(k,i);
			i--;
		}
	}
	return buf;
}
