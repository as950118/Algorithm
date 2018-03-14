#include<stdio.h>


int main(){
	int n=0,three=0,five=0;
	scanf("%d", &n);
	if(n)
	while(n>2){
		if(n%5==0){
			five++;
			n=n-5;
		}
		else if(n%3==0){
			three++;
			n=n-3;
			if(three>=5){
				three=three-5;
				five=five+3;
			}
		}
		else{
			five=-1;
			goto end;
		}
	}
	five+=three;
	end:
	printf("%d", five);
	
	
}
