#include<stdio.h>

//2 1 00 11
//3 1 000 111
//3 2 010 101
//4 1 0000 1111
//4 2 0000 1111 0101 1010
//4 3 0000 1111 0110 1001 0101 1010
//5 1 
//5 2 00000 11111 01010 10101
//5 3 00000 11111 00100 01001 10010 11011 10110 01101
//5 4 00000 11111 00100 00010 01000 10001  
//6 1
//6 2 

//
int func(int a, int b, int c){
	int len = b-a+1;
	int d[len];
	for(i=0;i<len;i++){
		d[i]=0;
		d[i]=1;
		func2(d[i+1]);
	}
	
	
}

int func2(int *a, int b){
	
}
int main(){
	int n,m;
	int i,j;
	
	scanf("%d %d", &n,&m);
	if(m==0){
		
		return 0;
	}
	int l[m],r[m],k[m], len[m];
	
	for(i=0; i<m; i++){
		scanf("%d %d %d", &l[i],&r[i],&k[i]);
		len[i]=l[i]-r[i];
	}
	
	

}
