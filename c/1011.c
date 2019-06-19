#include<stdio.h>
#include<math.h> 

/*

1=1			11

2= 1 1		21

3= 1 1 1
4= 1 2 1	22

5= 1 2 1 1
6= 1 2 2 1	32

7= 1 2 2 1 1
8= 1 2 2 2 1
9= 1 2 3 2 1	33

10=1 2 3 2 1 1
11=1 2 3 2 2 1
12=1 2 3 3 2 1	43

13=1 2 3 3 2 1 1
14=1 2 3 3 2 2 1
15=1 2 3 3 3 2 1
16=1 2 3 4 3 2 1		44

17=1 2 3 4 3 2 1 1
18=1 2 3 4 3 2 2 1
19=1 2 3 4 3 3 2 1
20=1 2 3 4 4 3 2 1		54

21=1 2 3 4 4 3 2 1 1
22=1 2 3 4 4 3 2 2 1
23=1 2 3 4 4 3 3 2 1
24=1 2 3 4 4 4 3 2 1
25=1 2 3 4 5 4 3 2 1	55

*36=1 2 3 4 5 6 5 4 3 2 1

*/

int main(){
	int t;
	int x,y;
	unsigned long long int len;
	unsigned long long int i=0,j,k,m,n;
	long double len_sqrt;
	scanf("%d", &t);
	while(t){
		scanf("%d %d", &x,&y);
		len=y-x;
		len_sqrt=sqrt((double)len);
		i=(int)len_sqrt;
		while(1){
			j=i*i;
			k=i*(i-1);
			m=i*(i+1);
			if(len<=j && len>k){
				printf("%d\n", i*2-1);
				break;
			}
			else if(len<=m && len>j){
				printf("%d\n", i*2);
				break;
			}
			i++;
		}
		t--;
	}
}
