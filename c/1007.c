#include <stdio.h>
#include <math.h>

// SX : 모든 x좌표들의 합
// SY : 모든 y좌표들의 합
long long SX, SY;
int vector[20][2], N;
 
long long MIN(long long a, long long b){
    return (a == 9223372036854775807)? b: (a>b)?b:a;
}

// x : 선택한 vector들의 x좌표들의 합
// y : 선택한 vector들의 y좌표들의 합
long long VECTOR_MATCHING(int left, int index, long long x, long long y){
    if(left == 0)
        return (SX-x-x)*(SX-x-x)+(SY-y-y)*(SY-y-y);
 
    long long ans = 9223372036854775807;
    for(; index < N; index++)
        ans = MIN(ans, VECTOR_MATCHING(left-1, index+1, x+vector[index][0], y+vector[index][1]));
 
    return ans;
}
  
int main(){
    int i, Testcase;
 
    scanf("%d", &Testcase);
    while(Testcase--){
        SX = SY = 0;
        scanf("%d", &N);
        for(i = 0; i < N; i++){
            scanf("%d %d", &vector[i][0], &vector[i][1]);
            SX += vector[i][0];
            SY += vector[i][1];
        }
 
        printf("%.6lf\n", sqrt((double)VECTOR_MATCHING(N/2, 0, 0, 0)));
    }
 
    return 0;
}
