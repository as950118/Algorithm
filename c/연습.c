#include<stdio.h>
#include<string.h>
#include<math.h>12
/*
3==		00*
		0*0*
		*****

6==		00000*
		0000*0*
		000*****
		00*00000*
		0*0*000*0*
		*****0*****
		
12		00000000000*
		0000000000*0*
		000000000*****
		00000000*00000*
		0000000*0*000*0*
		000000*****0*****
		00000*00000000000*
		0000*0*000000000*0*
		000*****0000000*****
		00*00000*00000*00000*
		0*0*000*0*000*0*000*0*
		*****0*****0*****0*****
		
�� 1
�� 2

�� 2
�� 4

�� 2��
�� 4��
�� 8��

�� 2��
�� 4��
�� 8��
�� 16��	

0+0 10+1 40+3 80+7 ==> 2^n * 5 + 2^n-1

2^n *5 + 2^n -1 ==> 2^n * 6 -1
3n+1 ==> 1
3n+2 ==> 2
3n+3 ==> 5
*/

int star(int n){
	int i,j;
	
	if(n==i){
			printf("*");
		}
		else if(n==i+1){
			puts("");
		}
		else{
			printf(" ");
		}
}

int sel(int n){
	int col,i,j,k=0,space;
	col=n/3;//���� �����
	//ù��° �� 
	for(i=1; i<=n-1; i++){
		printf(" ");
	}
	printf("*");
	puts("");
	for(i=1; i<=n-2; i++){
		printf(" ");
	}
	printf("* *");
	puts("");
	for(i=1; i<=n-3; i++){
		printf(" ");
	}
	printf("*****");
	puts("");
	//�ι�° ��
	for(i=1; i<=n-4; i++){
		printf(" ");
	}
	printf("*");
		for(i=1; i<=5; i++){
			printf(" ")
		}
		printf("*");
		puts("");
	for(i=1; i<=n-5; i++){
		printf(" ");
	}
	printf("* *");
		for(i=1; i<=3; i++){
			printf(" ")
		}
		printf("* *");
		puts("");
	for(i=1; i<=n-6; i++){
		printf(" ");
	}
	printf("*****");
		for(i=1; i<=1; i++){
			printf(" ");
		}
		printf("*****");
		puts("");
	//������
	for(i=1; i<=n-7; i++){
		printf(" ");
	}
	printf("*");
		for(i=1; i<=11; i++){
			printf(" ")
		}
		printf("*");
		puts("");
	for(i=1; i<=n-8; i++){
		printf(" ");
	}
	printf("* *");
		for(i=1; i<=9; i++){
			printf(" ")
		}
		printf("* *");
		puts("");
	for(i=1; i<=n-9; i++){
		printf(" ");
	}
	printf("*****");
		for(i=1; i<=7; i++){
			printf(" ");
		}
		printf("*****");
		puts("");
	//�׹�° ��
	for(i=1; i<=n-10; i++){
		printf(" ");
	}
	printf("*");
		for(i=1; i<=5; i++){
			printf(" ")
		}
		printf("*");
		for(i=1; i<=5; i++){
			printf(" ")
		}
		printf("*");
		for(i=1; i<=5; i++){
			printf(" ")
		}
		printf("*");
		puts("");
	for(i=1; i<=n-11; i++){
		printf(" ");
	}
	printf("* *");
		for(i=1; i<=3; i++){
			printf(" ")
		}
		printf("* *");
		for(i=1; i<=3; i++){
			printf(" ")
		}
		printf("* *");
		for(i=1; i<=3; i++){
			printf(" ")
		}
		printf("* *");
		puts("");
	for(i=1; i<=n-12; i++){
		printf(" ");
	}
	printf("*****");
		for(i=1; i<=1; i++){
			printf(" ");
		}
		printf("*****");
		for(i=1; i<=1; i++){
			printf(" ");
		}
		printf("*****");
		for(i=1; i<=1; i++){
			printf(" ");
		}
		printf("*****");
		puts("");
	 
	
	 
};

int star(){
	
} 

int main(){
	int n,col;
	scanf("%d", n);
	col=n/3;//�������� 
}
