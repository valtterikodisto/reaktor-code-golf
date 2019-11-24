import requests as j
print(j.get("http://bit.ly/2OIh10W").text.split("nt=")[15][1:6])