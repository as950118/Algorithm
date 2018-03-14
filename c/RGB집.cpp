#include<stdio.h>

int main(){
	int i=0;
	int n;
	scanf("%d", &n);
	int VR[100],VG[100],VB[100], Paint[100];
	int sum;
	for(i=0; i<n; i++){
		scanf("%d %d %d", VR[i],VG[i],VB[i]);
	}
	i=0;
	for(i=0; i<n; i++){
		Paint[i] = VR[i]>VG[i] ? VR[i]:VG[i];
		sum+=Paint[i];
	}
	printf("%d", sum);	
}
