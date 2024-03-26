#include<iostream>
using namespace std;

bool isMultiple(int a, int b) { //함수 선언
	if (b % a == 0) return true;
	else return false;
}
int main() {

	int a;
	int b;
	bool n;
	cout << "두 정수 입력:" << endl;
	cin >> a >> b;
	n = isMultiple(a, b);
	if (b % a == 0)
		cout << "yes" << endl;
	else
		cout << "no" << endl;



}
