#include<stdio.h>
#define DEBUG
#define FOR(i,n) for(i=1; i<=n; i++)

int main(){
	int t;
	int D[1001]={0,};
	int K[1001][1001];
	int i;
	int n, k;
	int a,b;
	int dest;
	#ifdef DEBUG
	while(1){
	#endif
	scanf("%d", &t);
	while(t){
		//�ǹ� ��, ���� ��
		scanf("%d %d", &n, &k); 
		//�ǹ��� �ҿ� �ð� 
		FOR(i,n){
			scanf("%d", &D[i]); 
		}
		//���赵 
		FOR(i,k){
			scanf("%d %d", &a, &b);
			//K[a]=b;
			//K[b]=a;
		}
		//������ϴ°ǹ�
		scanf("%d", &dest);
		
		
		
		t--;
	}
	#ifdef DEBUG
	puts("reset\n");
	}
	#endif

}


//int main(){
//	int T;
//	int N, K;
//	int *D;
//	int **relate;
//	int i;
//	int a,b;
//	int max=0;
//	int buf=0;
//	int sex;
//	#ifdef DEBUG
//	while(1){
//	#endif
//
//	
//	scanf("%d", &T); // ���̽� �� 
//	printf("got it 1\n");
//	while(T){
//		scanf("%d %d", &N, &K); //�ǹ� �� //���� �� 
//		printf("got it 2\n");
//		D=calloc(N+1, sizeof(int));
//		i=1;
//		while(i<=N){
//			scanf("%d", &D[i]);	//�ǹ��� �ɸ��� �ð� 
//			i++;
//		}
//		printf("got it 3\n");
//		
//		//2���� �迭 �����Ҵ� 
//		relate=(int**)calloc(N+1, sizeof(int));
//		for(i=0; i<N+1; i++){
//			relate[i] =(int*)calloc(N+1, sizeof(int));
//		}
//		
//		//���赵 
//		i=1;
//		while(i<=K){	 
//			scanf("%d %d", &a, &b);
//			relate[a][b]=1;	//���谡 1�̸� a->b, 0�̸� ���� 
//			i++;
//		}
//		printf("got it 4\n");
//		
//		//������ϴ� �ǹ� 
//		scanf("%d", &b);
//		printf("got it 5\n");
//		
//		//��� ã��
//		sex=D[b];
//		int j;
//		for(j=1; j<=b; j++){
//			restart:
//			i=b-1;
//			while(i>0){
//				if(relate[i][b]==1){
//					buf+=D[i];
//					relate[i][b]=0;
//					b=i;
//					goto restart;
//				}
//				else{
//					i--;
//				}
//			}
//			max = max>buf ? max:buf;
//		}
//	
//		//��� 
//		printf("%d\n", max+sex);
//		
//		//����
//		for(i=0; i<=N+1; i++){
//			free(relate[i]);
//		}
//		free(relate);
//		max=0;
//		buf=0;
//		T--;
//	}
//	#ifdef DEBUG
//	}
//	#endif
//
//}
