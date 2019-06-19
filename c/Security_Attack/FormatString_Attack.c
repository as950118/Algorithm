#include<stdio.h>

int main(int argc, char **argv){
	
	char *name = "Jeong";
	int age = 25;
	int nbytes = 0;
	
	printf("Name = %s age = %d%n\n", name, age, &nbytes);//\n이 아니라 %n임 
	printf("nbytes = %d", nbytes);//"Name ~~ age = 25" 까지의 문자열 길이가 출력됨 
	
	return 0;
}
