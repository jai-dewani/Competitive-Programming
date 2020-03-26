#include<bits/stdc++.h>
using namespace std;

void solve(int* dp, int sum){
	int m1,m2,y1,y2;
	cin>>m1>>y1;
	cin>>m2>>y2;
	if(m1>2) y1++;
	if(m2<2) y2--;
	int mod_y1 = y1%2800;
	int mod_y2 = y2%2800;
	int ans = 0;
	if(y2-y1<2800){
		if(mod_y1<=mod_y2){
			for(int i=mod_y1;i<=mod_y2;i++){
				ans+=dp[i];
				// cout<<dp[i]<<" ";
			} 
		}else{
			for(int i=mod_y1;i<2800;i++) {
				ans+=dp[i];
				// cout<<dp[i]<<" ";
			}
			for(int i=0;i<=mod_y2;i++) {
				ans+= dp[i];
				// cout<<dp[i]<<" ";
			}
		}
	}else{
		ans += ((y2-y1)/2800)*sum;
		y1 = y1%2800;
		y2 = y2%2800;
		if(y1<=y2){
			for(int i=y1;i<=y2;i++) ans+=dp[i];
		}else{
			for(int i=y1;i<2800;i++) ans+=dp[i];
			for(int i=0;i<=y2;i++) ans+= dp[i];
		}
	}
	cout<<ans<<endl;
}

int main(){
	int t;
	cin>>t;
	int dp[2800];
	int day = 4; 
	int sum = 0;
	for(int i=0;i<2800;i++){
		if(i>2000 && i<2400){
			cout<<i<<" "<<day<<endl;
		}
		if(i%4==0){
			if(i%100==0 && i%400!=0){
				if(day==5 || day==6){
					dp[i]=1;
				}else{
					dp[i]=0;
				}
			}else{
				if(day==5){
					dp[i]=1;
				}else{
					dp[i]=0;
				}
				day++;
			}
		}else{
			if(day==5 || day==6){
				dp[i]=1;
			}else{
				dp[i]=0;
			}
		}
		day++;		
		day = day%7;
	}
	// for(int i=2000;i<2040;i++) cout<<i<<" "<<dp[i]<<" "<<endl;
	// cout<<endl;
	for(int i=0;i<2800;i++) sum+=dp[i];
	for(int i=0;i<t;i++){
		solve(dp,sum);
	}
}

// 1 0 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0 1 0 0