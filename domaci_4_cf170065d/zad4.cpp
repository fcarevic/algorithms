#include <iostream>
#include <cmath>
#include <iomanip>
#define J1 0
#define J2 1
#define PRECISION 14

double find_zero(double a, double b, int order, double precision) {
			precision = pow(10.0, precision);
			double last = b+1;
			double curr = a-1;
			double left_val = std::sph_bessel(order, a);
			double right_val= std::sph_bessel(order, b);
			while (std::abs((curr-last)*precision) >=1  ) {
				last = curr;
				curr = (a + b) / 2;
				double curr_val= std::sph_bessel(order, curr);
				if (curr_val == 0) break;
				if (left_val * curr_val<0) {
					right_val = curr_val;
					b = curr;
				}
				else {
					left_val = curr_val;
					a = curr;
				}
			}
			return curr;


}

int main() {
	double points[][2][2] = { 
		{ {4,6},
		  {6,8}
		},
		
		{	{4,6},
	        {8, 10}
	    }
	};
	
	for (int i = 0; i < 2; i++) {
		
		std::cout << "J" << i + 1 << std::endl;
		for (int j = 0; j < 2; j++) {
			std::cout << "\t Zero between (a,b) = (" << points[i][j][0] << " , " << points[i][j][1] << ")  is  x = " << std::setprecision(PRECISION)<< find_zero(points[i][j][0], points[i][j][1], i+1, 12) << std::endl;
		}
	}




	return 0;
}