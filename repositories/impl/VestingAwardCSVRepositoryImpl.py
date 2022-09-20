import csv
from datetime import datetime

from models.AwardEmployeeModel import AwardEmployeeModel

from utils.MyRound import MyRound
from repositories.VestingAwardRepository import VestingAwardRepository

class VestingAwardCSVRepositoryImpl(VestingAwardRepository):

    def __init__(self) -> None:
        super().__init__()

    def get_by_id(self, id):
        return print("get_by_id"+id)

    def get_all(self, csv_file, vest_filter_date = '9999-12-30'):
        try:
            vest_filter_date = datetime.strptime(vest_filter_date, '%Y-%m-%d')
        except:
            return print("date should be like yyyy-mm-dd "+vest_filter_date)
        
        vesting_award = []    
        
        try:
            with open(csv_file, 'r') as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    vest_file_date = datetime.strptime(row[4], '%Y-%m-%d')
                    if vest_filter_date >= vest_file_date:
                        vesting_award.append(
                            {'event_type':row[0], 'employee_id':row[1], 'employee_name':row[2], 'vest_id':row[3], 'date':row[4] ,'award_amount':row[5]}
                        )       
        except:
             return print("file not found")

        return vesting_award

    def get_all_by_date_group_vest_id_and_employee_id(self, csv_file, vest_filter_date, digits = 6):

        if(int(digits) > 6):
            return print("Valid values are between 0 and 6 ")

        vesting_award = self.get_all(csv_file, vest_filter_date)
        
        award_vector = {}
        # sum values by vest_id and employeed_id
        for award in vesting_award:

            key = award['employee_id']+award['vest_id'].strip()

            if key not in award_vector:
                value = 0
                if (award['event_type'].upper() == 'CANCEL'):
                    value -= float(award['award_amount']) 
                elif (award['event_type'].upper() == 'VEST'):
                    value = float(award['award_amount'])
            else :
                if (award['event_type'].upper() == 'CANCEL'):
                    value = float(award_vector[key][3]) - float(award['award_amount'])
                elif (award['event_type'].upper() == 'VEST'):
                    value = float(award['award_amount']) + float(award_vector[key][3])
            
            award_vector[key] = [award['employee_id'], award['employee_name'], award['vest_id'], MyRound.my_round(value, digits), award['date'], award['event_type']]

        vesting_award = self.get_all(csv_file)

        # add employees and vests with 0 values
        for award in vesting_award:
            key = award['employee_id']+award['vest_id'].strip()

            if key not in award_vector:
                 award_vector[key] = [award['employee_id'], award['employee_name'], award['vest_id'], 0,  award['date'], award['event_type']]

        award_list = []
        for key in award_vector:
            award_list.append({'employee_id':award_vector[key][0], 'employee_id':award_vector[key][0], 'employee_name':award_vector[key][1], 'vest_id':award_vector[key][2], 'award_amount':award_vector[key][3], 'date':award_vector[key][4], 'event_type':award_vector[key][5]})

        sorted_award_list = sorted(award_list, key=lambda i: (i['employee_id'], i['vest_id']))

        return AwardEmployeeModel.list_to_object_list(sorted_award_list)


