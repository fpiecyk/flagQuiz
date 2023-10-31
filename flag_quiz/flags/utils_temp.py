import random
from .models import FlagData


class AnswerVariants:

    def __init__(self):
        self.all_variants_list = []
        self.all_prompt_list = []
        self.score = 0




    def correct_answer_add(self):
        self.answer = random.choice(FlagData.objects.all())
        # answer = getattr(self.answer, "full_name")
        self.all_variants_list.append(self.answer)
        return self.answer
    
    def prompt_answer_add(self):
        for _ in range(3):
            self.prompt = random.choice(FlagData.objects.all())
            # prompt = getattr(self.prompt, "full_name")
            self.all_variants_list.append(self.prompt)
            sorted_flags = sorted(self.all_variants_list, key=lambda x: x.full_name)
        return sorted_flags
        

    def all_answers(self):
        return self.all_variants_list
    
