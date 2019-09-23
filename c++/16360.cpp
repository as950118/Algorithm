#include <iostream>
#include <string>
using namespace std;
int n;
string S;
string engs("aiylneortuvw");
//string eng[12] = {"a", "i", "y", "l", "n", "ne", "o", "r", "t", "u", "v", "w"};
string lat[12] = {"as", "ios", "ios", "les", "anes", "anes", "os", "res", "tas", "us", "ves", "was"};

string func(string s){
	string eng_last;
	int idx_last;
	string append_lat;

	eng_last = s[s.size() -1];
	idx_last = engs.find(eng_last);

	if(idx_last>12){
		append_lat = "us";
		s.append(append_lat);
		return s;
	}
	if(idx_last == 5){
		string if_n;
		if_n = s[s.size() -2];
		if(s.size()>1 && if_n.compare("n") == 0){
			s.erase(s.size()-2, s.size());
			append_lat = lat[idx_last];
			s.append(append_lat);
		}
		return s;
	}
	s.erase(s.size()-1, s.size());
	append_lat = lat[idx_last];
	s.append(append_lat);
	return s;
}

int main() {
	cin>>n;
	for(int i=0; i<n; i++){
		cin>>S;
		cout<<func(S)<<endl;
	}
	return 0;
}
