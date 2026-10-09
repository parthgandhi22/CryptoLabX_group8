# CryptoLabX – Cryptography Lab Assignments

## Overview

CryptoLabX is a collection of cryptography laboratory assignments covering classical encryption algorithms, cryptanalysis techniques, and vulnerabilities in modern cryptographic systems. The repository focuses on implementing encryption and decryption algorithms, analyzing ciphertext, recovering plaintext, and understanding cryptographic security.

## Assignment 4: Shift Cipher and Its Cryptanalysis

### Objective

To implement the Shift Cipher and perform cryptanalysis using brute force, dictionary scoring, and Chi-Square analysis.

### Methods Used

1. Shift Cipher encryption and decryption.
2. Brute-force attack by testing possible keys.
3. Dictionary scoring to identify meaningful English plaintext.
4. Chi-Square analysis using English letter frequencies.
5. Comparison of dictionary scoring and Chi-Square key predictions.
6. Failure analysis and evaluation of attack effectiveness.
7. Experimental observations and verification.

### Implementation

The assignment includes the following modules:

- `shift_cipher.py`
- `brute_force_dictionary.py`
- `chi_square_attack.py`
- `main.py`

### Laboratory Report

The report documents both cryptanalysis algorithms, compares the predicted keys, analyzes failed attacks, records experimental observations, and summarizes the effectiveness of the techniques.

**Repository Directory:** `attacks/shift_cipher_attack/`

---

## Assignment 5: Monoalphabetic Substitution Cipher and Its Cryptanalysis

### Objective

To implement a Monoalphabetic Substitution Cipher and recover the plaintext using frequency analysis, word patterns, and iterative substitution.

The plaintext must be selected from *Modern Cryptography* by Katz and Lindell, using the page assigned to the group: page number = group number + 30.

### Methods Used

1. Monoalphabetic substitution encryption.
2. Letter-frequency analysis of the ciphertext.
3. Frequency counts, percentage frequencies, and descending frequency ranking.
4. Word-frequency analysis.
5. Analysis of one-letter, two-letter, and three-letter words.
6. Detection of repeated words and repeated letter patterns.
7. Iterative recovery of plaintext using candidate substitutions.
8. Examination of partial plaintext and rejection of incorrect hypotheses.
9. Recovery of the substitution key.
10. Validation by re-encrypting the recovered plaintext.

### Required Functions

- `frequency_analysis()`
- `word_frequency_analysis()`
- `pattern_analysis()`
- `apply_substitution()`
- `display_partial_plaintext()`
- `verify_solution()`

### Laboratory Documentation

The laboratory notebook should contain the algorithm, experimental observations, candidate substitutions, substitutions tested, results, decisions, and justification for the cryptanalytic choices.

**Repository Directory:** `attacks/monoalphabetic_substitution_cipher/`

---

## Assignment 6: Cryptanalysis of Vigenère Cipher Using Kasiski Examination and Frequency Analysis

### Objective

To recover the Vigenère cipher key and decrypt the assigned ciphertext using Kasiski Examination and frequency analysis.

### Assignment Details

- **Group Number:** 8
- **Ciphertext:** Ciphertext-2 (Even Group Numbers)

### Methods Used

1. Ciphertext preprocessing.
2. Repeated-pattern detection.
3. Distance calculation between repeated patterns.
4. Factor analysis.
5. Kasiski Examination for estimating key length.
6. Index of Coincidence (bonus).
7. Ciphertext grouping according to the estimated key length.
8. Frequency analysis.
9. Caesar shift estimation.
10. Key recovery.
11. Vigenère decryption.
12. Vigenère re-encryption.
13. Verification of the recovered plaintext and key.

### Required Functions

- `clean_ciphertext()`
- `find_repeated_patterns()`
- `calculate_distances()`
- `find_factors()`
- `kasiski_analysis()`
- `calculate_ic()`
- `split_into_groups()`
- `frequency_analysis()`
- `find_shift()`
- `find_key()`
- `vigenere_decrypt()`
- `vigenere_encrypt()`
- `verify()`

### Verification

