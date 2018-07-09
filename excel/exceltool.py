#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import xlrd
import xlwt
file = 'bus.xlsx'
def set_style(name,height,bold=False):
	style = xlwt.XFStyle()
	font = xlwt.Font()
	font.name = name
	font.bold = bold
	font.color_index = 4
	font.height = height
	style.font = font
	return style

def write_excel():
	rd = xlrd.open_workbook(filename=file)#open file
	rd_sheet1 = rd.sheet_by_index(0)
	wt = xlwt.Workbook()
	wt_sheet1 = wt.add_sheet('smilebus',cell_overwrite_ok=True)

	for r in range(len((rd_sheet1.col_values(0)))):
		for c in range(len((rd_sheet1.row_values(0)))):
			if(r==0):
				if(c<5):
					wt_sheet1.write(r,c,rd_sheet1.cell_value(r,c))
				elif(c==5):
					wt_sheet1.write(r,c,u'发车日期')
					wt_sheet1.write(r,c+1,u'发车时间')
				else:
					wt_sheet1.write(r,c+1,rd_sheet1.cell_value(r,c))
			else:
				if(c<5): 
					wt_sheet1.write(r,c,rd_sheet1.cell_value(r,c))
				elif(c==5):				
					ls = rd_sheet1.cell_value(r,c).split(' ');
					wt_sheet1.write(r,c,ls[0])
					wt_sheet1.write(r,c+1,ls[1])
				else:
					wt_sheet1.write(r,c+1,rd_sheet1.cell_value(r,c))
	wt.save('sbus.xls')
write_excel();