#include<stdio.h>

int main(){
	int row, column;
	scanf("%d %d", &row,&column);
	int map[row*column];
	int i=0;
	int lineup=0;
	while(i<row*column){
		scanf("%d",map[i]);
			if(lineup==row){
				printf("\n");
				lineup=0;
			}
			else{
				printf(" ");
			}
		i++;
		lineup++;
	}
	printf("%d", map[row*column]);
}
