'''
Module Name : Average Calculation
Description : This module contains the calculation of Mean , Median , Mode , Variance , Standard Deviation
Author : Siam Hasan
Date : 10-15-2022
'''
from audioop import avg
import math


class AvgCalc:
    def __init__(self, userInputList) -> None:
        self.list = userInputList

    def mean(self) -> int:
        list = self.list
        length = len(list)
        sum = 0
        for num in list:
            sum += num
        mean = sum / length
        return mean

    def median(self) -> int:
        list = self.list
        length = len(list)
        avg = (length + 1) / 2

        if (avg % 2) == 0 or (avg % 2) == 1:
            mode = list[int(avg) - 1]
            return mode
        else:
            mode = (list[int(avg) - 1] + list[math.ceil(avg) - 1]) / 2
            return mode
