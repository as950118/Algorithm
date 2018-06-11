#include<stdio.h>

struct form{
	int val;
	struct form *next;
	struct form *prev;
}form;

int func(struct form *a, struct form *b, int set, int n){
	if(a->next->val == b->next->val){
		set++;
		if(set!=n){
			func(a->next, b->next, set, n);
		}
		else{
			return set;
		}
	}
	else{
		return 0;
	}
}


int func2(struct form *a, struct form *b, int set, int n){
	if(a->next->val == b->prev->val){
		set++;
		if(set!=n){
			func2(a->next, b->prev, set, n);
		}
		else{
			return set;
		}	
	}
	else{
		return 0;
	}
}


int main(){
	int n;
	scanf("%d", &n);
	if(n==1 || n==2){
		printf("good puzzle");
	}
	int i;
	struct form j[n];
	struct form k[n];
	
	scanf("%d", &j[0].val);
	for(i=1; i<n-1; i++){
		scanf("%d", &j[i].val);
		j[i].prev = &j[i-1];
		j[i].next = &j[i+1];
	}
	scanf("%d", &j[n-1].val);
	j[n-1].prev = &j[n-2];
	j[n-1].next = &j[0];
	j[0].prev = &j[n-1];
	j[0].next = &j[1];
	
	scanf("%d", &k[0].val);
	for(i=1; i<n-1; i++){
		scanf("%d", &k[i].val);
		k[i].prev = &k[i-1];
		k[i].next = &k[i+1];
	}
	scanf("%d", &k[n-1].val);
	k[n-1].prev = &k[n-2];
	k[n-1].next = &k[0];
	k[0].prev = &k[n-1];
	k[0].next = &k[1];
	
	for(i=0; i<n; i++){
		if(j[i].val==k[0].val){
			if(j[i].next->val == k[0].next->val){
				int set = func(j[i].next, k[0].next, 2, n);
				if(set==n){
					printf("good puzzle");
					break;
				}
				else if(set==0){
					printf("bad puzzle");
					break;
				}
			}
			else if(j[i].next->val == k[0].prev->val){
				int set = func2(j[i].next, k[0].prev, 2, n);
				if(set==n){
					printf("good puzzle");
					break;
				}
				else if(set==0){
					printf("bad puzzle");
					break;
				}
				printf("\n%d", set);
			}
			else{
				printf("bad puzzle");
				break;
			}
		}
		else{
		}
	}
}

