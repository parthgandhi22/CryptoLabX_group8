#include <iostream>
#include <string>
using namespace std;

double english[26] =
{
    8.167, 1.492, 2.782, 4.253, 12.702,
    2.228, 2.015, 6.094, 6.966, 0.153,
    0.772, 4.025, 2.406, 6.749, 7.507,
    1.929, 0.095, 5.987, 6.327, 9.056,
    2.758, 0.978, 2.360, 0.150, 1.974,
    0.074
};

string decrypt(string text, int key)
{
    string result = "";

    for (int i = 0; i < text.length(); i++)
    {
        char ch = text[i];

        if (ch >= 'a' && ch <= 'z')
        {
            ch = (ch - 'a' - key + 26) % 26 + 'a';
        }
        else if (ch >= 'A' && ch <= 'Z')
        {
            ch = (ch - 'A' - key + 26) % 26 + 'A';
        }

        result += ch;
    }

    return result;
}

double calculateChiSquare(string text)
{
    int count[26] = {0};
    int total = 0;

    for (int i = 0; i < text.length(); i++)
    {
        char ch = text[i];

        if (ch >= 'a' && ch <= 'z')
        {
            count[ch - 'a']++;
            total++;
        }
        else if (ch >= 'A' && ch <= 'Z')
        {
            count[ch - 'A']++;
            total++;
        }
    }

    if (total == 0)
    {
        return 999999;
    }

    double chi = 0;

    for (int i = 0; i < 26; i++)
    {
        double expected = english[i] * total / 100.0;

        double difference = count[i] - expected;

        chi = chi + (difference * difference) / expected;
    }

    return chi;
}

int main()
{
    string ciphertext;

    cout << "Enter ciphertext: ";
    getline(cin, ciphertext);

    int bestKey = 0;
    double bestScore = 999999;
    string bestText = "";

    for (int key = 0; key < 26; key++)
    {
        string plaintext = decrypt(ciphertext, key);

        double currentScore =
            calculateChiSquare(plaintext);
        if (currentScore < bestScore)
        {
            bestScore = currentScore;
            bestKey = key;
            bestText = plaintext;
        }
    }

    cout << "\nBest Result\n";
    cout << "Key: " << bestKey << endl;
    cout << "Plaintext: " << bestText << endl;
    cout << "Chi-Square Score: " << bestScore << endl;

    return 0;
}