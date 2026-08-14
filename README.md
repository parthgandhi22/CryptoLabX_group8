# CryptoLabX

A C++-based cryptography laboratory project originally developed to implement and analyze classical and modern cryptographic algorithms, cryptanalysis techniques, and text analysis utilities.

As part of the Secure Applications / SAST assignment, the project was extended with a small **Flask-based E-Commerce Web Application** to demonstrate core web application functionalities and common security vulnerabilities. The application was analyzed using **SonarQube** as a Static Application Security Testing (SAST) tool.

---

## Team Members

* Parth Gandhi
* Lokesh Garg

---

## Project Description

CryptoLabX is a modular project designed for learning and experimenting with cryptographic concepts. The original project includes implementations of classical and modern encryption algorithms, attack techniques, mathematical utilities, and text analysis tools.

For the Secure Applications assignment, an additional e-commerce web application was developed under the `secure_applications` module.

The e-commerce application implements only the core functionalities required for the assignment rather than attempting to create a complete commercial website.

The application was also analyzed using **SonarQube** to identify security, reliability, and maintainability issues in the source code.

---

# Part 1 — Original Cryptography Laboratory

## Cryptography Features

The original CryptoLabX project includes modules for:

### Text Analysis

* Character Count
* Word Count
* Line Count
* Letter Frequency Analysis
* Unique Character Count

### Cryptographic Modules

The project is organized into separate modules for:

* Classical Cryptography
* Modern Cryptography
* Cryptanalysis / Attacks
* Mathematical Utilities
* Text Analysis

### Logging Utility

The project includes a logging utility that:

* Records user actions
* Maintains execution history
* Stores logs in `utils/logs.txt`

---

## Original Project Structure

```text
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

## Original Requirements

* C++11 or later
* GCC / Clang / MSVC Compiler
* Visual Studio Code (Recommended)

---

## Original Compilation

Compile the C++ project using:

```bash
g++ main.cpp utils/logger.cpp analysis/text_analysis.cpp -o CryptoLabX
```

Run:

```bash
./CryptoLabX
```

---

## Original Menu

```text
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

The `datasets/` folder contains sample text files used for testing encryption, decryption, attacks, and text analysis.

---

# Part 2 — Secure Applications E-Commerce Website

## E-Commerce Application

For the Secure Applications assignment, CryptoLabX was extended with a small **E-Commerce Website** implemented using Flask and SQLite.

The application is designed according to the assigned application:

> **Application 8 — E-Commerce Website**

The objective is to implement the core functionalities required to demonstrate web application security concepts rather than developing a complete commercial e-commerce platform.

---

## Core Functionalities

### 1. Product Browsing

Users can browse available products and view information such as:

* Product name
* Product description
* Product price

### 2. Shopping Cart

Users can:

* Add products to the cart
* View products in the cart
* Modify product quantities
* View the calculated cart total

### 3. Checkout

Users can proceed to checkout and place an order by providing the required information.

### 4. Order History

Users can view previously placed orders and their associated details.

---

## Security Vulnerabilities

The assignment provides the following vulnerabilities from which any three can be demonstrated:

* **SQL Injection**
* **Cross-Site Scripting (XSS)**
* **IDOR (Insecure Direct Object Reference)**
* **File Upload Vulnerability**
* **Price Manipulation due to Poor Validation**

The selected vulnerabilities are intentionally included for educational and security-testing purposes.

---

## Vulnerability Descriptions

### SQL Injection

A vulnerability that occurs when user-controlled input is directly incorporated into SQL queries without proper parameterization or validation.

It can potentially allow an attacker to manipulate database queries and access or modify unauthorized data.

### Cross-Site Scripting (XSS)

A vulnerability where untrusted user input is rendered in a web page without appropriate output encoding or sanitization, potentially allowing malicious scripts to execute in another user's browser.

### IDOR

Insecure Direct Object Reference occurs when an application exposes references such as order IDs without properly checking whether the current user is authorized to access the referenced object.

### File Upload Vulnerability

Occurs when an application accepts uploaded files without sufficiently validating their type, content, size, filename, or storage location.

### Price Manipulation

