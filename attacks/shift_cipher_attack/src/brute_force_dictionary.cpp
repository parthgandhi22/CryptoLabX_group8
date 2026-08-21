#include<iostream>
#include<fstream>
using namespace std;


string decrypt(string text, int key){
    string plaintext="";
    for (auto &it:text){
        if (it>='a' && it<='z'){
            plaintext+=(it-'a'-key+26)%26+'a';
        }

        else if (it>='A' && it<='Z'){
            plaintext+=(it-'A'-key+26)%26+'A';
        }
        else if (it==' ') plaintext+=' ';
    }

    return plaintext;
}

bool isword(string word){
    ifstream file ("../dictionary/englist_words.txt");
    string dictword;

    while(file>>dictword){
        if (word==dictword) return true;
    }

    return false;
}

int score(string text){
    string word="";
    int score=0;

    for (auto &it:text){
        if (it!=' ') word+=it;
        else if (it==' '){
            if (isword(word)) score++;
            word="";
        }
    }
    
    if (word!="" && isword(word)) return score+1;
    return score;
}


int main(){

    string ciphertext;
    cout<<"Enter ciphertext: ";
    getline(cin,ciphertext);

    int bestscore=-1;
    int bestkey=-1;

    for (int key=0;key<26;key++){
        string plaintext=decrypt(ciphertext,key);

        int thisscore=score(plaintext);
        if (thisscore>bestscore){
            bestscore=thisscore;
            bestkey=key;
        }
    }

    cout<<"Best key came at: "<<bestkey<<endl;
    string plaintext="";
    for (auto &it:ciphertext){
        if (it>='a' && it<='z'){
            plaintext+=(it-'a'-bestkey+26)%26+'a';
        }

        else if (it>='A' && it<='Z'){
            plaintext+=(it-'A'-bestkey+26)%26+'A';
        }
        else if (it==' ') plaintext+=' ';
    }

    cout<<"Plaintext using brute force: "<<plaintext<<endl;




}