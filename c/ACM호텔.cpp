#include<stdio.h>

int main(){
    int t,w,h,n,i;
    scanf("%d", &t);
    while(t){
    	scanf("%d %d %d", &h, &w, &n);
    	
    	if(n%h==0){
    		w=n/h;
		}
		else{
			w=n/h;
			w=w+1;
			h=n%h;
		}
		
		printf("%d\n", h*100+w);
		
		
    	t--;
	}
   
}
