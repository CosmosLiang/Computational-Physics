import numpy as np
import openpyxl
from openpyxl import Workbook
import matplotlib
import matplotlib.pyplot as plt
wb=openpyxl.load_workbook('data.xlsx')
for i in range(36):
	sheet=wb.get_sheet_by_name('Sheet'+'%d'%(i+1))
	x=[];psix=[];E=float(sheet['C1'].value)
	for cell in list(sheet.columns)[0]:
		x.append(float(cell.value))
	for cell in list(sheet.columns)[1]:
		psix.append(float(cell.value))
	plt.figure()
	plt.plot(x,psix,'b')
	plt.title('The figure of wavefuction which intrinsic energy is '+'%f'%(E))
	plt.xlabel('x')
	plt.ylabel('$\psi(x)$')
	plt.grid()
	plt.savefig("%d.eps"%(i+1))
