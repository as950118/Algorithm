#include<stdio.h>
#include<math.h>
/*
*/

int main(){
	int n,i,j,max;
	int num[10]={0,};
	scanf("%d", &n);
	if(n==0){
		printf("1");
		return 0;
	}
	//���ڸ����� ã�� ���� 
	i=0;
	while(1){
		if(n/(int)pow(10,i)==0){
			i--;
			break;
		}
		i++;
	}
	//�� �ڸ��������� ����
	while(i+1){
		num[n/(int)pow(10,i)]++;
		n=n%(int)pow(10,i);
		i--;
	}
	
	//6�� 9�� �ջ���	
	num[6]+=num[9];
	if(num[6]%2==0){
		num[6]=num[6]/2;
	}
	else{
		num[6]=num[6]/2;
		num[6]++;
	}
	
	//�ְ� �ڸ��� ã��
	i=0;
	max=i;
	while(i<8){
		if(num[max]<num[i+1]){
			max=i+1;
		}
		i++;
	}
	printf("%d", num[max]);
}
