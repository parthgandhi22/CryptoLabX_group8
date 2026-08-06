#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>

using namespace std;

void analyzeFile(string filename)
{
    ifstream file("datasets/" + filename);

    if (!file){
        cout<<"File not found."<<endl;
        return;
    }

    string line;
    int characters=0, words=0, lines=0;
    map<char, int> frequency;
    set<char> uniquechars;

    while (getline(file, line)) {

        lines++;
        characters+=line.length() ;

        string word = "";

        for (char c:line){

            uniquechars.insert(c);

            if (isalpha(c)) frequency[tolower(c)]++;

            if (isspace(c)) {

                if (word!="") {
                    words++;
                    word="";
                }
            }

            else{
                word+=c;
            }
        }

        if (word!="")
            words++;
    }

    cout<<"\n----- File Analysis -----"<<endl;
    cout<<"Characters       : " << characters << endl;
    cout<<"Words            : " << words << endl;
    cout<<"Lines            : " << lines << endl;
    cout<<"Unique Characters: " << uniquechars.size() << endl;

    cout << "\nLetter Frequency" << endl;
    for (auto x:frequency) {
        cout << x.first << " : " << x.second << endl;
    }

    file.close();
}

int main()
{
    string filename;
    cout << "Enter filename: ";
    cin >> filename;

    analyzeFile(filename);

    return 0;
}