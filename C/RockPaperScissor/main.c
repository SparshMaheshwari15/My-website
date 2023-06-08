#include<stdio.h>
#include <stdlib.h>
#include <time.h>
int CheckInput(char a){
    if (a=='r' || a=='p' || a=='s')
    {
        return 1;
    }
    else{
        return 0;
    }
}
int Game(char comp,char you){
    int a=CheckInput(you);
    if (a==0)
    {
        return 2;
    }
    if (a==1)
    {
        if (comp==you)
        {
            return 0;
        }
        if (comp=='r')
        {
            if (you=='p')
            {
                return 1;
            }
            if (you=='s')
            {
                return -1;
            }
            
        }
        if (comp=='p')
        {
            if (you=='s')
            {
                return 1;
            }
            if (you=='r')
            {
                return -1;
            }
            
        }
        if (comp=='s')
        {
            if (you=='r')
            {
                return 1;
            }
            if (you=='p')
            {
                return -1;
            }
            
        }
        
        
    }
    
}
int main(){
    int a;
    srand(time(0));
    int number=rand()%100;
    char c,u;
    // printf("%d\n",number);
    if (number<=33)
    {
        c='r';
    }
    if (number>33 && number<=66)
    {
        c='p';
    }
    if (number>66)
    {
        c='s';
    }
    printf("Computer has choose %c\n",c);
    printf("The random number is %d\n",number);
    printf("Enter your move Rock(r),Papper(p),Scissor(s)\n");
    scanf("%c",&u);
    printf("You have chosen %c\n",u);
    a=Game(c,u);
    if (a==2)
    {
        printf("Enter Correct input\n");
    }
    if (a==0)
    {
        printf("Oh ho It's a try\n");
    }
    if (a==-1)
    {
        printf("Computer win\n");
    }
    if (a==1)
    {
        printf("You win\n");
    }
    
    

return 0;
}