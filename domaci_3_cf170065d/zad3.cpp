#include <stdio.h>
#include <stdlib.h>
#include <vector>
#define NUM 10
int COSTS[NUM][NUM] = {

	0 ,   374 , 200,  223 , 108  ,178 , 252  ,285  ,240  ,356,
374,  0   , 255,  166 , 433,  199,  135,  95,   136 , 17,
200 , 255  ,0   , 128  ,277 , 821 , 180 , 160,  131  ,247,
223  ,166 , 128  ,0  ,  430  ,47   ,52   ,84  , 40 ,  155,
108 , 433  ,277,  430 , 0  ,  453,  478,  344  ,389 , 423,
178  ,199,  821 , 47   ,453 , 0   , 91 ,  110,  64   ,181,
252 , 135 , 180  ,52 ,  478  ,91   ,0   , 114 , 83 ,  117,
285  ,95  , 160 , 84  , 344,  110,  114  ,0    ,47  , 78,
240  ,136  ,131  ,40   ,389 , 64  , 83 ,  47 ,  0    ,118,
356  ,17   ,247  ,155 , 423  ,181  ,117 , 78  , 118 , 0



};

int calc_cost(int* array) {
	//array comes in form 1-1 , 2-3, 4-5, where first num represents node, second one represents neighbour
	int sum = 0;
	int hash[NUM] = {};
	for (int i = 0; i < NUM - 1; i++) {
		sum += COSTS[array[2*i]-1][array[2 * i + 1]-1];
		hash[array[2*i]-1]++;
		hash[array[2 * i + 1] - 1]++;
	}
	for (int i = 0; i < NUM; i++) {
		if (hash[i] > 3) sum += (hash[i] - 3) * 100;
	}
	return sum;
}


void print_results(std::vector<int*>& results, int len) {
	printf("Most efficient ways of connecting cities are: \n");
	for (int* res : results) {
		for (int i = 0; i<len; i++) {
		
				printf(" %d", res[i]);
				if ((i + 1) % 2 == 0 && i<len-2)
					printf("-");
			
		
		}
	
		printf("\n");
	
	}



}
void sequenceToSpanningTree(int* P, int len, int* T) {
	int i, j, q = 0;
	int n = len + 2;
	int* V = new int[n];
	for (i = 0; i < n; i++)
		V[i] = 0;

	for (i = 0; i < len; i++)
		V[P[i] - 1] += 1;

	for (i = 0; i < len; i++) {
		for (j = 0; j < n; j++)
		{
			if (V[j] == 0) {
				V[j] = -1;
				T[q++] = j + 1;
				T[q++] = P[i];
				V[P[i] - 1]--;
				break;
			}
		}
	}

	j = 0;
	for (i = 0; i < n; i++)
	{
		if (V[i] == 0 && j == 0) {

			T[q++] = i + 1;
			j++;
		}
		else if (V[i] == 0 && j == 1) {

			T[q++] = i + 1;
			break;

		}
	}

	delete[] V;
}




void variation_with_repetition(int n, int k) {
	int q;
	int* P = new int[k];
	for (int i = 0; i < k; i++)
		P[i] = 1;
   
	int* T = new int[2*k +2];
	std::vector<int*> results;
	int min = -1;
	do {
		sequenceToSpanningTree(P, k,T);
		int curr= calc_cost(T);
		if (curr < min || min == -1) {
			
			for (int* tmp : results) delete[]tmp;
			results.clear();
			int* curr_min = new int[2 * k + 2];
			memcpy(curr_min, T, sizeof(int)* (k * 2 + 2));
			results.push_back(curr_min);
			min = curr;
		
		}
		else if (min == curr) {
			int* curr_min = new int[2 * k + 2];
			memcpy(curr_min, T, sizeof(int)* (k * 2 + 2));
			results.push_back(curr_min);

		}





		q = k - 1;
		while (q >= 0) {
			P[q]++;
			if (P[q] > n) {
			
				P[q] = 1;
				q--;
			}
			else break;
		
		
		
		
		}
	
	
	
	} while (q >= 0);

	print_results(results, 2*k+2);
	printf("\n Cost is : %d \n", min);
	for (int* tmp : results) delete[]tmp;


	delete[] T;
	delete[] P;

}
int main() {


	variation_with_repetition(10,8);


	return 0;
}
