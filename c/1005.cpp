#include <iostream> 
#include <vector> 
#include <algorithm> 
using namespace std; 
int memo[1001]; 
bool connection[1001][1001]; 
int constructTime[1001];
 
void InitAllValue() {
	for (int i = 0; i < 1001; i++){
		memo[i] = 0;
		constructTime[i] = 0;
		for (int j = 0; j < 1001; j++) {
			connection[i][j] = false;
		} 
	} 
}
	
int solve(int goal, int buildingNum) {
	if (memo[goal] > 0) { 
		return memo[goal]; 
	}
	int result = 0; 
	for (int i = 0; i < buildingNum; i++) { 
		if (connection[i][goal]) { 
			result = max(result, solve(i, buildingNum)); 
		}
	}
	memo[goal] = result + constructTime[goal];
	return memo[goal];	
}
int main() { 
	int t;
	cin >> t;
	while (t) {
		InitAllValue();
		int buildingNum;
		int OrderRuleNum;
		cin >> buildingNum >> OrderRuleNum;
		int temptime = 0;
		for (int i = 0; i < buildingNum; i++) {
			cin >> temptime; constructTime[i] = temptime; 
		}
		for (int i = 0; i < OrderRuleNum; i++) {
			int from, end;
			cin >> from >> end;
			connection[from - 1][end - 1] = true;
		}
		int goal;
		cin >> goal;
		int result= solve(goal - 1, buildingNum);
		cout << result << endl; 
		t--;
	} 
}




//#include<iostream>
//#define DEBUG_
//#define FOR(i,n) for(i=1; i<=n; i++)
//
//int D[1001]={0,};
//int K[1001][1001]={0, };
//int path[1001]={0,};
//int dp[100001] = {0, };
//int n,k;
//int ret;
//
//int max(int a, int b){
//	int re= a>b? a:b;
//	return re;
//}
//
//int func(int dest, int cnt){
//	int i,j;
//	for(i=1; i<=n; i++){
//		for(j=1; j<=path[i]; j++){
//			if(K[i][j] == dest){
//				dp[cnt+1] = max(dp[cnt+1], dp[cnt] + D[i]);			
//				ret = max(ret, func(i,cnt+1));
//			}
//		}
//	}
//	return cnt;
//}
//
//int main(){
//	int t;
//	int i,j;
//	int x,y;
//	int a,b;
//	int dest=0;
//	#ifdef DEBUG
//	while(1){
//	#endif
//	scanf("%d", &t);
//	while(t){
//		//건물 수, 관계 수
//		scanf("%d %d", &n, &k); 
//		//건물당 소요 시간 
//		for(i=1;i<=n;i++){
//			scanf("%d", &D[i]); 
//		}
//		//관계도
//		for(i=1;i<=k;i++){
//			scanf("%d %d", &x, &y);
//			path[x]+=1;
//			K[x][path[x]]=y;
//		}
//		//지어야하는건물
//		scanf("%d", &dest);
//		dp[1] = D[dest];
//		ret=1;
//		func(dest, 1);
//		printf("%d\n", dp[ret]);
//		
//		for(i=1; i<=n;i++){
//			D[i]=0;
//			for(j=1; j<=path[i];j++){
//				K[i][j]=0;
//			}
//			path[i]=0;
//		}
//		for(i=1;i<=ret;i++){
//			dp[i]=0;
//		}
//		ret=0;
//		t--;
//	}
//	#ifdef DEBUG
//	puts("reset\n");
//	}
//	#endif
//
//}
//
//
////int main(){
////	int T;
////	int N, K;
////	int *D;
////	int **relate;
////	int i;
////	int a,b;
////	int max=0;
////	int buf=0;
////	int sex;
////	#ifdef DEBUG
////	while(1){
////	#endif
////
////	
////	scanf("%d", &T); // 케이스 수 
////	printf("got it 1\n");
////	while(T){
////		scanf("%d %d", &N, &K); //건물 수 //관계 수 
////		printf("got it 2\n");
////		D=calloc(N+1, sizeof(int));
////		i=1;
////		while(i<=N){
////			scanf("%d", &D[i]);	//건물당 걸리는 시간 
////			i++;
////		}
////		printf("got it 3\n");
////		
////		//2차원 배열 동적할당 
////		relate=(int**)calloc(N+1, sizeof(int));
////		for(i=0; i<N+1; i++){
////			relate[i] =(int*)calloc(N+1, sizeof(int));
////		}
////		
////		//관계도 
////		i=1;
////		while(i<=K){	 
////			scanf("%d %d", &a, &b);
////			relate[a][b]=1;	//관계가 1이면 a->b, 0이면 노상관 
////			i++;
////		}
////		printf("got it 4\n");
////		
////		//지어야하는 건물 
////		scanf("%d", &b);
////		printf("got it 5\n");
////		
////		//통로 찾기
////		sex=D[b];
////		int j;
////		for(j=1; j<=b; j++){
////			restart:
////			i=b-1;
////			while(i>0){
////				if(relate[i][b]==1){
////					buf+=D[i];
////					relate[i][b]=0;
////					b=i;
////					goto restart;
////				}
////				else{
////					i--;
////				}
////			}
////			max = max>buf ? max:buf;
////		}#include<iostream>

