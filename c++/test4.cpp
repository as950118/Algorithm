#include<iostream>
using namespace std;//cout�� endl�� iostream�� std��� �̸������� ���ǵǾ����� 
//�� namespace std�� ���� ������, �Ʒ����� std::cout, std::endl���� �ۼ��Ͽ����� 
int main(){
	int* p = new int;
	*p = 10;
	
	cout<<*p<<endl;
	
	delete p;
	//new, delete�� malloc, free�� ����
	
	int ArrSize;
	
	cout<<"Array Size : ";
	cin>>ArrSize;
	//cin�� �Է¹޴� ���� 
	
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
