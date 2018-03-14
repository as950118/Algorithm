#include<stdio.h>

int main(){
	char s[161];
	char c[21];
	int i,j,k,t;
	scanf("%d", &t);
	while(t){
	
	scanf("%d %s", &i, c);
	for(j=0; j<strlen(c); j++){
		for(k=i*j; k<i*j+i; k++){
			s[k]=c[j];
		}
	}
	printf("%s", s);
	t--;
	}
}
