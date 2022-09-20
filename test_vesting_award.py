import json

from models.AwardEmployeeModel import AwardEmployeeModel

from services.impl.VestingAwardServiceImpl import VestingAwardServiceImpl

def test_for_get_all_stage_one():
    serv = VestingAwardServiceImpl()
    filter_date="2020-04-01"
    file='tests/vestingfile-stage1.csv'
    assert_list = []
    object_list = []
    current_list =[]
    # E001 Alice Smith ISO-001 100.50
    object_list.append(AwardEmployeeModel('ISO-001', '', '', '1000',  'E001', 'Alice Smith'))
    object_list.append(AwardEmployeeModel('ISO-002', '', '', '800',  'E001', 'Alice Smith'))
    object_list.append(AwardEmployeeModel('NSO-001', '', '', '600',  'E002', 'Bobby Jones'))
    object_list.append(AwardEmployeeModel('NSO-002', '', '', '0',  'E003', 'Cat Helms'))
    object_current_list = serv.get_all_by_date_group_vest_id_and_employee_id(file,filter_date,0)

    for item in object_list:
        assert_list.append({'employee_id': item.employee_id, 'employee_name':item.employee_name,'vest_id':item.vest_id,'award_amount':str(item.award_amount)})

    for item in object_current_list:
        current_list.append({'employee_id': item.employee_id, 'employee_name':item.employee_name,'vest_id':item.vest_id,'award_amount':str(item.award_amount)})

    current = json.dumps(current_list, sort_keys=True)
    asser = json.dumps(assert_list, sort_keys=True)

    print(current)
    print(asser)

    assert current == asser
            
def test_for_get_all_stage_two():
    serv = VestingAwardServiceImpl()
    filter_date="2021-01-01"
    file='tests/vestingfile-stage2.csv'
    assert_list = []
    object_list = []
    current_list =[]
    object_list.append(AwardEmployeeModel('ISO-001', '', '', '300',  'E001', 'Alice Smith'))
    object_current_list = serv.get_all_by_date_group_vest_id_and_employee_id(file,filter_date,0)

    for item in object_list:
        assert_list.append({'employee_id': item.employee_id, 'employee_name':item.employee_name,'vest_id':item.vest_id,'award_amount':str(item.award_amount)})

    for item in object_current_list:
        current_list.append({'employee_id': item.employee_id, 'employee_name':item.employee_name,'vest_id':item.vest_id,'award_amount':str(item.award_amount)})

    current = json.dumps(current_list, sort_keys=True)
    asser = json.dumps(assert_list, sort_keys=True)
    
    assert current == asser

def test_for_get_all_stage_three_part_one():
    serv = VestingAwardServiceImpl()
    filter_date="2021-01-01"
    file='tests/vestingfile-stage3.csv'
    assert_list = []
    object_list = []
    current_list =[]
    object_list.append(AwardEmployeeModel('ISO-001', '', '', '299.8',  'E001', 'Alice Smith'))
    object_list.append(AwardEmployeeModel('ISO-002', '', '', '234.0',  'E002', 'Bobby Jones'))
    object_current_list = serv.get_all_by_date_group_vest_id_and_employee_id(file,filter_date,1)

    for item in object_list:
        assert_list.append({'employee_id': item.employee_id, 'employee_name':item.employee_name,'vest_id':item.vest_id,'award_amount':str(item.award_amount)})

    for item in object_current_list:
        current_list.append({'employee_id': item.employee_id, 'employee_name':item.employee_name,'vest_id':item.vest_id,'award_amount':str(item.award_amount)})

    current = json.dumps(current_list, sort_keys=True)
    asser = json.dumps(assert_list, sort_keys=True)
    
    assert current == asser

def test_for_get_all_stage_three_part_two():
    serv = VestingAwardServiceImpl()
    filter_date="2021-01-01"
    file='tests/vestingfile-stage4.csv'
    assert_list = []
    object_list = []
    current_list =[]

    object_list.append(AwardEmployeeModel('ISO-001', '', '', '100.50',  'E001', 'Alice Smith'))
    object_list.append(AwardEmployeeModel('ISO-002', '', '', '100.45',  'E002', 'Bobby Jones'))
    object_current_list = serv.get_all_by_date_group_vest_id_and_employee_id(file,filter_date,2)

    for item in object_list:
        assert_list.append({'employee_id': item.employee_id, 'employee_name':item.employee_name,'vest_id':item.vest_id,'award_amount':str(item.award_amount)})

    for item in object_current_list:
        current_list.append({'employee_id': item.employee_id, 'employee_name':item.employee_name,'vest_id':item.vest_id,'award_amount':str(item.award_amount)})

    print(assert_list)   
    print(current_list)  
    
    current = json.dumps(current_list, sort_keys=True)
    asser = json.dumps(assert_list, sort_keys=True)
    
    assert current == asser
