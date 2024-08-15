import math
num = 25
result = math.sqrt(num)
print(result)

from math import sqrt
num = 100
result = sqrt(num)
print(result)

from math import *
num = 25
square_root = sqrt(num)
circumference = 2 * pi
print(f"Square root of 25 is {square_root}")
print(f"Circumference of the circle with radius 1 is {circumference}")

import numpy as np
num_list = [1, 2, 3, 4, 5]
arr_1D = np.array(num_list)
print(arr_1D)

import numpy as np
arr_1D = np.array([1, 2, 3, 4, 5])
print(arr_1D)

import numpy as np
arr_2D = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2D)

import numpy as np
arr_3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3D)

import numpy as np
zeros_arr_2D = np.zeros((4, 4))
print(zeros_arr_2D)

import numpy as np
ones_arr_1D = np.ones(4)
print(ones_arr_1D)

import numpy as np
arr_1D = np.array([1, 2, 3, 4])
result1 = arr_1D + 10
print(result1)
result2 = arr_1D - 4
print(result2)
result3 = arr_1D * 2
print(result3)
result4 = arr_1D / 2
print(result4)

import numpy as np
arr_2D = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(arr_2D[1, 2])
print(arr_2D[0, :])
print(arr_2D[:, 1])

import numpy as np
arr_3D = np.array([[[10, 20], [30, 40]], [[50, 60], [70, 80]]])
print(arr_3D[0])
print(arr_3D[0, 0])
print(arr_3D[0, 0, 0])
print(arr_3D[1, 0, 1])

import pandas as pd
num_list = [1, 2, 3, 4, 5]
num_series = pd.Series(num_list)
print(num_series)
print(num_series[0])

import pandas as pd
num_series = pd.Series([1, 2, 3, 4, 5], index = ["A", "B", "C", "D", "E"])
print(num_series)

import pandas as pd
data = {
        "Name" : ["Dheeraj", "Kali", "Narayana"],
        "Age" : [20, 21, 21],
        "City" : ["Vizag", "Hyderabad", "Vijayawada"]
}
dataframe = pd.DataFrame(data, index = ["A", "B", "C"])
print(dataframe)

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [5, 3, 1, 0, 9]
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Plot Graph")
plt.show()

import matplotlib.pyplot as plt
categories = ["A", "B", "C", "D", "E"]
values = [34, 22, 10, 56, 4]
plt.bar(categories, values, color = "Green")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Plot")
plt.show()

import matplotlib.pyplot as plt
data = [4, 6, 3, 8, 12, 11, 13, 1, 5]
plt.hist(data, bins = 4, color = "Green", edgecolor = "Black")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()
