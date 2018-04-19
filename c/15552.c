#include<stdio.h>

int main(){
	int t;
	
	int a,b,ret;
	
	scanf("%d", &t);
	
	while(t){
		
		scanf("%d %d", &a,&b);
		ret = a+b;
		printf("%d\n", ret);
		
		t--;
	}
	
}
