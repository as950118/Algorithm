#include<stdio.h>

int main(){
	char ch[101];
	int len,i,j,k,n,m,count=0;
	scanf("%s", ch);
	len=strlen(ch);
	
	for(i=0; i<len; i++){
		if(i<len-1 && ch[i]=='c' && (ch[i+1]=='=' || ch[i+1]=='-')){
			count++;
			i++;
		}
		else if(i<len-1 && ch[i]=='d' && ch[i+1]=='-'){
			count++;
			i++;
		}
		else if(i<len-2 && ch[i]=='d' && ch[i+1]=='z' && ch[i+2]=='='){
			count++;
			i+=2;
		}
		else if(i<len-1 && (ch[i]=='l' || ch[i]=='n') && ch[i+1]=='j'){
			count++;
			i++;
		}
		else if(i<len-1 && (ch[i]=='s' || ch[i]=='z') && ch[i+1]=='='){
			count++;
			i++;
		}
		else{
			count++;
		}
	}
	printf("%d", count);
}
