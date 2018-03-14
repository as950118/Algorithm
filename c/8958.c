#include<stdio.h>

int main(){
	char OX[81];
	int count_O=0;
	int i,j=0,t;
	scanf("%d", &t);
	while(t){
		memset(OX, NULL, 81);
		scanf("%s", OX);
		for(i=0; i<strlen(OX); i++){
			while(OX[i]=='O'){
				j++;
				i++;
				count_O+=j;
			}
			j=0;
		}
		printf("%d\n", count_O);
		t--;
		count_O=0;
	}
}
