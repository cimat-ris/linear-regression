import numpy as np
import pandas as pd
import statsmodels.api as sm
x = [
   [66, 29.5], [57, 28.5], [59, 29], [61, 27.5], [77, 28], [76, 27.2], [75, 24], [67, 23.8], [76, 35], [58, 26], [57, 26.6], [55, 26.6], 
   [53, 23.6], [52, 27.8], [55, 28.5], [57, 27.9],
   [58, 28.1], [54, 28.3], [55, 28.7], [62, 27.3], [57, 26], [58, 26.7], [54, 28], [56, 28.7], [63, 29.2], 
   [54, 29.4],  [56, 29.4], [65, 26.5], [64, 26.1], [61, 26.8], [56, 28], [58, 28.5],
   [59, 28.5], [66, 26.3], [65, 27.3], [53, 26.5], [53, 27.3], [67, 28], [60, 28.8], [56, 25.9], [66, 26], [57, 27.4], [65, 27.9]
 ]
y = [1, 1, 1, 1, 1, 3, 1, 1, 1, 5, 3, 2, 3, 5, 8, 6
     , 12, 6, 1, 3, 1, 1, 2, 1, 6, 13, 2, 5, 6, 2, 1, 2, 8, 3, 2, 2, 1, 8, 6, 1, 2, 4, 2]
x, y = np.array(x), np.array(y)
x = sm.add_constant(x)
model = sm.OLS(y, x)
results = model.fit()
print(results.summary())
print(f"coefficient of determination: {results.rsquared}")


