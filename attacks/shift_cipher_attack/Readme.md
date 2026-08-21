# Assignment 4 — Shift Cipher Cryptanalysis

## Group Members

- Lokesh
- Parth

## Objective

The objective of this assignment is to perform cryptanalysis of a Shift Cipher using:

1. Brute Force
2. Dictionary Scoring
3. Chi-Square Analysis

The attacks attempt to recover the encryption key and plaintext without directly knowing the key.

## Shift Cipher

A Shift Cipher encrypts each alphabetic character by shifting it by a fixed number of positions.

### Encryption

C = (P + K) mod 26

### Decryption

P = (C - K + 26) mod 26

Where:

- P = Plaintext character
- C = Ciphertext character
- K = Encryption key

Since there are 26 letters in the English alphabet, there are only 26 possible keys (0–25).

## Cryptanalysis Algorithms

### 1. Brute Force and Dictionary Scoring

The ciphertext is decrypted using every possible key from 0 to 25.

For each decrypted text:

- The text is divided into words.
- Each word is checked against an English dictionary.
- The number of matching English words is used as the score.
- The key with the highest dictionary score is selected as the predicted key.

### 2. Chi-Square Analysis

Each possible key is used to decrypt the ciphertext.

For every candidate plaintext:

- The frequency of each letter A–Z is calculated.
- The observed frequencies are compared with standard English letter frequencies.
- A Chi-Square score is calculated.

The formula used is:

χ² = Σ ((O - E)² / E)

Where:

- O = Observed frequency
- E = Expected English frequency

The key with the lowest Chi-Square value is selected as the predicted key.

## Repository Structure

```text
CryptoLabX/
└── attacks/
    └── shift_cipher_attack/
        ├── src/
        │   ├── shift_cipher.py
        │   ├── brute_force_dictionary.py
        │   ├── chi_square_attack.py
        │   └── main.py
        │
        ├── dictionary/
        │   └── english_words.txt
        │
        ├── testcases/
        │
        ├── outputs/
        │
        ├── screenshots/
        │
        ├── reports/
        │   └── Assignment_4_Report.pdf
        │
        └── README.md