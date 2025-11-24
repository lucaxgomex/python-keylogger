# Python Keylogger (Educational & Authorized Use Only)

## 🔗 Overview
This project is an educational example demonstrating how keyboard and mouse event listeners can be implemented in Python for **authorized**, **ethical**, and **research‑oriented purposes only**.

It consists of a small set of scripts that capture keystrokes and monitor mouse position, storing the output in a local text file.

This code must only be used with explicit permission from the device owner and strictly for legitimate purposes, such as cybersecurity training, usability testing, or academic study.

## 🤖 Introduction
A **keylogger** is a tool designed to record user input from a keyboard. While keyloggers are commonly associated with malicious activity, they also serve **legitimate uses**, including:

- Security research and threat‑analysis training;

- Forensic investigations (with proper legal authorization);

- Monitoring and debugging user interfaces;

- Accessibility and usability studies.

Because keyloggers can collect sensitive information, it is essential that this project is used **only in controlled, fully authorized environments**. Unauthorized use is illegal and unethical.

## 🖥️ Project Structure
```
keylogger/
│
├── main.py
│   The primary script responsible for listening to keystrokes and
│   forwarding them to the log file.
│
├── log.txt
│   The text file where all logged keyboard events are stored.
│   It is generated and updated by main.py.
│
└── listen.py
    A helper script used to track the current mouse position on the screen.
```

You can execute it by typing, on your command line shell, in case you are running some Linux distro:

```python
python3 main.py
```
Or, in caso you are using Windows:
```
python main.py
```

## 🫂 Contributing
Contributions are welcome under the terms of the **MIT License**, which allows modification, redistribution, and commercial use with proper attribution.

Ethical guidelines for contributing:

- Do not submit features that facilitate covert, unlawful, or harmful surveillance;

- Focus on improvements related to:

    - Logging transparency;

    - Security, auditing, and consent mechanisms;

    - Code clarity and reliability;

    - Cross‑platform compatibility;

    - Testing and documentation;

- Clearly label any experimental or sensitive features;

- Ensure all additions comply with privacy laws and ethical best practices.

To contribute:

1. Fork the repository;

2. Create a descriptive branch for your feature or fix;

3. Submit a pull request with a detailed explanation of your changes.

## ⚠️ Watch Out!

### **Ethical and Legal Disclaimer**

This tool is provided **strictly for educational, research, and ethical cybersecurity purposes only**. It is intended to help students, security professionals, and developers better understand input‑logging mechanisms in controlled and fully authorized environments.

Unauthorized or malicious use of keyloggers or any similar monitoring tools is **illegal**, **unethical**, and may result in severe consequences, including:

* Violation of privacy laws;
* Criminal prosecution;
* Civil liability;
* Permanent damage to professional reputation.

By using this project, you agree to operate it **only with explicit permission** from the system owner and in compliance with all applicable local, state, federal, and international laws. Misuse of this software is solely the responsibility of the user.
