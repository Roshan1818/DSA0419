import numpy as np
import scipy.stats as stats
conversion_A = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1] 
conversion_B = [0, 0, 1, 0, 0, 1, 1, 1, 0, 1]
def ab_test(conversion_A, conversion_B):
    success_A = np.sum(conversion_A)
    success_B = np.sum(conversion_B)
    n_A = len(conversion_A)
    n_B = len(conversion_B)
    p_A = success_A / n_A
    p_B = success_B / n_B
    p_pool = (success_A + success_B) / (n_A + n_B)
    se = np.sqrt(p_pool * (1 - p_pool) * (1/n_A + 1/n_B))
    z = (p_A - p_B) / se
    p_value = stats.norm.sf(abs(z)) * 2  
    return p_value
p_value = ab_test(conversion_A, conversion_B)
print(f"P-value from A/B test: {p_value}")
