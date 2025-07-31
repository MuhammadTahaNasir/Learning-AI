# 🚀 ThinkBoard - Data Analytics Dashboard

A modern, interactive data analytics dashboard built with Flask and JavaScript. Upload CSV files, analyze statistics, visualize data with beautiful charts, and explore sorting/searching algorithms.

![ThinkBoard Dashboard](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

### 📊 **Data Analytics**
- **Statistical Analysis**: Mean, median, mode, max, min calculations
- **Real-time Visualization**: Interactive charts with multiple chart types
- **Data Upload**: Drag & drop CSV file support
- **Sample Data**: Pre-loaded datasets for testing

### 🎨 **Modern UI/UX**
- **Glass Morphism Design**: Translucent cards with blur effects
- **Dark Theme**: Black/red/orange color scheme
- **Responsive Design**: Works perfectly on mobile and desktop
- **Pill-style Navigation**: Modern navigation with active states
- **Smooth Animations**: Hover effects and transitions

### 🔧 **Technical Features**
- **Chart Types**: Bar, Line, and Pie charts
- **Data Operations**: Sort, search, and gradient computation
- **File Validation**: Secure CSV upload with size limits
- **Error Handling**: Comprehensive error messages
- **Mobile Menu**: Hamburger menu for mobile devices

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ThinkBoard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

## 📁 Project Structure

```
ThinkBoard/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── static/
│   ├── index.html        # Main dashboard HTML
│   ├── css/
│   │   └── style.css     # Modern CSS styles
│   └── js/
│       └── app.js        # Interactive JavaScript
└── Uploads/
    ├── sample_data1.csv  # Student data sample
    ├── sample_data2.csv  # Sales data sample
    └── sample_data3.csv  # Weather data sample
```

## 🎯 Usage Guide

### 1. **Getting Started**
- Open the dashboard in your browser
- Try the sample data buttons for quick testing
- Upload your own CSV file for analysis

### 2. **Uploading Data**
- **Drag & Drop**: Simply drag your CSV file onto the upload area
- **Click to Browse**: Click the upload area to select a file
- **Sample Data**: Use the provided sample datasets

### 3. **Analyzing Data**
- **Statistics**: View mean, median, mode, max, and min values
- **Charts**: Switch between Bar, Line, and Pie charts
- **Operations**: Sort, search, and compute gradients

### 4. **Chart Types**
- **Bar Chart**: Compare different metrics
- **Line Chart**: Show trends over time
- **Pie Chart**: Display proportions

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main dashboard page |
| `/upload` | POST | Upload CSV file |
| `/sort` | POST | Sort data by column |
| `/search` | POST | Search data |
| `/gradient` | POST | Compute gradient |
| `/stats` | GET | Get file statistics |
| `/health` | GET | Health check |
| `/Uploads/<filename>` | GET | Serve sample files |

## 🎨 Design Features

### **Color Scheme**
- **Primary**: Black (#000000)
- **Secondary**: Red (#dc2626)
- **Accent**: Orange (#ea580c)
- **Text**: White (#ffffff)

### **UI Components**
- **Glass Morphism**: Translucent cards with blur effects
- **Pill Navigation**: Modern navigation with active states
- **Responsive Grid**: Adapts to all screen sizes
- **Smooth Animations**: Hover effects and transitions

### **Mobile Responsive**
- **Hamburger Menu**: Mobile-friendly navigation
- **Touch-Friendly**: Large buttons and touch targets
- **Adaptive Layout**: Optimized for all devices

## 🚀 Features in Detail

### **Data Analytics**
```python
# Statistical calculations
- Mean values for numeric columns
- Median calculations
- Mode detection
- Maximum and minimum values
- Row and column counts
```

### **Chart Visualization**
```javascript
// Chart types available
- Bar charts for comparisons
- Line charts for trends
- Pie charts for proportions
- Interactive legends and tooltips
```

### **Data Operations**
```python
# Available operations
- Sort data by any column (ascending/descending)
- Search data with exact or partial matches
- Compute gradients for numeric columns
- Export results
```

## 🔧 Technical Stack

### **Backend**
- **Flask**: Python web framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Flask-CORS**: Cross-origin resource sharing

### **Frontend**
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with glass morphism
- **JavaScript**: Interactive functionality
- **Chart.js**: Data visualization
- **Font Awesome**: Icons

### **Dependencies**
```
Flask>=3.0.0
Flask-CORS>=4.0.0
pandas>=2.2.0
numpy>=1.26.0
Werkzeug>=3.0.0
```

## 🐛 Troubleshooting

### **Common Issues**

1. **Port already in use**
   ```bash
   # Change port in app.py
   app.run(host='127.0.0.1', port=5001)
   ```

2. **CSV upload fails**
   - Check file format (must be CSV)
   - Ensure file size < 10MB
   - Verify CSV structure

3. **Charts not displaying**
   - Check browser console for errors
   - Ensure Chart.js is loaded
   - Verify data format

### **Performance Tips**
- Use smaller CSV files for better performance
- Close other browser tabs to free memory
- Clear browser cache if issues persist

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Muhammad Taha Nasir**
- Created with ❤️ for data analytics enthusiasts
- Modern UI/UX design
- Comprehensive functionality

## 🙏 Acknowledgments

- **Chart.js** for beautiful data visualization
- **Font Awesome** for amazing icons
- **Flask** community for the excellent framework
- **CSS Glass Morphism** for modern design inspiration

## 📞 Support

If you encounter any issues or have questions:
- Create an issue in the repository
- Check the troubleshooting section
- Review the API documentation

---

**Made with ❤️ by Muhammad Taha Nasir**

*ThinkBoard - Where Data Meets Design* 