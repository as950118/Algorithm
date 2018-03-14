#include<iostream>
using namespace std;//cout와 endl은 iostream의 std라는 이름공간에 정의되어있음 
//이 namespace std를 쓰지 않으면, 아래에서 std::cout, std::endl같이 작성하여야함 
int main(){
	int i;
	char c;
	double d;
	float f;
	//c언어와 다를바없는 변수선언방식
	//하지만 for문을 쓸대 ()안에 변수선언을 하여도됨.
	for(int j=0; j<1; j++){
		printf("For");
	} 
	return 0;
}
