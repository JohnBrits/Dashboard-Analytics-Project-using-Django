# views.py
from django.shortcuts import render
import pandas as pd

def upload_view(request):
    return render(request, 'upload.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')
 

def analytics_view(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        file = request.FILES['csv_file']
        df = pd.read_csv(file)

        context = {
            'shape': df.shape,
            'columns': df.columns,
            'description': df.describe().to_html(),
        }
        plot_paths = {
    'histograms': ['analytics/age_hist.png', ...],
    'boxplots': ['analytics/age_box.png', ...],
    'heatmap': 'analytics/corr_heatmap.png',
    'pairplot': 'analytics/pairplot.png',
    'categorical': ['analytics/gender_bar.png', ...],
}

        return render(request, 'analytics.html', context)
    
    return render(request, 'analytics.html') 

