#include<stdio.h>
#include<math.h>

int countingM(int *count){
	while(i%j==0){
		i=i/j;
		count[j]++;
	}
	countingM(i,j);
};
int countingN(int i,int j){
	while(i%j==0){
		i=i/j;
		countN[j]++;		
	}
	countingN(i,j);
};
int compare(){
	int j;
	for(j=1; j<31; j++){
		if(countM[j]-countN[j]>=0){
			countM[j]=countM[j]-countN[j];
		}
	}
};


int main(){
	int countM[31];
	int countN[31];
	int t1,t2;
	scanf("%d", &t1);
	t2=t1;
	int k[t1];
	int n,m,i,j;
	while(t1){
		j=1;
		memset(countM,0,31);
		memset(countN,0,31);
		scanf("%d %d", &n, &m);
		for(i=m-1; i>=m-n+1; i--){
			countingM(i,j);
		}
		j=1;
		for(i=n-1; i>=1; i--){
			countingN(i,j);
		}
		compare();
		m=n=1;
		for(j=1; j<31; j++){
			if(countM[j]>0){
				m=m*countM[j];
			}
			if(countN[j>0]){
				n=n*countN[j];
			}
		}
		k[t1]=m/n;
	t1--;
	}
	while(t2){
	printf("%d\n", k[t2]);
	t2--;
	}
}

