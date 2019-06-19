#include<stdio.h>
#include<math.h>

int main(){
	int a,b,c,d;
	int i=1;
	int count[10]={0,0,0,0,0,0,0,0,0,0};
	scanf("%d\n%d\n%d", &a,&b,&c);
	d=a*b*c;
	while(1){
		a=pow(10,i);
		if(d/a==0){
			break;
		}
		i++;
	}
	i--;
	while(i+1){
		b=pow(10,i);
		a=d/b;
		d=d%b;
		count[a]++;
		i--;
	}
	printf("%d\n", count[0]);
	printf("%d\n", count[1]);
	printf("%d\n", count[2]);
	printf("%d\n", count[3]);
	printf("%d\n", count[4]);
	printf("%d\n", count[5]);
	printf("%d\n", count[6]);
	printf("%d\n", count[7]);
	printf("%d\n", count[8]);
	printf("%d", count[9]);
}
