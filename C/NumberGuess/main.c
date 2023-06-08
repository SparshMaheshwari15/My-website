#include<stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
    int num;
    int guess=1;
    srand(time(0));
    int number=rand()%100 +1;
    printf("The random number is %d\n",number);
    
    do
    {
        printf("Guess a number between 1-100:");
        scanf("%d",&num);
        if (num>100 || num<1)
        {
            printf("Enter a correct input\n");
            printf("Enter a number between 1-100\n");
            guess--;
        }
        
        else if (num>number)
        {
            printf("Enter a lower number\n");
        }
        else if (num<number)
        {
            printf("Enter a bigger number\n");
        }
        else if (num==number)
        {
            printf("You won the game in %d guess",guess);
        }
        guess++;
    } while (num!=number);
    

return 0;
}