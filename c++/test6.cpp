#include<iostream>
using namespace std;//cout�� endl�� iostream�� std��� �̸������� ���ǵǾ����� 
//�� namespace std�� ���� ������, �Ʒ����� std::cout, std::endl���� �ۼ��Ͽ����� 

void print(int a){
	cout<<"int : "<<a<<endl;
}
void print(char a){
	cout<<"char : "<<a<<endl;
}
void print(double a){
	cout<<"double : "<<a<<endl;
}

int main(){
	int a = 1;
	char b = 'b';
	double c = 3.14;
	print(a);
	print(b);
	print(c);
} 
