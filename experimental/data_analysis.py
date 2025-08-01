import numpy as np
from scipy import stats, optimize, interpolate
from scipy.signal import savgol_filter, find_peaks
import warnings

def mean_std(data):
    """Calculate mean and standard deviation."""
    return np.mean(data), np.std(data, ddof=1)

def weighted_mean(values, weights):
    """Calculate weighted mean and uncertainty."""
    weights = np.asarray(weights)
    values = np.asarray(values)
    wmean = np.average(values, weights=weights)
    variance = np.average((values - wmean)**2, weights=weights)
    uncertainty = np.sqrt(variance / len(values))
    return wmean, uncertainty

def linear_regression(x, y, sigma_y=None):
    """Perform linear regression with optional uncertainties."""
    x, y = np.asarray(x), np.asarray(y)
    if sigma_y is not None:
        weights = 1 / np.asarray(sigma_y)**2
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        n = len(x)
        sx2 = np.sum(weights * x**2) - np.sum(weights * x)**2 / np.sum(weights)
        slope_err = np.sqrt(1 / sx2)
        intercept_err = np.sqrt(np.sum(weights * x**2) / (n * sx2))
    else:
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        slope_err = std_err
        intercept_err = std_err * np.sqrt(np.mean(x**2))
    
    return {
        'slope': slope, 'intercept': intercept,
        'slope_error': slope_err, 'intercept_error': intercept_err,
        'r_squared': r_value**2, 'p_value': p_value
    }

def chi_squared_test(observed, expected, ddof=0):
    """Perform chi-squared goodness of fit test."""
    chi2_stat = np.sum((observed - expected)**2 / expected)
    dof = len(observed) - 1 - ddof
    p_value = 1 - stats.chi2.cdf(chi2_stat, dof)
    return chi2_stat, p_value, dof

def bootstrap_sample(data, n_samples=1000, statistic=np.mean):
    """Generate bootstrap samples and calculate confidence intervals."""
    data = np.asarray(data)
    bootstrap_stats = []
    for _ in range(n_samples):
        sample = np.random.choice(data, size=len(data), replace=True)
        bootstrap_stats.append(statistic(sample))
    
    bootstrap_stats = np.array(bootstrap_stats)
    return {
        'mean': np.mean(bootstrap_stats),
        'std': np.std(bootstrap_stats),
        'ci_95': np.percentile(bootstrap_stats, [2.5, 97.5]),
        'samples': bootstrap_stats
    }

def outlier_detection(data, method='iqr', threshold=1.5):
    """Detect outliers using IQR or Z-score methods."""
    data = np.asarray(data)
    if method == 'iqr':
        q1, q3 = np.percentile(data, [25, 75])
        iqr = q3 - q1
        lower = q1 - threshold * iqr
        upper = q3 + threshold * iqr
        outliers = (data < lower) | (data > upper)
    elif method == 'zscore':
        z_scores = np.abs(stats.zscore(data))
        outliers = z_scores > threshold
    else:
        raise ValueError("Method must be 'iqr' or 'zscore'")
    
    return outliers, data[~outliers]

def smooth_data(data, window_length=5, polyorder=2, method='savgol'):
    """Smooth noisy data using various methods."""
    if method == 'savgol':
        return savgol_filter(data, window_length, polyorder)
    elif method == 'moving_average':
        return np.convolve(data, np.ones(window_length)/window_length, mode='same')
    else:
        raise ValueError("Method must be 'savgol' or 'moving_average'")

def find_peaks_analysis(data, height=None, distance=None, prominence=None):
    """Find and analyze peaks in data."""
    peaks, properties = find_peaks(data, height=height, distance=distance, prominence=prominence)
    peak_heights = data[peaks]
    return {
        'peak_indices': peaks,
        'peak_heights': peak_heights,
        'peak_properties': properties
    }

def correlation_analysis(x, y, method='pearson'):
    """Calculate correlation coefficient and significance."""
    if method == 'pearson':
        corr, p_value = stats.pearsonr(x, y)
    elif method == 'spearman':
        corr, p_value = stats.spearmanr(x, y)
    elif method == 'kendall':
        corr, p_value = stats.kendalltau(x, y)
    else:
        raise ValueError("Method must be 'pearson', 'spearman', or 'kendall'")
    
    return corr, p_value

def fit_function(x, y, func, p0=None, sigma=None):
    """Fit arbitrary function to data with uncertainty estimation."""
    try:
        popt, pcov = optimize.curve_fit(func, x, y, p0=p0, sigma=sigma)
        parameter_errors = np.sqrt(np.diag(pcov))
        
        y_pred = func(x, *popt)
        residuals = y - y_pred
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((y - np.mean(y))**2)
        r_squared = 1 - (ss_res / ss_tot)
        
        return {
            'parameters': popt,
            'parameter_errors': parameter_errors,
            'covariance': pcov,
            'r_squared': r_squared,
            'residuals': residuals
        }
    except Exception as e:
        warnings.warn(f"Fitting failed: {e}")
        return None

def histogram_analysis(data, bins='auto', density=False):
    """Generate histogram with statistical analysis."""
    counts, bin_edges = np.histogram(data, bins=bins, density=density)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    bin_width = bin_edges[1] - bin_edges[0]
    
    return {
        'counts': counts,
        'bin_centers': bin_centers,
        'bin_edges': bin_edges,
        'bin_width': bin_width,
        'total_counts': np.sum(counts) if not density else None
    }

def interpolate_data(x, y, x_new, method='linear'):
    """Interpolate data using various methods."""
    if method == 'linear':
        f = interpolate.interp1d(x, y, kind='linear', bounds_error=False, fill_value='extrapolate')
    elif method == 'cubic':
        f = interpolate.interp1d(x, y, kind='cubic', bounds_error=False, fill_value='extrapolate')
    elif method == 'spline':
        f = interpolate.UnivariateSpline(x, y, s=0)
    else:
        raise ValueError("Method must be 'linear', 'cubic', or 'spline'")
    
    return f(x_new)

def moving_statistics(data, window_size, statistic='mean'):
    """Calculate moving statistics over a sliding window."""
    data = np.asarray(data)
    if statistic == 'mean':
        func = np.mean
    elif statistic == 'std':
        func = lambda x: np.std(x, ddof=1)
    elif statistic == 'median':
        func = np.median
    else:
        raise ValueError("Statistic must be 'mean', 'std', or 'median'")
    
    result = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        result.append(func(window))
    
    return np.array(result)
