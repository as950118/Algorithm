#include<stdio.h>
#include<unistd.h>

void main(void){
	int childpid;
    static int a;
	childpid = fork();
    if(childpid > 0){
    	for(a; a<100; a++){
        	if(a%2 == 0){
            	printf("O");
            }
        }
        exit(0);
    }
    else{
    	for(a; a<100; a++){
        	if(a%2 == 1){
            	printf("X");
            }
        }
        exit(0);
    }
}

