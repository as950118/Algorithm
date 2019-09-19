#include <iostream>
#include <cstring>
#include <tuple>
#include <queue>
#include <vector>
#include <list>
#include <cmath>
#include <algorithm>
#define INF 1e9
using namespace std;

int dp[1001][1001];
int n, w;
int prv[1001];
pair<int, int> map[1001];

int func(int x, int y){
	if(x==w || y==w)
	 	return 0;
	
	int &ret = dp[x][y];
	int temp;	
	if(ret != -1)
		return ret;
		
	int max_x_y = max(x,y);
	ret = func(max_x_y+1, y) + abs(map[max_x_y + 1].first - (x ? map[x].first : 1)) + abs(map[max_x_y + 1].second - (x ? map[x].second : 1));
	temp = func(x, max_x_y+1) + abs(map[max_x_y + 1].first - (y ? map[y].first : n)) + abs(map[max_x_y + 1].second - (y ? map[y].second : n));
	if(ret<temp){
		prv[max_x_y + 1] = 1;
		func(max_x_y+1, y);
	}
	else{
		ret = temp;
		prv[max_x_y + 1] = 2;
		func(x, max_x_y + 1);
	}
	return ret;
}

int main(){
	cin>>n;
	cin>>w;
	memset(dp, -1, sizeof(dp));
	memset(map, 0, sizeof(map));
	memset(prv, 0, sizeof(prv));
	for(int i=1; i<=w; i++){
		cin>>map[i].first;
		cin>>map[i].second;
	}
	cout<<func(0,0)<<endl;
	for(int i=1; i<=w; i++){
		cout<<prv[i]<<endl;
	}
	return 0;
}
