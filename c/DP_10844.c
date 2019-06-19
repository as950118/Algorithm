#include <stdio.h>

#define mod 1000000000

int main()
{
    int DP[101][10];
    int n,i,j;
    int sum = 0;

    scanf("%d", &n);

    for (j = 0; j < 10; j++)
        DP[1][j] = 1;

    for (i = 2; i <= n; i++)
    {
        for (j = 0; j < 10; j++)
        {
            if (j == 0)
                DP[i][j] = DP[i - 1][1] % mod;

            else if (j == 9)
                DP[i][j] = DP[i - 1][8] % mod;

            else
                DP[i][j] = (DP[i - 1][j - 1] + DP[i - 1][j + 1]) % mod;
        }

    }

    for (j = 1; j < 10; j++)
        sum = (sum + DP[n][j]) % mod;

    printf("%d", sum);

    return 0;
}



