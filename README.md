 SE333 Final Project – AI Testing Agent

Overview
This project implements an intelligent testing agent using the Model Context Protocol (MCP).  
The agent automatically generates, runs, and improves unit tests to increase code coverage for a Java calculator application.

The goal of this project is to demonstrate how AI-assisted development tools can automate parts of the software testing process and help developers improve test quality and coverage.



 Technologies Used
- Python
- Java
- Maven
- JaCoCo (Code Coverage Tool)
- Model Context Protocol (MCP)
- GitHub



 Project Structure

se333-final-project
│
├── src
│   ├── main
│   │   └── java
│   │       ├── Calculator.java
│   │       └── Main.java
│   │
│   └── test
│       └── java
│           └── CalculatorTest.java
│
├── main.py
├── server.py
├── mcp_sse_server.py
├── pom.xml
├── reflection.md
└── README.md



How the System Works

1. The AI testing agent analyzes the codebase.
2. It generates or improves unit tests for the Java calculator program.
3. Maven executes the generated tests.
4. JaCoCo collects execution data and generates a code coverage report.
5. Developers can review which parts of the code are tested and which parts still require additional tests.

This workflow demonstrates how AI tools can assist developers in improving automated software testing.



Running the Project

Run the unit tests:

mvn test

Generate the JaCoCo coverage report:

mvn jacoco:report

Open the coverage report:

open target/site/jacoco/index.html

The coverage report will show which parts of the code are covered by tests.



 Presentation Video

Project Demo Video:

https://depauledu-my.sharepoint.com/personal/mammar1_depaul_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Fmammar1%5Fdepaul%5Fedu%2FDocuments%2FAttachments%2FScreen%20Recording%202026%2D03%2D12%20at%2011%2E52%2E45%E2%80%AFPM%2Emov




