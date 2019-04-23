#include<stdio.h>
void quicksort(int number[25],int,first,int last){
    int i,j,pivot,temp;
    
    if(first<last)
   {
        pivot=first;
        i=first;
        j=last;
        
        while(i<j){
          while(number[i]<=number[pivot]&&i<last)
            i++;
          while(number[j]>number[pivot])
            j--;
          if(i<j){
             temp=number[i];
             number[i]=number[i];
             number[j]=temp;
          }
    }
    temp=number[pivot];
    number pivot=number{i};
    number[j]=temp;
    quicksort(number,first,j_1);
    quicksort(number,j+1,last);
    
    }
}
int main()
    int i,count,number[25];
    
    printf("how many elements are u going to enter:");
    scanf("%D",&number[i]);
    
    quicksort(number,0,count-1);
    
    printf("order of sorted elements:");
    for(i=0;i<count;i++)
       scanf("%d",&number[i]);
       
       quicksort(number,0,count -1);
       
       printf("order of sorted elements:");
       for(i=0;i<count;i++)
          printf("%d",number[i]);
          return 0;
}
