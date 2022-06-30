import csv
player_list = ["Will", "Parker", "Jackson", "Hastings"]
act_data = {"Homerun": 0, "Stolen Base": 0, "Runs": 0, "RBI": 0, "Walks": 0, "Strikeouts":0}
count_dict = {"Will": 0, "Parker": 0, "Jackson":0, "Hastings": 0}
will_dif = {"Homerun": 0, "Stolen Base": 0, "Runs": 0, "RBI": 0, "Walks": 0, "Strikeouts":0}
park_dif = {"Homerun": 0, "Stolen Base": 0, "Runs": 0, "RBI": 0, "Walks": 0, "Strikeouts":0}
jack_dif = {"Homerun": 0, "Stolen Base": 0, "Runs": 0, "RBI": 0, "Walks": 0, "Strikeouts":0}
hast_dif = {"Homerun": 0, "Stolen Base": 0, "Runs": 0, "RBI": 0, "Walks": 0, "Strikeouts":0}
homerun_dif = []
stole_base_dif = []
runs_dif = []
rbi_dif = []
walks_dif = []
strike_out_dif = []

filename = r"Z:\\Users\\WKerby\\My Computer\\Documents\\Python\braves-nationals\\BravesNatsData.csv"
with open(filename, 'r') as file_object:
    reader = list(csv.reader(file_object))
for i in list(range(6)):
    act_data[list(act_data.keys())[i]] = int(reader[i+1][1])

for i in list(range((len(reader)-1))):
    will_dif[list(act_data.keys())[i]] = abs(int(reader[i+1][1]) - int(reader[i+1][2]))
    park_dif[list(act_data.keys())[i]] = abs(int(reader[i+1][1]) - int(reader[i+1][3]))
    jack_dif[list(act_data.keys())[i]] = abs(int(reader[i+1][1]) - int(reader[i+1][4]))
    hast_dif[list(act_data.keys())[i]] = abs(int(reader[i+1][1]) - int(reader[i+1][5]))


name_list = [will_dif, park_dif, jack_dif, hast_dif]
for i in name_list:
    homerun_dif.append(i["Homerun"])
    stole_base_dif.append(i["Stolen Base"])
    runs_dif.append(i["Runs"])
    rbi_dif.append(i["RBI"])
    walks_dif.append(i["Walks"])
    strike_out_dif.append(i["Strikeouts"])

best_index = []
dif_name_list = [homerun_dif,stole_base_dif,runs_dif,rbi_dif,walks_dif,strike_out_dif]
for name in dif_name_list:
    blank_list = []
    for i,x in enumerate(name):
        if x == min(name):
            blank_list.append(i)
    best_index.append(blank_list)
count_dict = {"Will": 0, "Parker": 0, "Jackson": 0, "Hastings": 0} 
for index in best_index:
    if len(index) > 1:
        pass
    else:
        for i in player_list:
            if index[0] == player_list.index(i):
                count_dict[i] += 1

print("The winner is " + str(player_list[list(count_dict.values()).index(max(list(count_dict.values())))]) + "!")

#define the datasets to be used in the histogram
header_row = [reader[i][0] for i in list(range(1,7))]
act_data_y_values = [int(reader[i][1]) for i in list(range(1,7))]
will_data = [int(reader[i][2]) for i in list(range(1,7))]
park_data = [int(reader[i][3]) for i in list(range(1,7))]
jack_data = [int(reader[i][4]) for i in list(range(1,7))]
hast_data = [int(reader[i][5]) for i in list(range(1,7))]

#plot a line graph with two series of data
from matplotlib import pyplot as plt
stat_name_list = ["Homeruns", "Stolen Bases","Runs","RBIs","Walks","Strikeouts"]
x_axis = [1,2,3,4,5]
plt.plot(stat_name_list,will_data,c = 'blue',label = "Will's guess")
plt.plot(stat_name_list,act_data_y_values, c = 'red',label = "Actual num. occurrences")
plt.xlabel("",fontsize = 12)
plt.ylabel("Number of occurences")
plt.tick_params(axis = "both",labelsize = 14)
plt.legend()
plt.show()



#plot a histogram
import pygal
stat_name_list = ["Homeruns", "Stolen Bases","Runs","RBIs","Walks","Strikeouts"]
histogram = pygal.Bar()
histogram.title = "Braves v. Nationals 8-7-2021"
histogram.x_labels = ["Homeruns", "Stolen Bases","Runs","RBIs","Walks","Strikeouts"]
histogram.x_title = "Stat"
histogram.y_title = "Number of Occurrences"
histogram.add("Actual num. occurrences", act_data_y_values)
histogram.add("Will's guess", will_data)
histogram.render_to_file('bravesnats.svg')



    
            
    
            
            
    
    
    
    
    



        
        
            
        
        
        
    
