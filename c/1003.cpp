#include<iostream>
#include<string>
using namespace std;

int zero=0, one=0;
int memo[41][2]={0,};
int set[41]={0,};
	
int fibonacci(int n) {
    	
    if(set[n]!=0){
    	zero+=memo[n][0];
    	one+=memo[n][1];
    	return 0;
	}
	else{
	}
    
	if (n == 0) {
        zero++;
        return 0;
    } else if (n == 1) {
        one++;
        return 1;
    } else { 
    	return fibonacci(n-1)+fibonacci(n-2);
    }
}

int main(){
	int t;
	int n;
	int i;
	cin>>t;
	while(t){
		cin>>n;
		fibonacci(n);

		memo[n][0]=zero;
		memo[n][1]=one;
		
		set[n]=1;
		cout<<zero<<' '<<one<<endl;
		zero=0, one=0;
		t--;
	}
}

 
