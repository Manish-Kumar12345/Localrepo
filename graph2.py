import pandas as pd
import matplotlib.pyplot as pl
import numpy as np

names = ["jhon", "shan", "max", "smith", "Nick", "Steve"]
data = { "names": names,
         "dept": ["IT","HR","IT","HR","Admin","IT"],
         "salary": [56000,50000,45000,32000,70000,30000],
         "new salary":[45000,40000,40000,29000,55000, 20000]}
pl.figure(figsize = (10,6))

c =["y","b","m","g","c","r"]
pl.barh(data['names'], data["salary"] , align = "center", color = "red" , edgecolor = "k", label = "Previous Salary")
pl.barh(data['names'], data["new salary"], align = "center", color ="m", edgecolor = "k", label = "decreement salary")
pl.title("Salary of Empolyee")
pl.xlabel("Names", fontsize = 15)
pl.ylabel("Salary", fontsize = 15)
pl.legend()
pl.show()
pl.pie(data["salary"])
pl.show()

