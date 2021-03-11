from functions import get_data, make_dic, take_users, call_data, take_another, take_change, convert_currency

data_list = get_data()
data_dic = make_dic(data_list)
call_data(data_dic)

cur1 = take_users(data_dic)
cur2 = take_another(data_dic)

print(cur1)
print(cur2)

print(format_currency(1000, cur1, u'¤ #,##0.00', locale='en-US'))
