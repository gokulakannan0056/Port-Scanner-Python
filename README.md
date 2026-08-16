# Port Scanner (Python)

## Overview

This project is a simple **Python-based port scanner** developed for cybersecurity learning and security research.

It checks TCP ports on a specified host and identifies ports that are accepting connections. The project demonstrates the basic concept of network port scanning.

## Objectives

* Understand how TCP ports work.
* Learn the basic concept of port scanning.
* Identify open ports on an authorized system.
* Understand how port scanning can be used during security assessment.
* Practice Python socket programming.

## Technologies Used

* **Python**
* **Socket Programming**
* **datetime**

## Features

* Accepts an IP address or hostname.
* Allows the user to specify a port range.
* Checks TCP ports.
* Identifies open ports.
* Attempts to identify the associated service.
* Displays the scan results in the terminal.

## How to Run

Make sure Python 3 is installed.

Run:

```bash
python port_scanner.py
```

Enter a target when prompted.

For safe testing on your own computer, use:

```text
127.0.0.1
```

You can then enter a small port range, such as:

```text
Starting port: 1
Ending port: 100
```

## Example

```text
Port Scanner
----------------------------------------
Target: 127.0.0.1
----------------------------------------
Port 80: OPEN (http)
Port 443: OPEN (https)
----------------------------------------
Scan completed.
```

The exact results depend on which services are running on the target system.

## Project Structure

```text
Port-Scanner-Python/
├── README.md
└── port_scanner.py
```

## Security and Ethical Considerations

This project is intended for **educational purposes and authorized security testing**.

Only scan systems that you own or have explicit permission to test. Unauthorized port scanning may violate organizational policies or applicable laws.

## Future Improvements

* Add multithreaded scanning.
* Add a progress indicator.
* Add service/version detection.
* Add result export to a file.
* Add a graphical user interface.
* Add timeout configuration.

## Disclaimer

This project is created for cybersecurity education and authorized security research. The developer is not responsible for misuse of this tool.
