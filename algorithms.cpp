
void variation_with_repetition(int n, int k) {   // values of elements in array start from 0, in printf type p[i]+1
	int q;
	int* P = new int[k];
	for (int i = 0; i < k; i++)
		P[i] = 0;  //in order to start from 1, change statement to  p[i]=1

	do {
			//some processing
		q = k - 1;
		while (q >= 0) {
			P[q]++;
			if (P[q] == n) {    // in order to start from 1, change condition to  p[q]>n

				P[q] = 0;		//in order to start from 1, change statement to    p[q]=1
				q--;
			}
			else break;




		}



	} while (q >= 0);

}


void usage_example_of_sequenceToSpanningTree(){ // values of array elements start from 1
//array T comes in form 1-1 , 2-3, 4-5, where first num represents node, second one represents neighbour
	
    int P[] = {3,3,4,5,5,6};
    int len = sizeof(P)/ sizeof(int);
    int * T = new int[2*len+2];
    sequenceToSpanningTree(P, len, T);
    for(int i = 0 ;  i < 2*len+2;i++){
        
        printf(" %d", T[i]);
        if((i+1)%2==0)
        printf("-");
    }
  
  delete [] T;
    
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

