#include<iostream>
using namespace std;//cout�� endl�� iostream�� std��� �̸������� ���ǵǾ����� 
//�� namespace std�� ���� ������, �Ʒ����� std::cout, std::endl���� �ۼ��Ͽ����� 

class Animal{
	private:
		int food;
		int weight;
	
	public:
		void set(int setFood, int setWeight){
			food = setFood;
			weight = setWeight;
		}
		void increaseFood(int inc){
			food += inc;
			weight += (inc/3);
		}
		void stat(){
			cout<<"food : "<<food<<endl;
			cout<<"weight : "<<weight<<endl;
		}
};

int main(){
	Animal animal;
	animal.set(100,100);
	animal.increaseFood(30);
	animal.stat();
	return 0;
} 
