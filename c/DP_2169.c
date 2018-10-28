#include<stdio.h>

long long MIN = -10000000;
int arr[1001][1001];
long long dp[1001][1001][4];
int dir_x[3] = {1,0,0};
int dir_y[3] = {0,1,-1};
int n,m;
int i,j,k;

int max(int a, int b);
int func(int x, int y, int d);

int main(){
  scanf("%d %d", &n, &m);
  for(i=0; i<n; i++){
    for(j=0; j<m; j++){
      scanf("%d", &arr[i][j]);
      for(k=0; k<4; k++){
        dp[i][j][k] = MIN;
      }
    }
  }
  printf("%lld", func(0,0,0));
}

int max(int a, int b){
  if(a>b){
    return a;
  }
  else{
    return b;
  }
}

int func(int x, int y, int d){
  int xx, yy;
  if(x==n-1 && y==m-1){
    return arr[x][y];
  }
  int *ret = dp[x][y][d];
  if(ret != MIN){
    return ret;
  }
  for(i=0; i<3; i++){
    xx = x+dir_x[i];
    yy = y+dir_y[i];
    if(xx>-1 && xx<n && yy>-1 && yy<m && dp[xx][yy][3]==MIN){
      dp[xx][yy][3] = 1;
      ret = max(ret, func(xx,yy,i)+arr[x][y]);
      dp[xx][yy][3] = MIN;
    }
  }
  printf("%d", ret);
  return ret;
}
