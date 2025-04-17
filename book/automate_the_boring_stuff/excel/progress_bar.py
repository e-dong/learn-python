import time

class ProgressBar:
    def __init__(self, max):
        self.progress = ""
        self.max = max
        self.part = 0
    
    def render(self):
        self.part += 1
        self.progress += "="
        remaining_space = self.max - self.part
        time.sleep(0.1)
        perc_str = "{:.2f}".format(round((self.part/self.max) * 100, 2))
        frac_str = f"({str(self.part)}/{self.max})"
        bar_str = "[" + self.progress + ">" +  f"{remaining_space * ' '}]"
     
        print("\r", "{0:>6} {1}{2}".format(perc_str, frac_str, bar_str), end="")

