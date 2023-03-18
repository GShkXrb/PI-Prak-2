import numpy as np
import array
import matplotlib.pyplot as plt

#Описание индикаторной функции
def Indicator(num):
    if num == 0:
        return 0
    if np.random.binomial(num, 1/num) == 1:
        return 1
    else:
        return 0
        
#Функция заполнения массива в соответствии с распределением Пуассона
def PoissonFill(Lambda, Length):
    PoissonArray = []
    PoissonArray = np.random.poisson(Lambda, Length)
    return PoissonArray

#Объявление таких переменных, как длины массивов, массивы с 
#средним #временем и средним количеством абонентов и др.
ArrLengthShow = 30
ArrLength = 100000
AverageUsers = 0
AverageTime = 0
AverageUsersList = []
AverageTimeList = []
PoissLambda = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]

#Вывод примера работы программы на массиве малого размера
for lambd in PoissLambda:
    print('Лямбда =', lambd)

    print()

    StartArray = []
    EndArray = []

    Array = PoissonFill(lambd, ArrLengthShow)

    print('Массив, заполненный в соответствии с распределением Пуассона')

    for i in range(len(Array)):
        print(Array[i], end = ' ')

    print()

    #Расчет N для каждого слота в цикле
    for i in range(len(Array)):
        if i + 1 < len(Array):
            StartArray.append(Array[i])
            Array[i] -= Indicator(Array[i])
            EndArray.append(Array[i])
            Array[i+1] += Array[i]
            Array[i] = 0
        else:
            StartArray.append(Array[i])
            Array[i] -= Indicator(Array[i])
            EndArray.append(Array[i])

    #Вывод на экран информации об изменениях в массивах в ходе работы
    print('Количество абонентов в начале слота')

    for i in range(len(StartArray)):
        print(StartArray[i], end = ' ')

    print()

    print('Количество абонентов в конце слота ')

    for i in range(len(EndArray)):
        print(EndArray[i], end = ' ')

    print()

    print('Массив после моделирования')

    for i in range(len(Array)):
        print(Array[i], end = ' ')

    print()
    print()

#Основная часть программы, размер массива - 100000
for lambd in PoissLambda:

    Array = PoissonFill(lambd, ArrLength)

    #Расчет N для каждого слота в цикле
    for i in range(len(Array)):
        if i + 1 < len(Array):
            Array[i] -= Indicator(Array[i])
            Array[i+1] += Array[i]
        else:
            Array[i] -= Indicator(Array[i])
        #Запись количества абонентов в слоте в отдельную переменную 
        AverageUsers += Array[i]
    AverageUsers /= ArrLength
    #Запись количества абонентов в массив
    AverageUsersList.append(AverageUsers)
    AverageTime = AverageUsers/lambd
    #Запись количества времени на абонента в массив
    AverageTimeList.append(AverageTime)
    AverageUsers = 0
    AverageTime = 0

#Вывод графиков

plt.plot(PoissLambda, AverageUsersList)
plt.title('График зависимости среднего количества абонентов в системе от интенсивности входного потока\n')
plt.xlabel('Интенсивность входного потока, λ')
plt.ylabel('Среднее количество абонентов в системе, N')
plt.ylim([0, 2000])
plt.grid()
plt.show()

plt.plot(PoissLambda, AverageTimeList)
plt.title('График зависимости среднего времени нахождения абонентов в системе от интенсивности входного потока\n')
plt.xlabel('Интенсивность входного потока, λ')
plt.ylabel('Среднее время нахождения абонентов в системе, T')
plt.ylim([0, 2000])
plt.grid()
plt.show()