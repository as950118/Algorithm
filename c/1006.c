#include<stdio.h>
#include<math.h>

int main(){
	int t;
	int i,j;
	int n;
	double buf[20][20], sum;
	double vector[20][2];
	scanf("%d", &t);
	while(t){
		scanf("%d", &n);
		for(i=0; i<n; i++){
			scanf("%lf %lf", &vector[i][0], &vector[i][1]);
		}
		for(i=0; i<n; i++){
			for(j=1; j<n; j++){
				buf[i][j]=sqrt(pow((vector[i][0]-vector[j][0]),2)+pow((vector[i][1]-vector[j][1]),2));
			}
		}
		for(i=0; i<n; i++){
			for(j=1; j<n; j++){
				buf[i][j]<buf[i][j+1];
			}
		}
		
		printf("%f", buf);
		t--;
	}
}
