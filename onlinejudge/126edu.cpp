#include<bits/stdc++.h>
#define ll long long int
#define pb push_back
using namespace std;
void solve()
{

	ll n,i;
	cin>>n;
	ll a[n],b[n];
	vector<ll> v,m;
	for(i=0;i<n;i++)
	{
		cin>>a[i];
		v.push_back(a[i]);
		
	}
	for(i=0;i<n;i++)
	{
		cin>>b[i];
		m.push_back(b[i]);
	}
	for(i=0;i<n;i++)
	{
		if(a[i]<b[i])
		{
			int r=a[i];
			a[i]=b[i];
			b[i]=r;
		}
		
	}long long int sum=0;
	for(i=0;i<n-1;i++)
	{
		sum+=abs(a[i]-a[i+1]);
	}
	for(i=0;i<n-1;i++)
	{
		sum+=abs(b[i]-b[i+1]);
	}
	cout<<sum<<endl;
	
	
}
int32_t main()
{
ios::sync_with_stdio(false);
cin.tie(0);
ll t;
cin>>t;
while(t--)
{
solve();
}
return 0;
}
