import pandas as pd

# Global cache for analytics (could also use Redis, DB, etc.)
analytics_data = {}

def process_uploaded_file(file_path):
    try:
        df = pd.read_csv(file_path)
        # Example: Basic statistics
        analytics_data['summary'] = df.describe().to_html()
    except Exception as e:
        analytics_data['error'] = str(e)

def get_summary_statistics():
    return analytics_data
