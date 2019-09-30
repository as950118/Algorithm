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
//day = 그날의 일
//per = 그 사람이 일해야하는 일수
//st = 그날 일을 시작해야하는 사람의 수
int day[MAXN], per[MAXN], st[MAXN];

struct Point
{
    int id,cnt,next;
    Point(int i,int c,int n){id=i;cnt=c;next=n;}
    //다른 Point 구조체와 비교할때 cnt를 기준으로 한다는 의미
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
	//알아서 정렬되는 우선순위 큐 사용
	//일이 많은 날부터 해야함
    priority_queue<Point> q;
    //작업 대기열
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
    
    //day와 per가 같지않다면 성립하지않음
    if(sum(day, m) != sum(per, n)){
    	cout<<-1<<endl;
    	return 0;
    }
    if(n < m+w-1){
    	
    }
    
	st[0]=0;
	//그날 일을 시작해야하는 사람은
	//연속으로 일하는 횟수(w) 만큼 전에 것을 고려해야함
    for(int i=1;i<=n;i++){
        for(int j=1; j<w; j++){
            st[i + j] -= st[i];
        }
    }

	//우선순위 큐에 넣기
	//id, 그날 일의 개수, 다음날 일
	//그날 일의 개수로 정렬됨
    for(int i=1;i<=m;i++){
        q.push(Point(i,day[i],1));
    }
    
    Point now = {0,0,0};
    for(int i=1;i<=n;i++){
    	//q1이 있고 q1의 다음값이 i라면 
        while(q1.size() && q1.front().next==i){
        	//q1에서 가장 마지막에 들어간값을 꺼내서 q에 넣음
        	//왜냐면 가장 많은 날이 지난게 가장 해야할일이 많은 날이므로
        	now = q1.front();
            q1.pop();
            q.push(now);
        }
        
        //그날 일을 시작해야 하는 사람만큼
        while(st[i]--){
        	//st[i] == 할일의 숫자
        	//q가 비었다 == 일을 할수 없다
        	//할일이 남았는데 일일 할 수 없다면
            if(q.size()==0){
            	cout<<-1<<endl;
            	return 0;
            }
            //q가 비지 않았다면
            else{
            	//가장 할일이 많은 날을 꺼내서 처리시작
            	now = q.top();
            	q.pop();
            }
            
            //할일이 있는데 전체 날짜 < 현재 날짜 + 앞으로 해야할일 - 1 이라면
            //일을 종료할 수 없으므로 -1
            if(n < i+w-1){
            	cout<<-1<<endl;
            	return 0;
            }
            
            //완료한 날들을 추가
            ret[now.id].push_back(i);
            now.next = i+w+h;
            now.cnt -= w;
            
            //오늘 해야할일이 남았다면
            if(now.cnt !=0 ){
            	//대기열에 추가
            	q1.push(now);
            }
        }
    }
    
    //큐 == 일해야하는 날
    //일해야하는 날이 남았다면 -1
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
