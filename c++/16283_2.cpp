#include<bits/stdc++.h> 
using namespace std; 
int a, b, n, w; 
void solve(){ 
    int ans = 0, shp; 
    for(int i=1;i<n;++i) 
        if(a*(i)+b*(n-i)==w) 
            ans++, shp = i; 
    if(ans==1) 
        printf("%d %d",shp,n-shp); 
    else printf("-1"); } 
int main(){ 
    scanf("%d%d%d%d",&a,&b,&n,&w); 
    solve(); 
}

