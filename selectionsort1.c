#include<stdio.h>
void main()
{
	int a[10],i,j,n,smallest,swap;
	printf("Enter number of elements==");
	scanf("%d",&n);

	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	printf("Sorted element= ");
	for(i=0;i<n;i++)
	{
		smallest=i;
		for(j=i+1;j<n;j++)
		{
			if(a[j]<a[smallest])
			{
				smallest=j;
			}
		}	
		swap=a[smallest];
		a[smallest]=a[i];
		a[i]=swap;
	}
        for (i=0; i < n; i++) 
        {
       		 printf("%d ", a[i]); 
  	         printf("\n");  
	} 
}
  


