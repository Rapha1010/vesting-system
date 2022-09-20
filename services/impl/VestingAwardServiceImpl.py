import datetime
from repositories.impl.VestingAwardCSVRepositoryImpl import VestingAwardCSVRepositoryImpl
from services.VestingAwardService import VestingAwardService

class VestingAwardServiceImpl(VestingAwardService):

    def __init__(self)-> None:
        self.repo = VestingAwardCSVRepositoryImpl()

    def get_all(self):
        return self.repo.get_all()

    def get_all_by_date_group_vest_id_and_employee_id(self, csv_file, date, digits):    
        return self.repo.get_all_by_date_group_vest_id_and_employee_id(csv_file, date, digits) 

    def get_by_id(self, id):
        return "2"