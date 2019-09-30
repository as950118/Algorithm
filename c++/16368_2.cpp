#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<stack>
#define ll long long

using namespace std;

const ll MAXN=2005;
vector<int>ret[MAXN];
//day = �׳��� ��
//per = �� ����� ���ؾ��ϴ� �ϼ�
//st = �׳� ���� �����ؾ��ϴ� ����� ��
int day[MAXN], per[MAXN], st[MAXN];

struct Point
{
    int id,cnt,next;
    Point(int i,int c,int n){id=i;cnt=c;next=n;}
    //�ٸ� Point ����ü�� ���Ҷ� cnt�� �������� �Ѵٴ� �ǹ�
    bool operator < (const Point& r)const
    {
        return cnt<r.cnt;
    }
};

int sum(int a[], int size){
	int ret = 0;
	for(int i=1; i<=size; i++){
		ret += a[i];
	}
	return ret;
}

int main()
{
	//�˾Ƽ� ���ĵǴ� �켱���� ť ���
	//���� ���� ������ �ؾ���
    priority_queue<Point> q;
    //�۾� ��⿭
    queue<Point> q1;
	int m,n,w,h;
    
    cin>>m>>n>>w>>h;
	
    for(int i=1;i<=m;i++){
        cin>>day[i];
    }
    
    for(int i=1;i<=n;i++){
        cin>>per[i];
        st[i]=per[i];
    }
    
    //day�� per�� �����ʴٸ� ������������
    if(sum(day, m) != sum(per, n)){
    	cout<<-1<<endl;
    	return 0;
    }
    if(n < m+w-1){
    	
    }
    
	st[0]=0;
	//�׳� ���� �����ؾ��ϴ� �����
	//�������� ���ϴ� Ƚ��(w) ��ŭ ���� ���� ����ؾ���
    for(int i=1;i<=n;i++){
        for(int j=1; j<w; j++){
            st[i + j] -= st[i];
        }
    }

	//�켱���� ť�� �ֱ�
	//id, �׳� ���� ����, ������ ��
	//�׳� ���� ������ ���ĵ�
    for(int i=1;i<=m;i++){
        q.push(Point(i,day[i],1));
    }
    
    Point now = {0,0,0};
    for(int i=1;i<=n;i++){
    	//q1�� �ְ� q1�� �������� i��� 
        while(q1.size() && q1.front().next==i){
        	//q1���� ���� �������� ������ ������ q�� ����
        	//�ֳĸ� ���� ���� ���� ������ ���� �ؾ������� ���� ���̹Ƿ�
        	now = q1.front();
            q1.pop();
            q.push(now);
        }
        
        //�׳� ���� �����ؾ� �ϴ� �����ŭ
        while(st[i]--){
        	//st[i] == ������ ����
        	//q�� ����� == ���� �Ҽ� ����
        	//������ ���Ҵµ� ���� �� �� ���ٸ�
            if(q.size()==0){
            	cout<<-1<<endl;
            	return 0;
            }
            //q�� ���� �ʾҴٸ�
            else{
            	//���� ������ ���� ���� ������ ó������
            	now = q.top();
            	q.pop();
            }
            
            //������ �ִµ� ��ü ��¥ < ���� ��¥ + ������ �ؾ����� - 1 �̶��
            //���� ������ �� �����Ƿ� -1
            if(n < i+w-1){
            	cout<<-1<<endl;
            	return 0;
            }
            
            //�Ϸ��� ������ �߰�
            ret[now.id].push_back(i);
            now.next = i+w+h;
            now.cnt -= w;
            
            //���� �ؾ������� ���Ҵٸ�
            if(now.cnt !=0 ){
            	//��⿭�� �߰�
            	q1.push(now);
            }
        }
    }
    
    //ť == ���ؾ��ϴ� ��
    //���ؾ��ϴ� ���� ���Ҵٸ� -1
    if(q.size() || q1.size()){
       	cout<<-1<<endl;
       	return 0;
    }
    else{
    	cout<<1<<endl;
	    for(int i=1; i<=m; i++){
	        int len = ret[i].size();
	        for(int j=0; j<len; j++){
	        	cout<<ret[i][j]<<' ';
	        }
	        cout<<endl;
	    }
    }
    return 0;
}
