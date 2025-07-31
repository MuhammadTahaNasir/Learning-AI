// ThinkBoard - Data Analytics Dashboard JavaScript

// Global variables
let currentData = null;
let chartInstance = null;
let chartType = 'bar';
let currentFile = null;

// DOM Elements
const dataChart = document.getElementById('dataChart')?.getContext('2d');

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
    console.log('ThinkBoard initialized');
    console.log('Current URL:', window.location.href);
    console.log('Base URL:', window.location.origin);
    
    // Test API connectivity
    testAPIConnectivity();
    
    setupDragAndDrop();
    setupMobileMenu();
    setupSmoothScrolling();
    setupActiveNavigation();
});

// Test API connectivity
async function testAPIConnectivity() {
    try {
        const response = await fetch('/health');
        const data = await response.json();
        console.log('API Health Check:', data);
    } catch (error) {
        console.error('API Health Check Failed:', error);
    }
}

// Mobile menu functionality
function setupMobileMenu() {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileMenu = document.querySelector('.mobile-menu');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileMenu.classList.toggle('show');
            const icon = mobileMenuBtn.querySelector('i');
            if (icon) {
                icon.classList.toggle('fa-bars');
                icon.classList.toggle('fa-times');
            }
        });
    }
}

// Smooth scrolling setup
function setupSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Active navigation setup
function setupActiveNavigation() {
    const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-link');
    
    window.addEventListener('scroll', function() {
        const sections = document.querySelectorAll('section[id]');
        const scrollPos = window.scrollY + 100;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            
            if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    });
}

// Drag and drop functionality
function setupDragAndDrop() {
    const dragArea = document.getElementById('dragArea');
    const fileInput = document.getElementById('csv-upload');

    if (!dragArea || !fileInput) return;

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dragArea.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
        dragArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dragArea.addEventListener(eventName, unhighlight, false);
    });

    function highlight(e) {
        dragArea.classList.add('dragover');
    }

    function unhighlight(e) {
        dragArea.classList.remove('dragover');
    }

    dragArea.addEventListener('drop', handleDrop, false);

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        
        if (files.length > 0) {
            fileInput.files = files;
            handleFileSelect(fileInput);
        }
    }
}

