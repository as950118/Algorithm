#include<iostream>
using namespace std;//cout와 endl은 iostream의 std라는 이름공간에 정의되어있음 
//이 namespace std를 쓰지 않으면, 아래에서 std::cout, std::endl같이 작성하여야함 

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
