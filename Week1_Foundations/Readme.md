## Week 1: Foundations  

### Overview  
This week focuses on building a strong foundation in Python programming, Mathematics for AI, and Data Structures & Algorithms (DSA).

### Highlights  
- **Python Basics**: Variables, loops, functions, OOP, and libraries like NumPy and Pandas.  
- **Mathematics**: Linear algebra, calculus, probability, and statistics.  
- **DSA**: Arrays, linked lists, trees, and fundamental sorting/searching algorithms.  
- **Project**: ThinkBoard - A Python-based web application for data analysis and visualization.  

### Project: ThinkBoard  

A Python-powered web application designed to simplify data analysis and visualization. With features like CSV uploads, statistical computations, interactive charts, and calculus functions, ThinkBoard showcases the practical application of foundational concepts.  

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Setup Guide](#setup-guide)
  - [Local Installation](#local-installation)
  - [Quick Start](#quick-start)
- [Usage](#usage)
  - [Data Upload](#data-upload)
  - [Visualization](#visualization)
  - [Sorting and Searching](#sorting-and-searching)
  - [Calculus Features](#calculus-features)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---
## Features

- **CSV Upload**: Upload and validate CSV files for seamless data analysis.
- **Analytics**: Compute mean, median, mode, max, and min for numeric columns in uploaded datasets.
- **Visualization**: Display data using bar, line, or pie charts via Chart.js.
- **Sorting & Searching**: Sort data by any column (ascending/descending) and search for substrings within columns.
- **Calculus**: Calculate numerical gradients for numeric columns using NumPy.
- **Interactive Interface**: Features smooth navigation and responsive design for usability.
- **System Design**: Modular architecture designed for scalability and reliability.

---


## Tech Stack

| Layer      | Technology                     |
|------------|--------------------------------|
| Backend    | Python, Flask, Pandas, NumPy   |
| Frontend   | HTML, Tailwind CSS, Chart.js   |
| Other      | REST API, JavaScript           |

---

## Prerequisites

Before setting up the project, ensure you have:

- **Python 3.8+** installed ([Download Python](https://www.python.org/downloads/))
- A code editor (e.g., VS Code)
- Basic knowledge of terminal commands
- Internet access for dependencies

---


## Setup Guide

### Local Installation

1. Clone the repository.  
   ```bash
   git clone https://github.com/your-username/AI-Journey.git
   cd thinkboard
   ```
2. Install dependencies.  
   ```bash
   pip install -r requirements.txt
   ```
3. Start the server.  
   ```bash
   python app.py
   ```
4. Access the app in your browser at `http://127.0.0.1:5000`.  

### Quick Start

- Upload a CSV file to explore its statistical metrics.
- Visualize data interactively with different chart types.
- Sort or search through data instantly.

---

## Usage

### Data Upload

- Click "Choose File" to upload your CSV.
- The application validates the file and displays metrics like mean, median, and mode.

### Visualization

- Select the chart type from the dropdown menu.
- Charts update dynamically based on user interaction.

### Sorting and Searching

- Use the sort functionality to order data by any column.
- Search for specific data using the query field.

### Calculus Features

- Compute numerical gradients for numeric columns and visualize results.

---

## Screenshots  

### Dashboard  
Overview of uploaded data with interactive features.  
![Dashboard](https://raw.githubusercontent.com/MuhammadTahaNasir/AI-Journey/main/Week1_Foundations/techboard/assets/dashboard.png)

### File Upload  
Upload your CSV files for quick analysis.  
![File Upload](https://raw.githubusercontent.com/MuhammadTahaNasir/AI-Journey/main/Week1_Foundations/techboard/assets/upload_feature.png)

### Data Visualization  
Customizable charts to explore your data.  
![Data Visualization](https://raw.githubusercontent.com/MuhammadTahaNasir/AI-Journey/main/Week1_Foundations/techboard/assets/visualization.png)

### Sorting and Searching  
Sort and search data efficiently.  
![Sorting and Searching](https://raw.githubusercontent.com/MuhammadTahaNasir/AI-Journey/main/Week1_Foundations/techboard/assets/sorting.png)

---

## Future Enhancements

- Add support for advanced chart types (scatter, doughnut, etc.).
- Implement additional calculus features like numerical integration.
- Allow exporting sorted/search results as CSV.
- Deploy to cloud platforms (e.g., Heroku, AWS).
- Integrate with databases for persistent storage.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code adheres to project guidelines and includes tests.

---

## License  

This project is licensed under the **MIT License**. See the LICENSE file for details.  

---

## Acknowledgments

- **Tailwind CSS**: Responsive styling.
- **Chart.js**: Data visualization.
- **Pandas & NumPy**: Data processing.
- **Flask**: Backend framework.

Thanks to open-source communities and educational platforms for their support and inspiration.

