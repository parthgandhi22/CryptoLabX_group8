#include <iostream>
#include "utils/logger.h"
using namespace std;

void showMenu() {
    cout << "\n========== CryptoLabX ==========" << endl;
    cout << "1. Encrypt" << endl;
    cout << "2. Decrypt" << endl;
    cout << "3. Attack" << endl;
    cout << "4. Analyze" << endl;
    cout << "5. Exit" << endl;
    cout << "===============================" << endl;
}

int main() {
    int choice;

    while (true) {

        showMenu();

        cout << "Enter your choice (1-5): ";
        cin >> choice;

        if (choice == 1){
            cout << "\nEncrypt: Coming Soon..." << endl;
            writeLog("Encrypt");
        } 
        
        else if (choice == 2){
            cout << "\nDecrypt: Coming Soon..." << endl;
            writeLog("Decrypt");
        } 
        
        else if (choice == 3){
            cout << "\nAttack: Coming Soon..." << endl;
            writeLog("Attack");
        } 
        
        else if (choice == 4){
            cout << "\nAnalyze: Coming Soon..." << endl;
            writeLog("Analyze");
        } 
        
        else if (choice == 5) {
            cout << "\nThank you for using CryptoLabX!" << endl;
            writeLog("Closed!");
            break;
        }

        else{
            cout << "\nInvalid choice! Please enter a number between 1 and 5." << endl;
        }
            
    }

    return 0;
}