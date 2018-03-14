#include<stdio.h>
#include<math.h>
/*
lÀº M,NÁß Å«°Í 
X_Y´Â X,Y Â÷ÀÌ 

Â÷	XYÂ÷ 
0	0
1	l-1 1 .. L-2 2 .. L-3 3 .. 2 L-2 .. 1 0
2	l-2 2 .. L-4 4 .. L-6 6 .. 4 L-4 .. 2 0
3	l-3 3 .. L-6 6 .. L-9 9 .. 6 L-6 .. 3 0
4	l-4 4 .. L-8 8 .. L-12 12 .. 8 L-8 .. 4 0

.
.

Â÷ÀÇ °ø½Ä ==> M_N==l-I*X_Y || M_N==L-X_Y ÀÌ¾î¾ß ÇÔ 

*/
//int main(){
//	int t, m,n, x,y;
//	int m_n, x_y;
//	int mn_xy; 
//	int i=0,j,k,l;
//	scanf("%d", &t);
//	while(t){
//		scanf("%d %d %d %d", &m,&n,&x,&y);
//		//¹Ø¿¡ ¹æ¹ýÀº Æó±âÇÏ¿´ 
//		//m°ú n, x¿Í yÀÇ Â÷¸¦ ±¸ÇÔ 
//		m_n = m>n ? m-n : n-m;
//		x_y = x>y ? x-y : y-x;
//		l= m>n ? m : n;
//		//µÎ Â÷°¡ ³ª´² ¶³¾îÁöÁö ¾Ê´Â´Ù¸é ÀÖÀ» ¼ö ¾ø´Â °æ¿ì
//		while(1){
//			if(l-i*x_y<0 || m_n==l-i*x_y || m_n==l-x_y){
//				printf("%d\n",fun(m,n,x,y));
//				break;	
//			}
//			
//			i++;
//		}
//		
//		t--;
//	}
//}
//
//int fun(int m, int n, int x, int y){
//	int i=1,j=1,c=1;
//	while(1){
//		if(i==x && j==y){
//			return c;
//		}
//		if(i==m+1){
//			i=1;
//		} 
//		if(j==n+1){
//			j=1;
//		}
//		i++;
//		j++;
//		c++;
//	}
//}

/*
È¦Â¦ => Â¦ È¦ È¦ Â¦ Â¦ È¦ È¦ Â¦ Â¦
È¦È¦ => È¦ Â¦ È¦ Â¦ È¦ Â¦ 
Â¦Â¦ => Â¦ Â¦ Â¦ Â¦ Â¦ Â¦ Â¦ 

1 2 1 2 1 2 1 1 ==> È¦
1 2 1 2 1 2 1 2 ==> Â¦

5¿Í 20 
*/

int main(){
	int T;
	scanf("%d", &T);
	int x,y,x_=0,y_=0;
	int M,N;
	int Big;
	int Small;
	int Big_Small;
	int x_y;
	while(T){
		scanf("%d %d %d %d", &M,&N,&x,&y);
		if(M>N){
			Big = M;
			Small = N;
			Big_Small = M-N;
		}
		else{
			Big = N;
			Small = M;
			Big_Small = N-M;
		}
		
		if(Big_Small==0){
			if(x-y!=0){
				puts("-1");
			}
			else{
				printf("%d", x);
			}
		}
		else{
			if(M<N){
				
			}
			else{
				
			}
			
		}
		
		
		T--;
	}
}



