#include<stdio.h>
#include<string.h>

int main(){
  char arr1[4001];
  char arr2[4001];
  int dp[4002][4002] = {0,};
  scanf("%s%s", arr1,arr2);
  int len1 = strlen(arr1);
  int len2 = strlen(arr2);
  int ret = 0;
  int i,j;
  for(i=1; i<=len1; i++){
    for(j=1; j<=len2; j++){
      if(arr1[i-1]==arr2[j-1]){
        dp[i][j] = dp[i-1][j-1] + 1;
      }
      if(dp[i][j]>ret){
      	ret = dp[i][j];
      }
    }
  }
  printf("%d",ret);
}
