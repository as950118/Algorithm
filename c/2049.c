#include<stdio.h>
#include<string.h>

int func(int *a){
	int sum=a[0]+a[1]+a[2]+a[3];
	if(sum==4){
		puts("E");
	}
	else if(sum==3){
		puts("A");
	}
	else if(sum==2){
		puts("B");
	}
	else if(sum==1){
		puts("C");
	}
	else{
		puts("D");
	}
}

int main(){
	int a[4],b[4],c[4];
	scanf("%d %d %d %d", &a[0],&a[1],&a[2],&a[3]);
	scanf("%d %d %d %d", &b[0],&b[1],&b[2],&b[3]);
	scanf("%d %d %d %d", &c[0],&c[1],&c[2],&c[3]);
	func(a);
	func(b);
	func(c);
}
