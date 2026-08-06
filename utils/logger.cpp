#include <iostream>
#include <fstream>
#include <ctime>
#include <string>
#include "logger.h"
using namespace std;

void writeLog(string option) {

    ofstream file("utils/logs.txt",ios::app);

    if (!file) {
        cout << "File cannot be opened!" << endl;
        return;
    }

    time_t now=time(NULL);

    file << ctime(&now) << " - " << option << endl;

    file.close();
}