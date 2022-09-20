class AwardEmployeeModel:
    def __init__(self, vest_id, event_type, date, award_amount, employee_id, employee_name):
        self.vest_id = vest_id
        self.event_type = event_type
        self.date = date
        self.award_amount = award_amount
        self.employee_id = employee_id
        self.employee_name = employee_name

    def list_to_object_list(list):
        object_list = []
        for item in list :
            award = AwardEmployeeModel(item['vest_id'], item['event_type'], item['date'], item['award_amount'],  item['employee_id'], item['employee_name'])
            object_list.append(award)

        return object_list
            