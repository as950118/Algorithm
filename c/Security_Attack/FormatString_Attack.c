#include<stdio.h>

int main(int argc, char **argv){
	
	char *name = "Jeong";
	int age = 25;
	int nbytes = 0;
	
	printf("Name = %s age = %d%n\n", name, age, &nbytes);//\n�� �ƴ϶� %n�� 
	printf("nbytes = %d", nbytes);//"Name ~~ age = 25" ������ ���ڿ� ���̰� ��µ� 
	
	return 0;
}
