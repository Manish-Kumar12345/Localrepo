import pandas as pd
import matplotlib.pyplot as pl
import numpy as np

names = ["jhon", "shan", "max", "smith", "Nick", "Steve"]
data = { "names": names,
         "dept": ["IT","HR","IT","HR","Admin","IT"],
         "salary": [56000,50000,45000,32000,70000,30000],
         "new salary":[45000,40000,40000,29000,55000, 20000]}
pl.figure(figsize = (6,6))
pl.pie(data["salary"], labels = data['names'], autopct = "%1.2f%%", startangle = 90, counterclock = False, explode =(0,0.4,0,0,0,0), shadow = True, colors= ["r","b","c","m","y","g"])
c =["y","b","m","g","c","r"]
pl.title("Salary  of Empolyee")
pl.legend()

pl.show()

