#include<iostream>
using namespace std;//cout와 endl은 iostream의 std라는 이름공간에 정의되어있음 
//이 namespace std를 쓰지 않으면, 아래에서 std::cout, std::endl같이 작성하여야함 

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
