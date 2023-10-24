import csv
import random
from tkinter import *
from PIL import ImageTk, Image
from .models import FlagData

class FlagListTotal:

    def __init__(self):
        self.flaglist = []



flag_total = FlagListTotal()

class Flags:
    def __init__(self, full_name, short_name, flag_img):
        self.full_name = full_name
        self.short_name = short_name
        self.flag_img = flag_img

    def __repr__(self):
        return f"{self.full_name} | {self.short_name} | {self.flag_img}"

def create_flag_list():
    with open("country_codes.csv", "r") as file:
        content = csv.DictReader(file, delimiter=";")

        # full_name = []
        # short_name = []
        for row in content:
            instance = FlagData(row['full_name'],row['short_name'], row['flag_img'])
            # flag_total.flaglist.append(instance_id)
    #         print(instance_id.full_name)
    # #
    # for flag in flag_total.flaglist:
    #     print(flag)


class QuizQuestion:

    def __init__(self):
        self.list_of_answers = []


class AnswerVariants:

    def __init__(self):
        self.answer_list = []
        self.prompt_list = []
        self.all_variants = []
        self.answer = None
        self.prompt = None
        self.score = 0

    def correct_answer_add(self):
        self.answer = random.choice(flag_total.flaglist)
        answer = getattr(self.answer, "full_name")
        self.answer_list.append(answer)

    def correct_answer_remove(self):
        self.answer_list.clear()
        self.answer = None
    def prompt_answer_add(self):
        for i in range(3):
            self.prompt = random.choice(flag_total.flaglist)
            prompt = getattr(self.prompt, "full_name")
            self.prompt_list.append(prompt)

    def prompt_answer_discard(self):
        self.prompt_list.clear()

    def all_variants_completion(self):
        self.correct_answer_add()
        self.prompt_answer_add()
        self.all_variants = self.answer_list + self.prompt_list

        return self.all_variants

    def clear_all_variants(self):
        self.correct_answer_remove()
        self.prompt_answer_discard()
        self.all_variants.clear()
    def check_answer(self, event):
        user_answer = event.widget.cget('text')

        def close_image():
            win2.destroy()

        if user_answer in self.answer_list:
            self.score += 1
            win2 = Toplevel()
            win2.geometry("300x200")
            info = Label(win2, text="Gratulacje, poprawna odpowiedź!")
            info.pack()
            text = f"Zdobyte punkty: {self.score}"
            score_box = Label(win2, text=text, bg="blue", fg="yellow", pady=5)
            score_box.pack()
            button_close = Button(win2, text="Close", command=close_image)
            button_close.pack()
            win2.mainloop()

        else:
            win2 = Toplevel()
            win2.geometry("300x200")
            info = Label(win2, text="Przegryw!")
            info.pack()
            button_close = Button(win2, text="Close", command=close_image)
            button_close.pack()
            win2.mainloop()

        # self.clear_all_variants()

object_answer = AnswerVariants()

# print(object_answer.all_variants_completion())
# print(object_answer.answer)




def display_image():
    object_answer.all_variants_completion()
    # print(event)
    def close_image():
        win.destroy()

    def next_question_frame():
        win.destroy()
        object_answer.clear_all_variants()
        display_image()

    # Define the geometry of the window
    win = Tk()
    win.geometry("900x700")

    frame2 = Frame(win, width=600, height=400)
    frame2.place(anchor='center', relx=0.5, rely=0.5)

    img_name = getattr(object_answer.answer, "flag_img")
    img = ImageTk.PhotoImage(Image.open("Flags/"+ img_name))

    # Create a Label Widget to display the text or Image
    label = Label(frame2, image=img)
    label.pack()

    for country in sorted(object_answer.all_variants):
        button = Button(frame2, text=country, width=50)
        # user_answer = button.cget('text')
        button.bind("<Button-1>", object_answer.check_answer)
        button.pack()

    button_next = Button(frame2, text="Next question", command=next_question_frame)
    button_next.pack()
    button_close = Button(frame2, text="Close", command=close_image)
    button_close.pack()
    win.mainloop()


display_image()
print(object_answer.answer)
print(object_answer.answer_list)
print(object_answer.prompt_list)
print(object_answer.all_variants)