#include<iostream>
using namespace std;//cout�� endl�� iostream�� std��� �̸������� ���ǵǾ����� 
//�� namespace std�� ���� ������, �Ʒ����� std::cout, std::endl���� �ۼ��Ͽ����� 

int ChangeVal(int &p){//���۷������ ����, �����Ϳ� ��������� �ٸ�/���۷����� �ѹ� ����Ǹ� �ٸ������� ���۷����� �ɼ� ���� 
	p = 3;
	return 0;
}
int ChangeVal2(int p){
	p = 3;
	return 0;
}
int main(){
	int Num=5;
	cout<<Num<<endl;
	ChangeVal(Num);
	cout<<Num<<endl;
	ChangeVal2(Num);
	cout<<Num<<endl;
	
	//���۷����� �������� ���� 
	int& a=Num;
	int* b=&Num;
	
	cout<<"C++(a) : "<<a<<endl;
	cout<<"C++(Num) : "<<Num<<endl;
	printf("C : %d\n", *b);
	
	int Num2=10;
	a=Num2;
	b=&Num2;
	
	cout<<"C++(a) : "<<a<<endl;
	cout<<"C++(Num) : "<<Num<<endl;
	printf("C : %d", *b);
	//��ó�� �����ʹ� ������ �� ������, ���۷����� ������������ 
	//������ ���۷����� a=Num2; ó�� �Է��� �� �ִµ�,
	//�̰��� �� Num�� ���� Num2�� �ٲٰ� ��. 
}
