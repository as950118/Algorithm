#include<stdio.h>

int fibonacci(int n);

int zero =0;
int one =0;
		
int main(){
	int i;
	scanf("%d", &i);
	int a;
	while(i>0){
		scanf("%d", &a);
		zero =0;
		one =0;
		fibonacci(a);
		printf("%d %d\n", zero, one);
		i--;
	}
}

int fibonacci(int n) {
	if (n==0) {
        zero++;
        return 0;
    } else if (n==1) {
        one++;
        return 1;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}
