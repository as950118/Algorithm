#include<iostream>
using namespace std;//cout와 endl은 iostream의 std라는 이름공간에 정의되어있음 
//이 namespace std를 쓰지 않으면, 아래에서 std::cout, std::endl같이 작성하여야함 
int main(){
	int* p = new int;
	*p = 10;
	
	cout<<*p<<endl;
	
	delete p;
	//new, delete는 malloc, free와 같음
	
	int ArrSize;
	
	cout<<"Array Size : ";
	cin>>ArrSize;
	//cin은 입력받는 것임 
	
	int* list = new int[ArrSize];
	
	for(int i=0; i<ArrSize; i++){
		cin>>list[i];
	} 
	for(int i=0; i<ArrSize; i++){
		cout<<i<<"th element of list : "<<list[i]<<endl;
	} 
	delete[] list;
	return 0;
}