// Load sample data
async function loadSampleData(filename) {
    try {
        showNotification('Loading sample data...', 'info');
        
        const response = await fetch(`/Uploads/${filename}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const csvText = await response.text();
        
        // Create a file object from the CSV text
        const blob = new Blob([csvText], { type: 'text/csv' });
        const file = new File([blob], filename, { type: 'text/csv' });
        
        // Set the file input
        const fileInput = document.getElementById('csv-upload');
        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);
        fileInput.files = dataTransfer.files;
        
        // Simulate file selection
        handleFileSelect(fileInput);
        
        showNotification(`Loaded ${filename} successfully!`, 'success');
    } catch (error) {
        console.error('Error loading sample data:', error);
        showNotification('Error loading sample data. Please try uploading manually.', 'error');
    }
}

// Handle file selection
function handleFileSelect(input) {
    const file = input.files[0];
    if (file) {
        const uploadBtn = document.getElementById('uploadBtn');
        if (uploadBtn) {
            uploadBtn.classList.remove('hidden');
            uploadBtn.innerHTML = `<i class="fas fa-upload"></i> Upload ${file.name}`;
        }
        
        // Validate file type
        if (!file.name.toLowerCase().endsWith('.csv')) {
            showNotification('Please select a CSV file', 'error');
            return;
        }
        
        showNotification('File selected successfully!', 'success');
    }
}

// Show/hide loading indicator
function showLoading(show) {
    const loading = document.getElementById('loadingIndicator');
    const uploadBtn = document.getElementById('uploadBtn');
    
    if (show) {
        if (loading) loading.classList.remove('hidden');
        if (uploadBtn) {
            uploadBtn.disabled = true;
            uploadBtn.innerHTML = '<div class="loading"></div> Processing...';
        }
    } else {
        if (loading) loading.classList.add('hidden');
        if (uploadBtn) {
            uploadBtn.disabled = false;
            uploadBtn.innerHTML = '<i class="fas fa-upload"></i> Upload & Analyze';
        }
    }
}

// File Upload Module
async function uploadCSV() {
    const csvUpload = document.getElementById('csv-upload');
    const file = csvUpload?.files[0];
    
    if (!file) {
        showNotification('Please select a CSV file to upload.', 'error');
        return;
    }

    showLoading(true);
    currentFile = file;
    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("/upload", {
            method: "POST",
            body: formData,
        });
        
        const data = await response.json();
        
        if (data.error) {
            showNotification(data.error, 'error');
            return;
        }
        
        currentData = data;
        displayAnalytics(data.summary);
        renderChart(data.summary);
        const resultsTable = document.getElementById('resultsTable');
        if (resultsTable) resultsTable.innerHTML = '';
        showNotification('File uploaded successfully!', 'success');
        
    } catch (error) {
        console.error("Error uploading file:", error);
        console.error("Error details:", {
            message: error.message,
            stack: error.stack,
            url: window.location.href
        });
        showNotification('Error uploading file. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

// Display analytics with modern cards
function displayAnalytics(summary) {
    const analyticsContainer = document.getElementById("analyticsContainer");
    if (!analyticsContainer) return;
    
    const stats = [
        { label: 'Columns', value: summary.columns.length, icon: 'fas fa-columns' },
        { label: 'Rows', value: summary.row_count, icon: 'fas fa-list' },
        { label: 'Numeric Columns', value: Object.keys(summary.mean_values).length, icon: 'fas fa-calculator' }
    ];

    const statsHTML = stats.map(stat => `
        <div class="stat-card">
            <i class="${stat.icon} stat-icon"></i>
            <div class="stat-value">${stat.value}</div>
            <div class="stat-label">${stat.label}</div>
        </div>
    `).join('');

    const mean = Object.entries(summary.mean_values).map(([key, value]) => `${key}: ${value.toFixed(2)}`).join(", ");
    const max = Object.entries(summary.max_values).map(([key, value]) => `${key}: ${value}`).join(", ");
    const min = Object.entries(summary.min_values).map(([key, value]) => `${key}: ${value}`).join(", ");
    const median = Object.entries(summary.median_values).map(([key, value]) => `${key}: ${value.toFixed(2)}`).join(", ");
    const mode = Object.entries(summary.mode_values).map(([key, value]) => `${key}: ${value}`).join(", ");

    analyticsContainer.innerHTML = `
        <div class="stats-grid">
            ${statsHTML}
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
            <div class="glass-effect p-4">
                <h4 class="text-highlight mb-2">Statistical Summary</h4>
                <p class="text-secondary mb-1"><strong class="text-primary">Mean:</strong> ${mean}</p>
                <p class="text-secondary mb-1"><strong class="text-primary">Median:</strong> ${median}</p>
                <p class="text-secondary mb-1"><strong class="text-primary">Mode:</strong> ${mode}</p>
            </div>
            <div class="glass-effect p-4">
                <h4 class="text-highlight mb-2">Range Summary</h4>
                <p class="text-secondary mb-1"><strong class="text-primary">Max:</strong> ${max}</p>
                <p class="text-secondary mb-1"><strong class="text-primary">Min:</strong> ${min}</p>
            </div>
        </div>
        <div class="flex flex-wrap gap-4 justify-center">
            <button class="btn-secondary" onclick="sortData()">
                <i class="fas fa-sort"></i> Sort Data
            </button>
            <button class="btn-secondary" onclick="searchData()">
                <i class="fas fa-search"></i> Search Data
            </button>
            <button class="btn-secondary" onclick="computeGradient()">
                <i class="fas fa-chart-line"></i> Compute Gradient
            </button>
        </div>
    `;
}

// Enhanced chart rendering with theme colors
function renderChart(summary) {
    if (!dataChart) return;
    
    if (chartInstance) {
        chartInstance.destroy();
    }

    // Theme colors - black/red/orange
    const colors = [
        'rgba(220, 38, 38, 0.8)',    // Red
        'rgba(234, 88, 12, 0.8)',    // Orange
        'rgba(239, 68, 68, 0.8)',    // Light Red
        'rgba(245, 101, 101, 0.8)'   // Lighter Red
    ];

    const datasets = [
        {
            label: 'Mean Values',
            data: Object.values(summary.mean_values),
            backgroundColor: colors[0],
            borderColor: colors[0].replace('0.8', '1'),
            borderWidth: 3,
            fill: chartType === 'line' ? false : undefined,
            tension: 0.4
        },
        {
            label: 'Median Values',
            data: Object.values(summary.median_values),
            backgroundColor: colors[1],
            borderColor: colors[1].replace('0.8', '1'),
            borderWidth: 3,
            fill: chartType === 'line' ? false : undefined,
            tension: 0.4
        },
        {
            label: 'Max Values',
            data: Object.values(summary.max_values),
            backgroundColor: colors[2],
            borderColor: colors[2].replace('0.8', '1'),
            borderWidth: 3,
            fill: chartType === 'line' ? false : undefined,
            tension: 0.4
        },
        {
            label: 'Min Values',
            data: Object.values(summary.min_values),
            backgroundColor: colors[3],
            borderColor: colors[3].replace('0.8', '1'),
            borderWidth: 3,
            fill: chartType === 'line' ? false : undefined,
            tension: 0.4
        }
    ];

    if (chartType === 'pie') {
        datasets.forEach((dataset, index) => {
            dataset.backgroundColor = colors[index];
            dataset.borderColor = colors[index].replace('0.8', '1');
            dataset.borderWidth = 2;
        });
    }

    chartInstance = new Chart(dataChart, {
        type: chartType,
        data: {
            labels: Object.keys(summary.mean_values),
            datasets: datasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        color: '#ffffff',
                        font: {
                            size: 12,
                            weight: '600'
                        },
                        padding: 15,
                        usePointStyle: true
                    }
                },
                title: {
                    display: true,
                    text: 'Data Visualization',
                    color: '#ffffff',
                    font: {
                        size: 18,
                        weight: 'bold'
                    },
                    padding: {
                        top: 10,
                        bottom: 20
                    }
                }
            },
            scales: chartType === 'pie' ? {} : {
                y: {
                    beginAtZero: true,
                    title: { 
                        display: true, 
                        text: 'Values',
                        color: '#ffffff',
                        font: {
                            size: 14,
                            weight: '600'
                        }
                    },
                    ticks: {
                        color: '#ffffff',
                        font: {
                            size: 12,
                            weight: '500'
                        }
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.15)',
                        lineWidth: 1
                    }
                },
                x: {
                    title: { 
                        display: true, 
                        text: 'Columns',
                        color: '#ffffff',
                        font: {
                            size: 14,
                            weight: '600'
                        }
                    },
                    ticks: {
                        color: '#ffffff',
                        font: {
                            size: 12,
                            weight: '500'
                        }
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.15)',
                        lineWidth: 1
                    }
                }
            }
        }
    });
}

// Chart type selector
function updateChartType(type) {
    chartType = type;
    
    // Update pill buttons
    const pills = document.querySelectorAll('.chart-pill');
    pills.forEach(pill => {
        pill.classList.remove('active');
        if (pill.getAttribute('data-type') === type) {
            pill.classList.add('active');
        }
    });
    
    if (currentData) {
        renderChart(currentData.summary);
    }
}

// Enhanced sort function
async function sortData() {
    if (!currentData || !currentFile) {
        showNotification('Please upload a CSV file first.', 'error');
        return;
    }
    
    const column = prompt("Enter the column to sort by:");
    if (!column) return;
    
    const order = confirm("Sort ascending? Click Cancel for descending.") ? "asc" : "desc";

    try {
        const response = await fetch("/sort", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ column, order }),
        });
        
        const sortedData = await response.json();
        
        if (sortedData.error) {
            showNotification(sortedData.error, 'error');
            return;
        }
        
        displayTable(sortedData, `Sorted by ${column} (${order})`);
        showNotification('Data sorted successfully!', 'success');
        
    } catch (error) {
        console.error("Error sorting data:", error);
        showNotification('Error sorting data. Please try again.', 'error');
    }
}

// Enhanced search function
async function searchData() {
    if (!currentData || !currentFile) {
        showNotification('Please upload a CSV file first.', 'error');
        return;
    }
    
    const column = prompt("Enter the column to search in:");
    if (!column) return;
    
    const query = prompt("Enter the search query:");
    if (!query) return;

    try {
        const response = await fetch("/search", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ column, query }),
        });
        
        const searchResults = await response.json();
        
        if (searchResults.error) {
            showNotification(searchResults.error, 'error');
            return;
        }
        
        displayTable(searchResults, `Search Results for "${query}" in ${column}`);
        showNotification(`Found ${searchResults.length} results!`, 'success');
        
    } catch (error) {
        console.error("Error searching data:", error);
        showNotification('Error searching data. Please try again.', 'error');
    }
}

// Enhanced gradient function
async function computeGradient() {
    if (!currentData || !currentFile) {
        showNotification('Please upload a CSV file first.', 'error');
        return;
    }
    
    const column = prompt("Enter the numeric column for gradient calculation:");
    if (!column) return;

    try {
        const response = await fetch("/gradient", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ column }),
        });
        
        const gradientData = await response.json();
        
        if (gradientData.error) {
            showNotification(gradientData.error, 'error');
            return;
        }
        
        renderGradientChart(gradientData.gradients, column);
        showNotification('Gradient computed successfully!', 'success');
        
    } catch (error) {
        console.error("Error computing gradient:", error);
        showNotification('Error computing gradient. Please try again.', 'error');
    }
}

// Enhanced table display
function displayTable(data, title) {
    const resultsTable = document.getElementById('resultsTable');
    if (!resultsTable) return;
    
    if (!data || data.length === 0) {
        resultsTable.innerHTML = `
            <div class="glass-effect p-6 text-center">
                <i class="fas fa-info-circle text-2xl text-highlight mb-2"></i>
                <p class="text-muted">No results found.</p>
            </div>
        `;
        return;
    }

    const headers = Object.keys(data[0]);
    const tableHTML = `
        <div class="glass-effect p-6">
            <h4 class="text-xl font-bold mb-4 text-center text-primary">${title}</h4>
            <div class="table-container">
                <table class="data-table w-full text-left">
                    <thead>
                        <tr>
                            ${headers.map(header => `<th class="text-highlight">${header}</th>`).join('')}
                        </tr>
                    </thead>
                    <tbody>
                        ${data.slice(0, 10).map(row => `
                            <tr class="hover:bg-white hover:bg-opacity-10 transition-colors duration-200">
                                ${headers.map(header => `<td class="text-secondary">${row[header]}</td>`).join('')}
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            </div>
            <p class="text-sm text-muted mt-4 text-center">Showing up to 10 rows of ${data.length} total results.</p>
        </div>
    `;
    resultsTable.innerHTML = tableHTML;
}

// Enhanced gradient chart
function renderGradientChart(gradients, column) {
    if (!dataChart) return;
    
    if (chartInstance) {
        chartInstance.destroy();
    }

    chartInstance = new Chart(dataChart, {
        type: 'line',
        data: {
            labels: Array.from({ length: gradients.length }, (_, i) => i + 1),
            datasets: [{
                label: `Gradient of ${column}`,
                data: gradients,
                backgroundColor: 'rgba(220, 38, 38, 0.3)',
                borderColor: 'rgba(220, 38, 38, 1)',
                borderWidth: 4,
                fill: true,
                tension: 0.4,
                pointBackgroundColor: 'rgba(220, 38, 38, 1)',
                pointBorderColor: '#ffffff',
                pointBorderWidth: 2,
                pointRadius: 6,
                pointHoverRadius: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        color: '#ffffff',
                        font: {
                            size: 14,
                            weight: '600'
                        },
                        padding: 15
                    }
                },
                title: {
                    display: true,
                    text: `Gradient of ${column}`,
                    color: '#ffffff',
                    font: {
                        size: 18,
                        weight: 'bold'
                    },
                    padding: {
                        top: 10,
                        bottom: 20
                    }
                }
            },
            scales: {
                y: {
                    title: { 
                        display: true, 
                        text: 'Gradient Values',
                        color: '#ffffff',
                        font: {
                            size: 14,
                            weight: '600'
                        }
                    },
                    ticks: {
                        color: '#ffffff',
                        font: {
                            size: 12,
                            weight: '500'
                        }
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.15)',
                        lineWidth: 1
                    }
                },
                x: {
                    title: { 
                        display: true, 
                        text: 'Row Index',
                        color: '#ffffff',
                        font: {
                            size: 14,
                            weight: '600'
                        }
                    },
                    ticks: {
                        color: '#ffffff',
                        font: {
                            size: 12,
                            weight: '500'
                        }
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.15)',
                        lineWidth: 1
                    }
                }
            }
        }
    });
}

// Enhanced notification system
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.innerHTML = `
        <div class="flex items-center">
            <i class="fas fa-${type === 'success' ? 'check' : type === 'error' ? 'exclamation-triangle' : 'info-circle'} mr-2"></i>
            <span>${message}</span>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.classList.add('show');
    }, 100);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            if (document.body.contains(notification)) {
                document.body.removeChild(notification);
            }
        }, 300);
    }, 3000);
}

// Utility functions
function scrollToAnalytics() {
    const analyticsSection = document.getElementById('analytics');
    if (analyticsSection) {
        analyticsSection.scrollIntoView({ 
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Export functions for global access
window.loadSampleData = loadSampleData;
window.uploadCSV = uploadCSV;
window.updateChartType = updateChartType;
window.sortData = sortData;
window.searchData = searchData;
window.computeGradient = computeGradient;
window.scrollToAnalytics = scrollToAnalytics; 