import random
content = "pl1,pl2,pr1,pr2\n"

for i in range(100):
    content += str(round(random.random()*20, 2)) + "," + str(round(random.random()*20, 2)) + "," + str(round(random.random()*20, 2)) + "," + str(round(random.random()*20,2)) +"\n"
with open("data.csv", "w") as file:
    file.write(content)
