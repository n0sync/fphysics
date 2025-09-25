import json
import csv
import numpy as np
from datetime import datetime

def export_to_csv(data, filename, headers=None):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if headers:
            writer.writerow(headers)
        writer.writerows(data)

def export_to_json(data, filename):
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)

def generate_summary_report(data, title="Physics Report"):
    report = {
        'title': title,
        'timestamp': datetime.now().isoformat(),
        'data': data
    }
    return report

def save_report(report, filename):
    with open(filename, 'w') as f:
        json.dump(report, f, indent=2)

def save_plot(figure, filename, format='png', dpi=300):
    figure.savefig(filename, format=format, dpi=dpi, bbox_inches='tight')

def export_data_for_plotting(x_data, y_data, filename):
    data = {'x': x_data, 'y': y_data}
    with open(filename, 'w') as f:
        json.dump(data, f)
