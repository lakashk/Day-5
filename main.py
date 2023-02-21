import pandas as pd

# temp = pd.read_csv('AB_US_2020.csv')
# print(temp.head)
# print(temp.to_string())
# print(type(temp))

# my_ds = {
#     "foods": ["Pizza","Fried Rice", "Momos"],
#     "movies": ["harry","potter","fast"]
# }

# my_data_frame = pd.DataFrame(my_ds)
# # print(type(my_ds))
# print(my_data_frame.head())
#
# data_frame = pd.DataFrame(my_ds, columns=["akash fav food","rishab fav food "])
# print(data_frame)

#l1 nad l2 and column name create data frame
# l1 = ["Harry","Ronnie","raju"]
# l2 = ["Voldermot","Tom Riddle","Babu bhiya"]
# col = ["heros","Villans"]

# temp_dict = {
#     col[0]:l1,
#     col[1]:l2
# }

# a_o_a = list(zip(l1,l2))
# print(type(a_o_a["Harry"]))

# df = pd.DataFrame(columns= col,data=a_o_a)
# print(df)

# ls1 = pd.Series(["Harry","Ronnie","raju"])
# ls2 = pd.Series(["Voldermot","Tom Riddle","Babu bhiya"])
# col1 = ["heros","Villans"]
# print(ls1)



#read csv

house_price = pd.read_csv("AB_US_2020.csv")
# print(house_price.iloc[10])
# print(house_price.iloc[3:4,0:4])
# print(house_price.iloc[[0,3,7]])
# print(house_price.iloc[0:,0:2])

# print(house_price.iloc[lambda x:x.index % 2 == 0])

# print(house_price.loc[0:,["name", "host_name","availability_365"]])
# print(house_price.loc[10:100,["name", "host_name","availability_365"]])

temp = house_pr
print()