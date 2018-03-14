#include<stdio.h>

int main(){
	int T;
	int N, K;
	int *D;
	int **relate;
	int i;
	int a,b;
	int max=0;
	int buf=0;
	int sex;
	
	scanf("%d", &T); // 케이스 수 
	printf("got it 1\n");
	while(T){
		scanf("%d %d", &N, &K); //건물 수 //관계 수 
		printf("got it 2\n");
		D=calloc(N+1, sizeof(int));
		i=1;
		while(i<=N){
			scanf("%d", &D[i]);	//건물당 걸리는 시간 
			i++;
		}
		printf("got it 3\n");
		
		//2차원 배열 동적할당 
		relate=(int**)calloc(N+1, sizeof(int));
		for(i=0; i<N+1; i++){
			relate[i] =(int*)calloc(N+1, sizeof(int));
		}
		
		//관계도 
		i=1;
		while(i<=K){	 
			scanf("%d %d", &a, &b);
			relate[a][b]=1;	//관계가 1이면 a->b, 0이면 노상관 
			i++;
		}
		printf("got it 4\n");
		
		//지어야하는 건물 
		scanf("%d", &b);
		printf("got it 5\n");
		
		//통로 찾기
		sex=D[b];
		int j;
		for(j=1; j<=b; j++){
			restart:
			i=b-1;
			while(i>0){
				if(relate[i][b]==1){
					buf+=D[i];
					relate[i][b]=0;
					b=i;
					goto restart;
				}
				else{
					i--;
				}
			}
			max = max>buf ? max:buf;
		}
	
		//출력 
		printf("%d\n", max+sex);
		
		//해제
		for(i=0; i<=N+1; i++){
			free(relate[i]);
		}
		free(relate);
		max=0;
		buf=0;
		T--;
	}
}
