from services.impl.VestingAwardServiceImpl import VestingAwardServiceImpl
import sys

serv = VestingAwardServiceImpl()
# filter_date="2021-01-01"
# file='C:/projectPy/project-carta/app/tests/vestingfile-stage4.csv'
# digits=2

if(len(sys.argv) <= 1):
        print("file can not be empty") 
        exit()

if(len(sys.argv) == 2):
        print("date can not be empty") 
        exit()
digits=6
if(len(sys.argv) == 4):
    digits=sys.argv[3]

file=sys.argv[1]
filter_date=sys.argv[2]

awards = serv.get_all_by_date_group_vest_id_and_employee_id(file,filter_date, digits)

for item in awards:
    print('{} {} {} {}'.format(item.employee_id,item.employee_name,item.vest_id,item.award_amount))
