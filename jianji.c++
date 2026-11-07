#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a,b;
	char c;
	scanf("%d%c%d",&a,&c,&b);
	if(c=='+')
		printf("%d\n",a+b);
	if(c=='-')
		printf("%d\n",a-b);
	if(c=='*')
		printf("%d\n",a*b);
	if(c=='/')
	{
		if(b==0)
          printf("-1\n");
      else
        printf("%.1f\n",1.0*a/b);
	}
		
	return 0;
}