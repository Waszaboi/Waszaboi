import os
import tensorflow as tf
import keras
import pandas as pd
import sklearn
import numpy as np
from sklearn import linear_model
from sklearn.utils import shuffle


fut=True
while fut:
    print("Training adatok:\n")
    invalid=True
    while invalid:
        if input("Beírod manuálisan az adatokat?(y/n): ")=="n":
            csvdata=input("Data fileneve: ")
            try:
                data = pd.read_csv(csvdata, sep=";")
                invalid=False
            except:
                pass
        else:
            beirt = open("beirt.csv", "w+")
            N=int(input("Adatsorok száma: "))
            adattipusok=[]
            tipusok=input("Adattípusok: ").split()
            i=1
            for x in tipusok:
                adattipusok.append(x)
                if i < len(tipusok):
                    beirt.write(x+";")
                else:
                    beirt.write(x)
                i+=1
            print("Adatok:")
            for x in range(N):
                beirt.write("\n")
                i=1
                for y in [int(z) for z in input().split()]:
                    if i < len(tipusok):
                        beirt.write(str(y)+";")
                    else:
                        beirt.write(str(y))
                    i+=1

            beirt.close()
            try:
                data = pd.read_csv("beirt.csv", sep=";")
                invalid=False
            except:
                pass
        if invalid:
            print("Invalid input!")

    #print(data)

    adat=True
    while adat:
        predict = input("Melyik adattípust számítsuk ki?: ")

        x = np.array(data.drop([predict], 1))

        #print("x:\n",x)

        y = np.array(data[predict])

        #print("y:\n",y)

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y)

        """
        print("x_train:\n",x_train)
        print("x_test:\n",x_test)
        print("y_train:\n",y_train)
        print("y_test:\n",y_test)
        """

        linear=linear_model.LinearRegression()

        linear.fit(x_train, y_train)
        acc=linear.score(x_test,y_test)

        print("Várható ponosság: ",float(acc//0.001/10),"%",sep="")

        #print("Co: ",linear.coef_)
        #print("Intercept: ",linear.intercept_ )

        predictions= linear.predict(x_test)



        kis = True
        while kis:
            x_test = []
            for z in input("Kiszámítandó adatok (a kiszámítandó elem helyére írj ?-t): ").split():
                if z != "?":
                    x_test.append(int(z))

            prediction=linear.predict([x_test])

            print(prediction[0])

            if input("Adsz meg új a kiszámítási elemet?(y/n): ")=="y":
                kis=False
        if input("Adsz meg új training adatokat?(y/n): ")=="y":
            adat=False

    if input("Bezárod a programot?(y/n): ")=="y":
        fut=False

        #for i in range(len(predictions)):
        #    print(predictions[i], x_test[i],y_test[i])

    #TODO: megcsinálni univerzális inputra, loopoltatni 3-szorosan