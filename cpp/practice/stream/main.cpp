#include "iostream"

using namespace std;

int main() {
    cout << "Soroush" << endl; // Soroush

    int number;
    cin >> number; // read int until white space
    cout << "number is " << number << endl;
    // in "1" -> out "1"
    // in "1  2  3" -> out "1"
    // in "   1  2  3" -> out "1"

    int num1;
    int num2;
    cout << "Enter number1" << endl;
    cin >> num1;
    cout << "Enter number2" << endl;
    cin >> num2;
    cout << "num1:" << num1 << "num2:" << num2 << endl;
    // in1 : 100
    // in2 : 200
    // out : 100 200

    // in1 : 100 200 input stream buffer
    // out : 100 200


}
