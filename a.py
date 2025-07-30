import numpy as np
import pandas as pd

def central_tendency_measures(data):
    mean = np.mean(data)
    median = np.median(data)
    # Calculate mode using pandas
    mode = pd.Series(data).mode()[0]
    variance = np.var(data)
    std_dev = np.std(data)
    
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")