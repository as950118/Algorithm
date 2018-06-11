#include<iostream>
using namespace std;//cout와 endl은 iostream의 std라는 이름공간에 정의되어있음 
//이 namespace std를 쓰지 않으면, 아래에서 std::cout, std::endl같이 작성하여야함 

int ChangeVal(int &p){//레퍼런스라는 개념, 포인터와 비슷하지만 다름/레퍼런스는 한번 선언되면 다른변수의 레퍼런스가 될수 없음 
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
	
	//레퍼런스와 포인터의 차이 
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
	//이처럼 포인터는 변경할 수 있으나, 레퍼런스는 변경하지못함 
	//하지만 레퍼런스도 a=Num2; 처럼 입력할 수 있는데,
	//이것은 곧 Num의 값을 Num2로 바꾸게 됨. 
}
