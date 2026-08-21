#include<iostream>
using namespace std;

int main(){

    string plaintext;
    cout<<"Enter plaintext:";
    cin>>plaintext;

    int key;
    cout<<"Enter key:";
    cin>>key;

    string ciphertext="";
    for (auto &it:plaintext){

        if (it>='a' && it<='z'){
            ciphertext+=(it-'a'+key)%26+'a';
        }

        else if (it>='A' && it<='Z'){
            ciphertext+=(it-'A'+key)%26+'A';
        }
    }

    cout<<"Cipher text:"<<ciphertext<<endl;


}