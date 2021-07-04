from Question import Question
import random
from tkinter import*
import pygame


ques1 = Question ("1+1=? ",("2", True), ("3", False), ("4", False), ("5", False))
ques2 = Question ("2+2=? ",("2", False), ("3", False), ("4", True), ("5", False))
ques3 = Question ("3+4=? ",("8", False), ("5", False), ("9", False), ("7", True))
ques4 = Question ("5+4=? ",("10", False), ("9", True), ("7", False), ("8", False))
ques5 = Question ("11+7=? ",("18", True), ("17", False), ("21", False), ("20", False))
ques6 = Question ("10-9=? ",("8", False), ("1", True), ("7", False), ("6", False))
ques7 = Question ("5x4=? ",("20", True), ("15", False), ("19", False), ("17", False))
ques8 = Question ("10/2=? ",("8", False), ("5", True), ("3", False), ("4", False))
ques9 = Question ("3x6=? ",("12", False), ("13", False), ("18", True), ("10", False))
ques10 = Question ("6X6=? ",("36", True), ("25", False), ("39", False), ("31", False))
ques11 = Question ("7x8=? ",("51", False), ("56", True), ("69", False), ("47", False))
ques12 = Question ("8X5=? ",("38", False), ("35", False), ("53", False), ("40", True))
ques13 = Question ("4X4=? ",("18", False), ("16", True), ("19", False), ("12", False))
ques14 = Question ("12X12=? ",("144", True), ("135", False), ("139", False), ("147", False))
ques15 = Question ("14X8=? ",("128", False), ("112",True), ("119", False), ("127", False))
ques16 = Question ("WON!", (":)", True), (":)", True),(":)", True),(":)", True))



questions = [ques1, ques2, ques3, ques4, ques5, ques6, ques7, ques8,
             ques9, ques10, ques11, ques12, ques13, ques14, ques15]

