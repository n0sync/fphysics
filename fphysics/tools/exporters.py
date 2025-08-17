"""
Data export utilities for simulation results and physics data.
"""

import json
import csv
import numpy as np
from datetime import datetime

class DataExporter:
    """Export data to various formats"""
    
    def export_to_csv(self, data, filename, headers=None):
        """Export data to CSV file"""
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if headers:
                writer.writerow(headers)
            writer.writerows(data)
    
    def export_to_json(self, data, filename):
        """Export data to JSON file"""
        with open(filename, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=2)

class ReportGenerator:
    """Generate reports from physics calculations"""
    
    def generate_summary_report(self, data, title="Physics Report"):
        """Generate summary report"""
        report = {
            'title': title,
            'timestamp': datetime.now().isoformat(),
            'data': data
        }
        return report
    
    def save_report(self, report, filename):
        """Save report to file"""
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)

class GraphExporter:
    """Export graphs and visualizations"""
    
    def save_plot(self, figure, filename, format='png', dpi=300):
        """Save matplotlib figure to file"""
        figure.savefig(filename, format=format, dpi=dpi, bbox_inches='tight')
    
    def export_data_for_plotting(self, x_data, y_data, filename):
        """Export data in format suitable for external plotting"""
        data = {'x': x_data, 'y': y_data}
        with open(filename, 'w') as f:
            json.dump(data, f)
