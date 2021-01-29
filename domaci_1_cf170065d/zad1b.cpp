#include <iostream>
using namespace std;
#define MAX 711

bool check(int a, int b, int c, int d) {
	return (a + b + c + d) == MAX && a*b*c*d == MAX * 1000000;

}



void b() {
	cout << endl;
	cout << endl;

	int num = 0;
	for (int a = 1; a < MAX; a++)
		for (int b = 1; b < MAX; b++)
			for (int c = 1; c < MAX; c++)
			{
				num++;
				int d = MAX - a - b - c;
				if (d <= 0) continue;
				if (check(a, b, c, d)) {
					cout << "Resenje pod b je: a= " << a / 100.0 << " \t b=" << b / 100.0 << " \t c=" << c / 100.0 << " \t d=" << d / 100.0 << endl;
					cout << "Broj poziva optimizacione fje pod b je " << num << endl;
					return;
				}
			}


}


int main() {
	b();
	return 0;
}