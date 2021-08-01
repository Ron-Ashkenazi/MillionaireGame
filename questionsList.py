from Question import Question
import random
from tkinter import*
import pygame


ques1 = Question ("1+1=? ",("2", True), ("3", False), ("4", False), ("5", False))
ques2 = Question ("10-9=? ",("8", False), ("1", True), ("7", False), ("6", False))
ques3 = Question ("3x6=? ",("12", False), ("13", False), ("18", True), ("10", False))
ques4 = Question ("10/2=? ",("8", False), ("5", True), ("3", False), ("4", False))
ques5 = Question ("11+7=? ",("18", True), ("17", False), ("21", False), ("20", False))

ques6 = Question ("(10-6)x8=? ",("27", False), ("32", True), ("36", False), ("40", False))
ques7 = Question ("5x4/2=? ",("10", True), ("15", False), ("20", False), ("25", False))
ques8 = Question ("10+2x6=? ",("72", False), ("22", True), ("20", False), ("28", False))
ques9 = Question ("3x6/9=? ",("6", False), ("3", False), ("2", True), ("4", False))
ques10 = Question ("5+6X6=? ",("41", True), ("45", False), ("39", False), ("50", False))

ques11 = Question ("3x3x3x3=? ",("27", False), ("81", True), ("90", False), ("60", False))
ques12 = Question ("(8X5/2)x6=? ",("112", False), ("124", False), ("100", False), ("120", True))
ques13 = Question ("4X4x8/2=? ",("48", False), ("64", True), ("56", False), ("72", False))
ques14 = Question ("12X12x3=? ",("432", True), ("345", False), ("512", False), ("404", False))
ques15 = Question ("(14X8)/4+(6/2)=? ",("36", False), ("31",True), ("41", False), ("27", False))

ques16 = Question ("WON!", (":)", True), (":)", True),(":)", True),(":)", True))

easyQuestions = [ques1, ques2, ques3, ques4, ques5]
normalQuestions = [ques6, ques7, ques8, ques9, ques10]
hardQuestions = [ques11, ques12, ques13, ques14, ques15]

random.shuffle(easyQuestions)
random.shuffle(normalQuestions)
random.shuffle(hardQuestions)

questions = [ easyQuestions[0], easyQuestions[1], easyQuestions[2], easyQuestions[3], easyQuestions[4],
             normalQuestions[0], normalQuestions[1], normalQuestions[2], normalQuestions[3], normalQuestions[4],
             hardQuestions[0], hardQuestions[1], hardQuestions[2], hardQuestions[3], hardQuestions[4] ]

