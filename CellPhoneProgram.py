import CellPhoneClass as c 

ipohone = c.CellPhone('Apple', '12', '1,000')
print(ipohone.get_manufact())
print(ipohone.get_model())
print(ipohone.get_retail_price())

samsung = c.CellPhone('Samsung', 'Galaxy', '800' )
print(samsung.get_manufact())
print(samsung.get_model())
print(samsung.get_retail_price())
