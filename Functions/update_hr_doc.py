hr_list = [('0123', 'HR', 'Rebecca Yang', '69000'), 
           ('0121', 'IT', 'Mark Blick', '67000'), 
           ('0068', 'IT', 'Kahna Larsen', '112000'), 
           ('0234', 'OPS', 'Jim Smith', '54000')]

rebecca, mark, kahna, jim = hr_list
mark = list(mark)
mark[2] = 'Mark Blick-Hawley'
print(mark)

HR, IT, IT, OPS = hr_list
OPS = list(OPS)
OPS[1] = 'CS'
print(OPS)

'69000', '67000', '112000', '54000' = hr_list
'5400' = list('54000')
'54000'[3] = '60000'
print('54000')







# THIS CODE BELOW WAS THE FIRST ATTEMPT ON UPDATING 'MARK'S' LAST NAME
# updated_name = list(hr_list)
# print(updated_name)
# print(updated_name[1])
# updated_name[1] = 'Blick-Hawley'
# hr_list = tuple(updated_name[2])
# print(hr_list)