Occurs when the application trusts a price supplied by the client instead of retrieving the authoritative product price from the server-side database.

---

# Technology Stack

## Original Project

* **Language:** C++
* **Standard:** C++11 or later
* **Compiler:** GCC / Clang / MSVC
* **IDE:** Visual Studio Code

## E-Commerce Application

* **Language:** Python
* **Framework:** Flask
* **Database:** SQLite
* **Frontend:** HTML
* **Styling:** CSS
* **SAST Tool:** SonarQube
* **Containerization:** Docker
* **Development Environment:** Visual Studio Code

---

# E-Commerce Project Structure

```text
secure_applications/
│
├── src/
│   │
│   ├── static/
│   │   └── style.css
│   │
│   ├── templates/
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── orders.html
│   │   └── products.html
│   │
│   ├── app.py
│   ├── assign2.py
│   ├── ecommerce.db
│   └── sonar-project.properties
│
├── outputs/
│   ├── cart.png
│   ├── checkout.png
│   └── shop.png
│
├── sast/
│   ├── SonarQubeissues.png
│   └── SonarQubeissues2.png
│
├── tests/
│
└── ...
```

---

# Running the E-Commerce Application

Navigate to the application source directory:

```bash
cd secure_applications/src
```

Install the required dependencies:

```bash
pip install flask
```

Run the Flask application:

```bash
python app.py
```

The application runs locally at:

```text
http://127.0.0.1:5000
```

---

# SonarQube Static Analysis

The Flask application was analyzed using **SonarQube** running through Docker.

The SonarQube project configuration is:

```properties
sonar.projectKey=Crypto_lab
sonar.projectName=Crypto_lab
sonar.sources=.
sonar.sourceEncoding=UTF-8
```

The source code was analyzed using the SonarScanner Docker image and submitted to the local SonarQube server.

---

## SonarQube Analysis Results

The latest analysis reported:

* **374 Lines of Code**
* **17 Total Issues**
* **3 Security Issues**
* **8 Reliability Issues**
* **6 Maintainability Issues**
* **0.0% Test Coverage**
* **0.0% Code Duplication**

### Security

SonarQube reported:

```text
3 Open Security Issues
Security Rating: D
```

### Reliability

SonarQube reported:

```text
8 Open Reliability Issues
Reliability Rating: C
```

### Maintainability

SonarQube reported:

```text
6 Open Maintainability Issues
```

### Test Coverage

The current analysis reports:

```text
0.0% Coverage
```

The configured Quality Gate requires at least:

```text
80.0% Coverage
```

Therefore, the coverage condition currently fails.

### Code Duplication

The analysis reports:

```text
0.0% Duplication
```

---

# SonarQube Quality Gate

The current project Quality Gate is reported as **Failed**.

The main conditions shown in the analysis include:

* New issues are present
* Test coverage is below the required threshold

The Quality Gate result is used to demonstrate the outcome of static analysis and does not mean that the application itself cannot run.

---

# SAST Analysis Workflow

The security analysis process used for the project can be summarized as:

```text
E-Commerce Flask Application
          ↓
      Source Code
          ↓
     SonarScanner
          ↓
       SonarQube
          ↓
 ┌───────────────────────┐
 │ Security              │
 │ Reliability           │
 │ Maintainability       │
 │ Code Coverage         │
 │ Code Duplication      │
 └───────────────────────┘
```

---

# Purpose of the Project

The purpose of this project is to demonstrate both software functionality and application security concepts in an academic environment.

The original CryptoLabX project provides implementations and utilities related to cryptography, while the Secure Applications module demonstrates how security vulnerabilities can occur in a web-based e-commerce application.

The project also demonstrates how a **Static Application Security Testing (SAST)** tool such as SonarQube can be used to analyze source code and identify potential security and code-quality issues.

---

# Educational Purpose

This project was developed for educational purposes as part of the **Cryptography Lab / Secure Applications coursework**.

The vulnerabilities included in the e-commerce application are intentionally introduced for controlled security testing and demonstration.

The application is not intended to be deployed as a production e-commerce system.

---

# License

This project is developed for educational purposes as part of the Cryptography Lab course **(22CPP307)**.
