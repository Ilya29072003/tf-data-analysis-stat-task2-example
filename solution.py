import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 422189248

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    v = np.var(x, ddof = 1)
    chi2 = norm.ppf((1-p)/2)
    chi21 = norm.ppf((1+p)/2)
    return np.sqrt((n-1) * v / (38*chi21)), \
           np.sqrt((n-1) * v / (38*chi2)) 
