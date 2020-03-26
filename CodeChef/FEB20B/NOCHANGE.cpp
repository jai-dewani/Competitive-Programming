#include<bits/stdc++.h>
using namespace std;

void solve(){
	int n,p;
	cin>>n>>p;
	int d[n];
	for(int i=0;i<n;i++){
		cin>>d[i];
	}
	bool flag = false;
	int flag_index = -1;
	for(int i=0;i<n;i++){
		if(p%d[i]!=0){
			flag = true;
			flag_index = i;
		}
	}
	if(flag){
		cout<<"YES ";
		for(int i=0;i<n;i++){
			if(i==flag_index){
				int count = p/d[i];
				cout<<count+1<<" ";
			}else{
				cout<<"0 ";
			}
		}
		cout<<endl;
	}else{
		cout<<"NO"<<endl;
	}

}

int main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		solve();
	}
	// cout<<t;
	return 0;
}
