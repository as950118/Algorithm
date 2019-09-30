#include <iostream>
#include <algorithm>
#include <cstring>
#include <array>
#define debug 1
using namespace std;

int n,m,w,h;
int person[2001], day[2001], ret[2001];
int flag[2001];
int able[2001];

int func(){
	for(int i=0; i<m; i++){
		continue;
	}
	return 0;
}

int main() {
	memset(person, 0, sizeof(person));
	memset(day, 0, sizeof(day));
	memset(ret, 0, sizeof(ret));
	memset(flag, 0, sizeof(flag));
	memset(able, 0, sizeof(able));
	
	cin>>m>>n>>w>>h;
	
	for(int i=0; i<m; i++){
		cin>>person[i];
	}
	for(int i=0; i<n; i++){
		cin>>day[i];
	}
	//Á¤·Ä 
	sort(person, person+m);
	if(debug){
		cout<<"sort person"<<endl;
		for(int i=0; i<m; i++){
			cout<<person[i]<<" ";
		}
		cout<<endl;
		char b = index(test, "b");
		cout<<b;
	}
	return 0;

}
