#include<stdio.h>
#include<math.h>
int main(){
	int t,n,i;
	int x1,y1,x2,y2;
	int r1,r2;
	int x,y,r;
	int what;
	scanf("%d", &t);
	int *count;
	int k;
	count=calloc(t,sizeof(int));
	k=t;
	while(t){
		what=0;
		scanf("%d %d %d %d", &x1,&y1,&x2,&y2);
		scanf("%d", &n);
		for(i=0; i<n; i++){
			scanf("%d %d %d", &x,&y,&r);
			if((pow((x1-x),2)+pow((y1-y),2))<r*r && (pow((x2-x),2)+pow((y2-y),2))>r*r){
				what++;
			}
			else if((pow((x2-x),2)+pow((y2-y),2))<r*r && (pow((x1-x),2)+pow((y1-y),2))>r*r){
				what++;
			}
		}
		count[t]=what;
		t--;
	}
	while(k){
	printf("%d\n",count[k]);
	k--;
	}
}
