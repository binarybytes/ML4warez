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

legit = malData[0:41323].drop(["legitimate"], axis=1)

mals = malData[41323::].drop(["legitimate"], axis=1)

print("the shape of legit dataset is, %s samples, %s features " %(legit.shape[0],legit.shape[1]))

print ("the shape of mals dataset is, %s samples, %s features " %(mals.shape[0],mals.shape[1]))
#run

