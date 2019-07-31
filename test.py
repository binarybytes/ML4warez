#1-make sure that pefile/pandas is installed
# $ sudo apt install python3-pip
# $ pip3 install pefile
# $ pip3 install pandas

#2-download malware dataset + gunzip it to same dir where script lives
#https://github.com/chihebchebbi/Mastering-Machine-Learning-for-Penetration-Testing/blob/master/Chapter03/MalwareData.csv.gz
#gunzip MalwareData.csv.gz

#import libraries
import pandas as pd

#instantiate the csv
malData = pd.read_csv("MalwareData.csv", sep="|")

legit = malData[0:41323].drop(["legitimate"])

