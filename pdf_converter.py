import os
from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    current_x = 10
    current_y = 30
    block_num = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        current_dir = os.path.dirname(os.path.abspath(__file__))
        regular_font_path = os.path.join(
            current_dir, "JetBrainsMono", "JetBrainsMonoNerdFont-Regular.ttf"
        )
        bold_font_path = os.path.join(
            current_dir, "JetBrainsMono", "JetBrainsMonoNerdFont-Bold.ttf"
        )
        italic_font_path = os.path.join(
            current_dir, "JetBrainsMono", "JetBrainsMonoNerdFont-Italic.ttf"
        )
        korean_font_path = os.path.join(current_dir, "S_Core_Dream", "SCDream2.ttf")
        korean_bold_font_path = os.path.join(
            current_dir, "S_Core_Dream", "SCDream5.ttf"
        )

        self.add_font("JetBrainsMono", "", regular_font_path, uni=True)
        self.add_font("JetBrainsMono", "B", bold_font_path, uni=True)
        self.add_font("JetBrainsMono", "I", italic_font_path, uni=True)
        self.add_font("SCDream2", "", korean_font_path, uni=True)
        self.add_font("SCDream5", "", korean_bold_font_path, uni=True)

    def header(self):
        self.set_font("SCDream5", "", 20)
        self.cell(0, 10, f"{self.name}'s Tarot Result", 0, 1, "C")
        self.set_font("JetBrainsMono", "", 10)
        self.cell(0, 10, "2024-05-14", 0, 1, "R")

    def footer(self):
        self.set_y(-15)
        self.set_font("JetBrainsMono", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    def add_concern(self, concern):
        self.point_return()
        self.set_font("SCDream5", "", 20)
        self.multi_cell(0, 10, f"concern: {concern}")

        self.point_return()
        self.add_y(max(15, (len(concern) + 20) // 45 * 15))



    def add_block(self, ascii_card, card_name, comment):
        if self.current_y >= 170:
            self.add_page()
            self.current_y = 30

        self.point_return()
        self.multi_cell(0, 5)  
        self.image(ascii_card, x=self.current_x, y=self.current_y, w=60)

        self.point_return()
        self.add_y(5)
        self.add_x(70)
        self.set_font("JetBrainsMono", "B", 13)
        self.multi_cell(0, 5, card_name)
        self.add_y(10)
        self.add_x(0)
        self.set_font("SCDream2", "", 11)
        self.multi_cell(0, 7, comment)

        self.add_x(-70)
        self.point_return()
        self.add_y(max(100, (len(comment) // 35 + len(card_name) // 35 + 3) * 5))
        for i in range(((len(comment) // 35 + len(card_name) // 35 + 3) * 5) // 275):
            self.add_page()
            self.current_y = 30
        self.block_num += 1

    def add_result(self, result):
        necessary_space = 40
        result_height = (len(result) + 20) // 45 * 15
        if self.current_y + necessary_space + result_height >= 275:
            self.add_page()
            self.current_y = 30
        
        self.point_return()
        self.add_y(20)
        self.set_font("SCDream5", "", 15)
        self.multi_cell(0, 7, "Result")

        self.add_y(10)
        self.set_font("SCDream2", "", 11)
        self.multi_cell(0, 7, result)
        
        self.point_return()
        self.add_y(max(15, result_height))

    def add_x(self, x):
        self.set_x(self.current_x + x)
        self.current_x += x

    def add_y(self, y):
        print(self.current_y, end=" ")
        self.set_y(self.current_y + y)
        self.current_y += y
        print(self.current_y)
        while self.current_y > 275:
            self.current_y -= 240
        if self.current_y < 30:
            self.current_y = 30

    def point_return(self):
        self.set_y(self.current_y)
        self.set_x(self.current_x)
