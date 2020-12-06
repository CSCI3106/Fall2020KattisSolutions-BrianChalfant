/*
# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
*/
#include <iostream>
using namespace std;
int main() {
    int x, y, n;
    cin >> x;
    cin >> y;
    cin >> n;
    for (size_t i = 1; i < n + 1; i++)
    {
        if (i% y == 0 && i % x == 0){
            cout << "FizzBuzz" << endl;
        }
        else if (i % y == 0) {
            cout << "Buzz" << endl;
        }
        else if (i % x == 0)
        {
            cout << "Fizz" << endl;
        }
        else {
            cout << i << endl;
        }
    }

}