The recovered key and plaintext are verified by re-encrypting the plaintext and comparing the resulting ciphertext with the original ciphertext.

**Repository Directory:** `attacks/vigenere_kasiski/`

---

## Assignment 7: Padding Oracle Attack on AES-CBC

### Objective

To understand and demonstrate how a Padding Oracle Attack can recover plaintext from an AES-CBC encrypted message without knowing the AES encryption key.

### Concepts Covered

1. AES-CBC encryption and decryption.
2. Initialization Vector (IV).
3. PKCS#7 padding and padding validation.
4. Padding oracle implementation.
5. Modification of the previous ciphertext block.
6. Oracle queries and their responses.
7. Recovery of intermediate bytes and plaintext bytes from right to left.
8. Recovery of plaintext across multiple ciphertext blocks.
9. Removal of padding from the recovered plaintext.
10. Counting and analyzing oracle queries.
11. Security recommendations for preventing padding oracle vulnerabilities.

### Attack Methodology

The program encrypts a message using AES-CBC and PKCS#7 padding. The padding oracle simulates a system that reveals whether decrypted data has valid padding. By modifying the previous ciphertext block and observing the oracle's responses, the attack recovers plaintext bytes without accessing the AES key.

The attack is implemented without using a ready-made padding-oracle attack library.

### Security Recommendations

- Prefer authenticated encryption, such as AES-GCM.
- Verify authentication before accepting decrypted plaintext.
- Avoid distinguishable responses for valid and invalid padding.
- Handle decryption failures securely and avoid exposing padding-validation details.

**Repository Directory:** `attacks/padding_oracle_attack/`

---

## Repository Structure

```text
CryptoLabX/
├── attacks/
│   ├── monoalphabetic_substitution_cipher/
│   ├── padding_oracle_attack/
│   │   └── src/
│   │       └── main.py
│   ├── shift_cipher_attack/
│   │   ├── src/
│   │   │   ├── shift_cipher.py
│   │   │   ├── brute_force_dictionary.py
│   │   │   ├── chi_square_attack.py
│   │   │   └── main.py
│   │   ├── dictionary/
│   │   ├── testcases/
│   │   ├── outputs/
│   │   ├── screenshots/
│   │   └── reports/
│   │       └── Assignment_4_Report.pdf
│   ├── shift_cipher_attack/
│   └── vigenere_kasiski/
├── README.md
└── ...
```

The structure is illustrative. Retain the existing repository files and folders, and remove duplicate entries or add directories as appropriate for the actual implementation.

---

## Technologies and Techniques

### Cryptographic Algorithms

- Shift Cipher
- Monoalphabetic Substitution Cipher
- Vigenère Cipher
- AES-CBC

### Cryptanalysis Techniques

- Brute-force search
- Dictionary scoring
- Chi-Square analysis
- Letter-frequency analysis
- Word and pattern analysis
- Kasiski Examination
- Index of Coincidence
- Caesar shift estimation
- Padding Oracle Attack

### Tools and Libraries

- Python and other programming languages where permitted by the assignment.
- Standard cryptographic libraries for the required encryption and decryption operations.
- Git and GitHub for version control and repository management.

---

## Learning Outcomes

These assignments demonstrate how cryptographic algorithms work and how their weaknesses can be analyzed.

- Understand classical cipher encryption and decryption.
- Apply statistical and pattern-based methods to recover plaintext.
- Estimate and recover cipher keys using cryptanalysis.
- Understand CBC mode, padding, and padding oracle vulnerabilities.
- Validate implementations through re-encryption and experimental analysis.
- Document algorithms, observations, and security recommendations.
- Maintain a structured repository and meaningful Git commit history.

## Conclusion

CryptoLabX brings together classical cryptanalysis and a modern cryptographic attack. Assignments 4–6 focus on recovering plaintext or keys from classical ciphers, while Assignment 7 demonstrates how an implementation-level vulnerability can compromise confidentiality even when AES itself remains secure.

The assignments emphasize algorithmic understanding, systematic experimentation, verification, and secure cryptographic implementation.
