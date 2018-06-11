#include<stdio.h>
#include<string.h>

#define TOKEN "\n\t "

int main(){
	char string[100];
	char *token;
	
	gets(string);
	token=strtok(string,TOKEN);
	while(token !=NULL){
		puts(token);
		token=strtok(0,TOKEN);	
	}

}
