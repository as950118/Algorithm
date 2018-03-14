#include<stdio.h>
int i=0;

int process(int a){
	if(a%3==0){
		div_3(a);
	}
	else if(a%2==0){
		div_2(a);
	}
	else{
		sub_1(a);
	}
}
int div_3(int a){
	a=a%3;
	if(a%3==0){
		div_3(a);
	}
	else if(a%2==0){
		div_2(a);
	}
	else{
		sub_1(a);
	}
}
int div_2(int a){
}
int sub_1(int a){
}

int main(){
	int x;
	scanf("%d", &x);

	while(x!=1){
		if(x%3==0){
			x=x/3;
			i++;
		}
		else if(x%2!=0 && (x-1)%3==0){
			x--;
			i++;
		}
		else if(x%2==0){
			x=x/2;
			i++;
		}
		else if(x!=1){
			x--;
			i++;
		}
	}
	printf("%d", i);
}
