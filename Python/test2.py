from functions import get_data, make_dic, take_users, call_data, take_another, take_change, convert_currency

data_list = get_data()
data_dic = make_dic(data_list)
call_data(data_dic)

take_users(data_dic)
take_another(data_dic)