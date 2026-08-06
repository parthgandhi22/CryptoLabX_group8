# CryptoLabX

A C++-based cryptography laboratory project developed to implement and analyze classical and modern cryptographic algorithms, cryptanalysis techniques, and text analysis utilities.

---

## Team Members

- Parth Gandhi
- Lokesh Garg

---

## Project Description

CryptoLabX is a modular C++ application designed for learning and experimenting with cryptographic concepts. The project includes implementations of classical and modern encryption algorithms, attack techniques, mathematical utilities, and text analysis tools.

The project is organized into separate modules, making it easy to extend with new algorithms and utilities.

---

## Project Structure

```
CryptoLabX/
│
├── analysis/
│   └── text_analysis.cpp
│
├── attacks/
│
├── classical/
│
├── modern/
│
├── math/
│
├── utils/
│   ├── logger.cpp
│   ├── logger.h
│   └── logs.txt
│
├── datasets/
│   ├── sample_text1.txt
│   ├── sample_text2.txt
│   ├── sample_text3.txt
│   ├── sample_text4.txt
│   └── sample_text5.txt
│
├── outputs/
│
├── tests/
│
├── docs/
│
├── main.cpp
├── README.md
└── requirements.txt
```

---

## Features

- Text Analysis
  - Character Count
  - Word Count
  - Line Count
  - Letter Frequency Analysis
  - Unique Character Count

- Logging Utility
  - Records user actions
  - Maintains execution history in `logs.txt`

---

## Requirements

- C++11 or later
- GCC / Clang / MSVC Compiler
- Visual Studio Code (Recommended)

---

## Compilation

Compile the project using:

```bash
g++ main.cpp utils/logger.cpp analysis/text_analysis.cpp -o CryptoLabX
```

Run:

```bash
./CryptoLabX
```

---

## Current Menu

```
========== CryptoLabX ==========
1. Encrypt
2. Decrypt
3. Attack
4. Analyze
5. Exit
===============================
```

---

## Dataset

The `datasets/` folder contains sample text files that are used for testing encryption, decryption, attacks, and text analysis.

---

## License

This project is developed for educational purposes as part of a Cryptography Lab course(22CPP307).