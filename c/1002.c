#include<stdio.h>
#include<math.h>

int main(){
    int x1,y1,x2,y2,r1,r2,max_r,min_r;
    double r;
	int n;
    int what;
	scanf("%d",&n);
	for(n; n>0; n--){
  		scanf("%d %d %d %d %d %d", &x1,&y1,&r1,&x2,&y2,&r2);  
		   
		r=sqrt((double)((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)));
		max_r=r1>r2 ? r1:r2;
		min_r=r1>r2 ? r2:r1;
		what=0;
		
   	 	if(x1==x2 && y1==y2){	//같은 점일때 
        	if(r1==r2){
				what=-1;
			}
			else{
				what=0;
			}
			goto sex;
   		}
   		
   		else if(r==r1+r2){	//외접할 때
   			what=1;
		}
		
		else if(r<r1+r2){	//내접하거나 내외부에서 만날때 때 
			if(r<max_r && max_r==r+min_r){		//내접 
				what=1;
			}
			else if(r<max_r && max_r<r+min_r){		//내부에서 2점 
				what=2;
			}
			else if(r<max_r && max_r>r+min_r){		//안접함 
				what=0;
			}
			else{
				what=2;
			}
		}
		else{
		}
		
    	sex:
    	printf("%d\n", what);
	}
}
