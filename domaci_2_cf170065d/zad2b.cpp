#include <iostream>
#include <algorithm>
#include <utility>
#include <cstring>
using namespace std;


struct S {
	double x;
	double y;
	int pos;
	S(double x_, double y_, int pos_) : x(x_), y(y_), pos(pos_) {}
	S() = default;
	bool operator< (S& s2) {
		return pos < s2.pos;
	}
	friend std::ostream& operator<<(std::ostream& out, const  S& s);

};

std::ostream& operator<<(std::ostream& out, const  S& s) {
	out << s.pos << "(" << s.x << "," << s.y << ")";
	return out;
}

double coords[] = { 62.0, 58.4,
					57.5, 56.0,
					51.7, 56.0,
					67.9, 19.6,
					57.7, 42.1,
					54.2, 29.1,
					46.0, 45.1,
					34.7, 45.1,
					45.7, 25.1,
					34.7, 26.4,
					28.4, 31.7,
					33.4, 60.5,
					22.9, 32.7,
					21.5, 45.8,
					15.3, 37.8,
					15.1, 49.6,
					9.1, 52.8,
					9.1, 40.3,
					2.7, 56.8,
					2.7, 33.1
};

#define MAX_NUM sizeof(coords) / sizeof(double) 


void init_data(S* array, int num_of_data) {

	for (int i = 0, j = 0; i < MAX_NUM && j < num_of_data; i += 2, j++) {
		array[j] = S(coords[i], coords[i + 1], j + 1);
	}
}

double calc_cost(S* array, int num) {
	double s = 0;
	for (int i = 0; i < num - 1; i++) {
		s += sqrt((array[i].x - array[i + 1].x)*(array[i].x - array[i + 1].x) + (array[i].y - array[i + 1].y)*(array[i].y - array[i + 1].y));
	}
	return s;
}


void shortest_path(S* array, int num, S** final) {
	double min = calc_cost(array, num);
	S* final_array = *final;
	memcpy(final_array, array, num * sizeof(S));
	while (next_permutation(array, array + num)) {
		double curr_dist = calc_cost(array, num);
		if (curr_dist < min) {
			min = curr_dist;
			memcpy(final_array, array, num * sizeof(S));

		}
	}
}





int main() {
	int num = 12;

	S* array = new S[num];
	S* final_arr = new S[num];
	init_data(array, num);
	shortest_path(array, num, &final_arr);
	cout << "Shortest path is" << endl;
	for (int i = 0; i < num; i++) {
		cout << final_arr[i] << "\t";
	}
	cout << endl;
	cout << "Distance required: " << calc_cost(final_arr, num) << endl;
	delete[] array;
	delete[] final_arr;

	return 0;
}