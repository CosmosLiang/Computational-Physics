from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
from openpyxl import Workbook
wb=openpyxl.load_workbook('Poisson_Boltzman.xlsx')
sheet=wb.get_sheet_by_name('Sheet')
x=[];y1=[];y2=[];y3=[]
for cell in list(sheet.columns)[0]:
	x.append(float(cell.value))
for cell in list(sheet.columns)[1]:
	y1.append(float(cell.value))
for cell in list(sheet.columns)[2]:
	y2.append(float(cell.value))
for cell in list(sheet.columns)[3]:
	y3.append(float(cell.value))
plt.figure()
plt.grid()
plt.plot(x,y1,label="$\epsilon^{2}$=0.01",color="red",linewidth=2)
plt.plot(x,y2,label="$\epsilon^{2}$=0.1",color="yellow",linewidth=2)
plt.plot(x,y3,label="$\epsilon^{2}$=0.3",color="blue",linewidth=2)
plt.xlabel("x")
plt.ylabel("$\phi$(x)")
plt.title("Solution to Poisson Boltzman Equation")
plt.xlim(0,300)
plt.ylim(-11600,0.0)
plt.legend()
plt.show()
