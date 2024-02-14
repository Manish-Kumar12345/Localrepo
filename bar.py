import numpy as np
import matplotlib.pyplot as pl
import pandas as pd

x = [1,2,3,4,5]
y = [2,3,5,7,11]
# plotting a dashed line

pl.plot(x,y, linestyle = "--", color ="blue")

pl.xlabel("X-axis")
pl.ylabel("Y-axis")
pl.title("dashed Line Plot")
pl.grid(True)
pl.show()
