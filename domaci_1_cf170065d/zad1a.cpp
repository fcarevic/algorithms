#include <iostream>
using namespace std;
#define MAX 711

bool check(int a, int b, int c, int d) {
	return (a + b + c + d) == MAX && a*b*c*d == MAX * 1000000;

}


void a() {
	cout << endl;
	cout << endl;

	double num = 0;
	for (int a = 1; a < MAX; a++)
		for (int b = 1; b < MAX; b++)
			for (int c = 1; c < MAX; c++)
				for (int d = 1; d < MAX; d++) {
					num++;
					if (check(a, b, c, d)) {
						cout << "Resenje pod a je: a= " << a / 100.0 << " \t b=" << b / 100.0 << " \t c=" << c / 100.0 << " \t d=" << d / 100.0 << endl;
						cout << "Broj poziva optimizacione fje pod a je " << num << endl;
						return;
					}
				}
}


int main() {
	a();

	return 0;
}