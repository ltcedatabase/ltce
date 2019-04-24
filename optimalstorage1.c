//Optimal Storage
#include<stdio.h>
int n=3,sum=0,pSum=0;
int L[]={5,3,10};
int RT[]={0,0,0};
void OptimalStorageSchedule();
void SortProgs();
int main()
{
	OptimalStorageSchedule();
	return 0;
}
void OptimalStorageSchedule()
{
	int k=0,i,Sum;
	printf("\n\nOriginal program lenght");
	for(i=0;i<n;i++)
	{
		printf("%d",L[i]);
	}
	SortProgs();
	printf("\n\nSorted program lenght: -->");
	for(i=0;i<n;i++)
	{
		pSum= pSum + L[i];
		Sum = pSum + L[i];
		RT[i] =Sum;
	}
	printf("\n\nTotal retrival time --> %d",RT[2]);
	printf("\n\nMean Retrieval Time: --> %f",RT[2]/(float)n);
}
void SortProgs()
{
	int i,j,temp;
	for(i=0;i<n-1;i++)
	{
		for(j=0;j<(n-1);j++)
		{
			if(L[j+1]<L[j])
			{
				temp=L[j];
				L[j]=L[j+1];
				L[j+1]=temp;
			}
		}
	}
}
  
  
