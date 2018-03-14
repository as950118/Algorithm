#include<stdio.h>

int main(){
	char c[1000001];
	int count[53];
	memset(count, 0, 53);
	int i,j,k,m,n;
	int max;
	scanf("%s", c);
	int g=strlen(c);
	for(i=0; i<g; i++){
		if(c[i]>='a'){
			k=c[i]-97;
		}
		else
			k=c[i]-65;
		count[k]++;
	}
	max=count[0];
	m=0;
	n=0;
	
	for(i=1; i<53; i++){
		if(count[i]>=max){
			max=count[i];
			m=i;
		}
	}
	
	for(i=0; i<53; i++){
		if(count[i]==max){
			max=count[i];
			n++;
		}
	}
	
	if(n>=2){
		printf("?");
	}
	else{
		printf("%c", m+65);
	}
}
