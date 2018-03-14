#include<stdio.h>
//012 345 678 ...192021 22.23.24  25
//0	1 2..7 8 9
int main(){
	char dial[16];
	int num,sum=0;
	int i;
	int len;
	scanf("%s", dial);
	len=strlen(dial);
	for(i=0;i<len;i++){
		num=dial[i]-'A';
		if(dial<=17){	
		}
		else if(num>=18 && dial[i]!='Z'){
			num--;	
		}
		else if(dial[i]=='Z'){
			num-=2;
		}
			num/=3;
			num+=2;
		sum+=num+1;
	}
	printf("%d", sum);
	
}
