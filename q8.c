//  Read three numbers and check if all three are equal (use && )
#include<stdio.h>
int main() {
    int a,b,c;
    printf("Enter a number");
    scanf("%d",&a);
    printf("Enter second number:");
    scanf("%d",&b);
    printf("Enter third number:");
    scanf("%d",&c);
    if (a&&b==c) {
        printf("all are equal.");
    }
    else {
        printf("all are not equal.");
    }
}
