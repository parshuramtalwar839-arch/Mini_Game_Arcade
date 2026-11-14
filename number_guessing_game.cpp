// Mini Game Arcade - Number Guessing Game
// Beginner C++ project using variables, loops, conditions and random numbers.

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(static_cast<unsigned int>(time(0)));

    int secretNumber = rand() % 100 + 1;
    int guess;
    int attempts = 0;

    cout << "================================" << endl;
    cout << "       NUMBER GUESSING GAME" << endl;
    cout << "================================" << endl;
    cout << "I have chosen a number from 1 to 100." << endl;
    cout << "Try to guess it!" << endl;

    do {
        cout << "\nEnter your guess: ";
        cin >> guess;
        attempts++;

        if (guess < secretNumber) {
            cout << "Too low! Try a bigger number." << endl;
        } else if (guess > secretNumber) {
            cout << "Too high! Try a smaller number." << endl;
        } else {
            cout << "Correct! You guessed the number." << endl;
            cout << "Number of attempts: " << attempts << endl;
        }
    } while (guess != secretNumber);

    cout << "Thanks for playing!" << endl;
    return 0;
}
