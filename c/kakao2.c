#include<stdio.h>
#include<string.h>
#include<stdlib.h>

struct ST{
	int check;
	int val;
}ST;

int main(){
	int i,j=0;
	char str[9];
	struct ST buf[3];
	scanf("%s", str);
	
	for(i=0; i<strlen(str); i++){
		if(str[i]=='1'){
			if(str[i+1]=='0'){
				printf("%s", str[i+1]);
				buf[j].val=10;
				i++;
				j++;
			}
			else{
				buf[j].val=1;
				j++;
			}
		}
		else if(str[i]=='S'){
		}
		else if(str[i]=='D'){
			buf[j-1].val = buf[j-1].val*buf[j-1].val;
		}
		else if(str[i]=='T'){
			buf[j-1].val = buf[j-1].val*buf[j-1].val*buf[j-1].val;
		}
		else if(str[i]=='*'){
			if(j==1){
				buf[j-1].val *= 2;
			}
			else{
				buf[j-1].val *= 2;
				buf[j-2].val *= 2;
			}
		}
		else if(str[i]=='#'){
			buf[j-1].val *= -1;
			}
		else{
			buf[j].val = atoi(&str[i]);
			j++;
		}
	}
	

	printf("%d", buf[0].val+buf[1].val+buf[2].val);
	
	
}
