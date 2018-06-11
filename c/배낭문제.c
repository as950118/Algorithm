#include <stdio.h>

typedef struct B{
	int value;
	int weight;
	float value_weight;
}B;

int main()
{
   FILE* f = NULL;
   int num =0;
   int i,j;
   B tmp;
   int value[num];
   int weight[num];
   B a[num];
   B b[num];
   int C = 1000;
   int L = 0, w = 0, v = 0;

   f = fopen("test.txt", "r");

   while(!feof(f))
   {
      fscanf(f, "%d %d", &value[num], &weight[num]);
      printf("%d %d\n", value[num], weight[num]);
      a[num].value = value[num];
      a[num].weight = weight[num];
	  a[num].value_weight = (float)value[num] / weight[num];
      
      printf("%f\n", a[num].value_weight);
      num++;
      printf("num : %d\n", num);
   }
   for (i = 0; i < num; i++) {
      b[i] = a[i];
   }
   for (i = 0; i < num-1; i++)
   {
      for (j = 1; j < num - i; j++)
      {
         if (b[j - 1].value_weight < b[j].value_weight)
         {
            tmp = b[j - 1];
            b[j - 1] = b[j];
            b[j] = tmp;
         }
      }
   }
   for (i = 0; i < num; i++)
      printf("%d¹øÂ°\nV\t: %d\nW\t: %d\nV/W\t: %f\n", i, b[i].value, b[i].weight, b[i].value_weight);
   	
}
