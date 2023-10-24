import csv
import random
from tkinter import *
from PIL import ImageTk, Image
from .models import FlagData

def create_flag_list():
    with open("source_files\country_codes.csv", "r") as file:
        content = csv.DictReader(file, delimiter=";")

        # full_name = []
        # short_name = []
        for row in content:
            instance = FlagData(row['full_name'],row['short_name'], row['flag_img'])
            instance.save()