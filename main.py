from tkinter import *
from tkinter import messagebox, font
from PIL import Image, ImageTk
import time

## Importing Libraries
import random
import time
import sys
import os
import datetime
import warnings
from tarot_reader import TarotReader

warnings.filterwarnings("ignore")

## Importing Classes
# from opening import OpeningMessage
from PandasToList import PandasToList
from cards import cards
from pdf_converter import PDF
# from emailsender import EmailSender
from secret import sender_email, password  # .gitIgnore에 추가됨.
# from send_kakao import Send_kakao
# from google_drive_api import Google_Drive_Api

from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH/'assets/frame0'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# email_sender = EmailSender(sender_email, password)
# send_message=Send_kakao()

reader=TarotReader()

## Tarot Card import
p = PandasToList()
list_up_tarot = p.up_deck("TarotCardsUpright.csv")
list_rev_tarot = p.rev_deck("TarotCardsReversed.csv")

# big_font=font.Font(family='SCDream2.otf',size=50)
big_font=('SCDream2.otf',50)
normal_font=('S_Core_Dream\\SCDream2.otf',10)


class BeforeStartApp():
    def __init__(self,root):
        self.root=root

        self.root.configure(bg = "#FFFFFF")


        self.canvas = Canvas(
            self.root,
            bg = "#FFFFFF",
            height = 900,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x=0,y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1440.0,
            608.0,
            fill="#001C54",
            outline=""
        )

        self.button_image_1 = ImageTk.PhotoImage(
            Image.open("assets\\frame0\\button_1.png")
        )

        self.startButton=Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.goToClassicTarotApp,
            relief='flat'
        )
        self.startButton.place(
            x=438.9999999999999,
            y=685.0,
            width=562.0,
            height=142.0
        )
        self.canvas.create_text(
            392.9999999999999,
            241.00000000000006,
            anchor="nw",
            text="TAROT AI",
            fill="#41C1C3",
            font=("Arial Black", 128 * -1)
        )
        self.canvas.create_text(
            520,
            220,
            anchor="nw",
            text="2 0 2 4  S T E M  C A M P",
            fill="#41C1C3",
            font=("Arial Black", 32 * -1)
        )
    def goToClassicTarotApp(self):
        self.canvas.destroy()
        classicTarotApp=ClassicTarotApp(self.root)

class ClassicTarotApp():
    def __init__(self,root):
        self.root=root

        self.canvas = Canvas(
            self.root,
            bg = "#FFFFFF",
            height = 900,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x=0,y=0)
        
        self.canvas.create_text(
            392.9999999999999,
            241.00000000000006,
            anchor="nw",
            text="타로점 보기",
            fill="#41C1C3",
            font=("Arial Black", 128 * -1)
        )

        self.canvas.create_text(
            228.9999999999999,
            49.00000000000006,
            anchor="nw",
            text="안녕? 나는 오늘 너에게 잠깐이나마 미래를 보여줄 인공지능 Tarot AI야.",
            fill="#41C1C3",
            font=("Arial", 32 * -1)
        )

        self.canvas.create_text(
            287.9999999999999,
            88.00000000000006,
            anchor="nw",
            text="학교생활 많이 힘들지? 이렇게 시간 내서 점 보러 와줘서 고마워.",
            fill="#41C1C3",
            font=("Arial", 32 * -1)
        )

        self.canvas.create_text(
            197.9999999999999,
            127.00000000000006,
            anchor="nw",
            text="시작하기 전에, 네 이름과 MBTI를 알려줘. 진짜 이름 말고, 가명으로 적어도 돼.",
            fill="#41C1C3",
            font=("Arial", 32 * -1)
        )

        self.entry_image_1 = ImageTk.PhotoImage(
            Image.open("assets\\entry_1.png")
        )
        self.nameEntryImage = self.canvas.create_image(
            719.9999999999999,
            484.00000000000006,
            image=self.entry_image_1
        )
        self.nameEntry=Entry(self.canvas, bd=0,bg="#E7E7E7",fg="#000716",highlightthickness=0,font=("Arial", 40 * -1))
        self.nameEntry.place(x=121.99999999999989,y=450.00000000000006,width=1196.0,height=66.0)
        self.mbtiEntryImage = self.canvas.create_image(
            719.9999999999999,
            564.00000000000006,
            image=self.entry_image_1
        )
        self.mbtiEntry=Entry(self.canvas, bd=0,bg="#E7E7E7",fg="#000716",highlightthickness=0,font=("Arial", 40 * -1))
        self.mbtiEntry.place(x=121.99999999999989,y=530.00000000000006,width=1196.0,height=66.0)

        self.button_image_1 = ImageTk.PhotoImage(
            Image.open("assets\\button_1.png")
        )

        self.nameConfirmButton=Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=self.proceed1
        )
        self.nameConfirmButton.place(
            x=500.9999999999999,
            y=682.0,
            width=437.0,
            height=110.41636657714844
        )
        self.canvas.create_rectangle(
            0,
            209.00000000000006,
            1504.0,
            218.00000000000006,
            fill="#41C1C3",
            outline=""
        )
    
    def proceed1(self):
        global name
        name=self.nameEntry.get().replace('\n','')
        self.mbti=self.mbtiEntry.get().replace('\n','')
        if self.mbti!='':
            
            self.canvas.destroy()
            self.canvas=Canvas(
                self.root,
                bg = "#FFFFFF",
                height = 900,
                width = 1440,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )
            self.canvas.place(x=0,y=0)

            self.canvas.create_text(
                378.9999999999999,
                49.00000000000006,
                anchor="nw",
                text=f'네 이름은 {name}이구나. mbti는 {self.mbti}네,  반가워!',
                fill="#41C1C3",
                font=("Arial", 32 * -1)
            )

            self.canvas.create_text(
                307.9999999999999,
                88.00000000000006,
                anchor="nw",
                text="'오늘 내 운세는 어때' 같이 특정 기간의 운세를 봐줄 수도 있고,",
                fill="#41C1C3",
                font=("Arial", 32 * -1)
            )

            self.canvas.create_text(
                327.9999999999999,
                127.00000000000006,
                anchor="nw",
                text="'내가 연애를 할 수 있을까' 처럼 특정 고민을 적어줘도 좋아.",
                fill="#41C1C3",
                font=("Arial", 32 * -1)
            )

            self.entry_image_1 = ImageTk.PhotoImage(
                Image.open("assets\\concernEntry.png")
            )
            self.concernEntryImage = self.canvas.create_image(
                719.9999999999999,
                481.00000000000006,
                image=self.entry_image_1
            )
            self.concernEntry=Text(self.canvas, bd=0,bg="#E7E7E7",fg="#000716",highlightthickness=0,font=("Arial", 40 * -1))
            self.concernEntry.place(x=121.99999999999989,y=350.00000000000006,width=1196.0,height=264.0)

            self.button_image_1 = ImageTk.PhotoImage(
                Image.open("assets\\button_1.png")
            )

            self.concernConfirmButton=Button(
                self.canvas,
                image=self.button_image_1,
                borderwidth=0,
                highlightthickness=0,
                relief="flat",
                command=self.proceed2
            )
            self.concernConfirmButton.place(
                x=500.9999999999999,
                y=682.0,
                width=437.0,
                height=110.41636657714844
            )
            self.canvas.create_rectangle(
                0,
                209.00000000000006,
                1504.0,
                218.00000000000006,
                fill="#41C1C3",
                outline=""
            )
            
        else:
            messagebox.showerror('mbti가 뭐야?','mbti란을 비워둘 순 없어!')

    def proceed2(self):
        self.concern=self.concernEntry.get(1.0, 'end').replace('\n',' ')
        self.canvas.destroy()
        self.canvas=Canvas(
            self.root,
            bg = "#FFFFFF",
            height = 900,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x=0,y=0)
        self.showPrompot()


    def showPrompot(self):
        self.canvas.destroy()
        self.canvas=Canvas(
            self.root,
            bg = "#FFFFFF",
            height = 900,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x=0,y=0)
        reader.set_concern(self.concern)
        reader.set_mbti(self.mbti)
        reader.set_cards_num()
        self.card_num = reader.cards_num
        self.canvas.create_text(
                500,
                280,
                anchor="nw",
                text="좋아, 그럼 이제 카드를 뽑아볼까?",
                fill="#41C1C3",
                font=("Arial", 32 * -1)
            )

        self.button_image_1 = ImageTk.PhotoImage(
            Image.open("assets\\button_1.png")
        )
        self.yesButton=Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=self.goToClassicTarotCardPullApp
        )
        self.yesButton.place(
            x=500.9999999999999,
            y=682.0,
            width=437.0,
            height=110.41636657714844
        )

    def goToClassicTarotCardPullApp(self):
        self.canvas.destroy()
        tarotApp=ClassicTarotCardPullApp(self.root, self.card_num, self.concern)

class ClassicTarotCardPullApp():
    def __init__(self, root, card_num, concern):
        self.root=root
        self.card_num=card_num
        self.concern=concern

        self.mainFrame=Frame(self.root,width=1440,height=900)
        self.mainFrame.grid(column=0,row=0)

        self.canvas=Canvas(
            self.root,
            bg = "#FFFFFF",
            height = 900,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.canvas.create_text(
            565.9999999999999,
            0,
            anchor="nw",
            text="타로점 보기",
            fill="#001C54",
            font=("Arial Black", 64 * -1)
        )

        self.canvas.create_text(
            479.9999999999999,
            80.00000000000006,
            anchor="nw",
            text=f"지금부터 총 {card_num}개의 카드를 뽑을거야.",
            fill="#41C1C3",
            font=("Arial", 32 * -1)
        )

        self.canvas.create_text(
            419.9999999999999,
            129.00000000000006,
            anchor="nw",
            text="마음을 가다듬고, 너가 뽑고 싶은 카드를 뽑아줘.",
            fill="#41C1C3",
            font=("Arial", 32 * -1)
        )

        self.card_frame=[]
        self.image_path=[]
        self.image=[]
        self.label=[]
        self.originSize=(int(1144*0.13),int(1919*0.13))
        self.bigSize=(int(1144*0.16),int(1919*0.16))
        for i in range(0,21):
            self.display_card(0,i,40*i,0.5)
        for i in range(0,21):
            self.display_card(0,i+21,40*i,0.2)
        self.selected_card=[]


        self.button_image_1 = ImageTk.PhotoImage(
            Image.open("assets\\frame0\\button_2.png")
        )

        self.startButton=Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.next,
            relief="flat"
        )
        self.startButton.place(
            x=566.9999999999999,
            y=760.0,
            width=305.0,
            height=77.06405639648438
        )
    
    def display_card(self, card_index, index, x, y):
        self.card_frame.append(0)
        self.image_path.append(0)
        self.image.append(0)
        self.label.append(0)
        self.card_frame[index] = Frame(self.canvas, width=self.originSize[0], height=self.originSize[1],)
        self.card_frame[index].place(relx=x/(22*40), rely=y)
        
        self.image_path[index] = cards[card_index]['card']
        self.image[index] = ImageTk.PhotoImage(Image.open(self.image_path[index]).resize(self.originSize))
        
        self.label[index] = Label(self.card_frame[index], image=self.image[index], padx=10,pady=10)
        self.label[index].image = self.image[index]  # Keep a reference to the image to prevent garbage collection
        self.label[index].place(x=0, y=0)

        self.label[index].bind("<Enter>", (lambda event:self.on_enter(event, index)))
        self.label[index].bind("<Leave>", (lambda event:self.on_leave(event, index)))
        self.label[index].bind("<Button-1>", (lambda event:self.on_click(event, index)))
        
        
        return self.card_frame[index], self.label[index]
    
    def on_enter(self, event, index):
        self.card_frame[index].config(width=self.bigSize[0],height=self.bigSize[1])
        self.image[index]=ImageTk.PhotoImage(Image.open(self.image_path[index]).resize(self.bigSize))
        self.label[index].config(width=self.bigSize[0],height=self.bigSize[1],image=self.image[index])
    def on_leave(self, event, index):
        self.card_frame[index].config(width=self.originSize[0],height=self.originSize[1])
        self.image[index]=ImageTk.PhotoImage(Image.open(self.image_path[index]).resize(self.originSize))
        self.label[index].config(width=self.originSize[0],height=self.originSize[1],image=self.image[index])
    def on_click(self, event, index):
        if index in self.selected_card:
            self.selected_card.remove(index)
            self.card_frame[index].config(highlightthickness=0, highlightbackground='black')
        elif len(self.selected_card)<self.card_num:
            self.selected_card.append(index)
            self.card_frame[index].config(highlightthickness=4, highlightbackground='yellow')
        else:
            messagebox.showerror('카드 개수가 너무 많아요!',f'{self.card_num+1}개는 고를 수 없어!')
    def next(self):
        if len(self.selected_card)!=self.card_num:
            messagebox.showerror('아직 카드를 다 고르지 않았어!',f'{self.card_num}개의 카드를 골라줘!')
        else:
            self.canvas.destroy()
            interpretation_app=ClassicInterpretationApp(self.root, self.selected_card, self.concern)
            
class ClassicInterpretationApp():
    def __init__(self, root, selected_card, concern):
        self.root=root
        self.selected_card=selected_card
        self.concern=concern

        self.mainFrame=Frame(self.root)
        self.mainFrame.grid(column=0,row=0)

        self.titleLabel=Label(self.mainFrame,text='타로점 보기',font=("Arial Black", 64 * -1))
        self.titleLabel.grid(column=0,row=0)

        self.animation = '|/-\\'
        self.animationLabel=Label(self.mainFrame, text='')
        self.animationLabel.grid(column=0, row=1)

        self.updateAnimation()
        self.root.after(3000,self.showPromptFirst)


    def updateAnimation(self):
        self.animationLabel.config(text='응답 생성중...'+self.animation[int(time.time()*10)%len(self.animation)])
        self.root.after(100,self.updateAnimation)

    def showPromptFirst(self):
        self.animationLabel.destroy()
        self.list_tarot_deck_mixed=list_up_tarot + list_rev_tarot
        random.shuffle(self.list_tarot_deck_mixed)   
        self.first=self.list_tarot_deck_mixed[self.selected_card[0]]
        if len(self.selected_card)==3:
            self.second=self.list_tarot_deck_mixed[self.selected_card[1]]
            self.third=self.list_tarot_deck_mixed[self.selected_card[2]]
        if len(self.selected_card)==3:
            reader.set_cards([self.first,self.second,self.third])
        else:
            reader.set_cards([self.first])

        print(self.selected_card)
        reader.set_meaning_by_idx(0)
        reader.set_interpretation_by_idx(0)
        interpretations = reader.cards
        interpretation_word_first = interpretations[0]["meaning"]
        self.interpretation_concern_first = interpretations[0]["interpretation"]
        self.fName=self.first[1]

        self.fLabel=Label(self.mainFrame,text=self.fName+'\n'+interpretation_word_first+'\n'+self.interpretation_concern_first, wraplength=800,font=('',18))
        self.fLabel.grid(column=1,row=1)

        
        self.originSize=(114*2,191*2)
        for n in range(len(self.list_tarot_deck_mixed)+1):
            if self.first[0]==cards[n]['name']:
                self.fImagePath=cards[n]['card']
                self.fImage=ImageTk.PhotoImage(Image.open(self.fImagePath).resize(self.originSize))
        self.fImageLabel=Label(self.mainFrame,image=self.fImage)
        self.fImageLabel.grid(column=0,row=1)
        
        if len(self.selected_card)==3:
            self.nextSButton=Button(self.mainFrame,text='다음 카드',command=self.showPromptSecond)
            self.nextSButton.grid(column=0,row=2)
        else:
            self.overallButton=Button(self.mainFrame,text='종합',command=self.showOverall)
            self.overallButton.grid(column=0,row=2)

    def showPromptSecond(self):
        self.fLabel.destroy()
        self.fImageLabel.destroy()
        self.nextSButton.destroy()
        reader.set_meaning_by_idx(1)
        reader.set_interpretation_by_idx(1)
        interpretations = reader.cards
        interpretation_word_second = interpretations[1]["meaning"]
        self.interpretation_concern_second = interpretations[1]["interpretation"]
        
        self.sName=self.second[1]
        self.sLabel=Label(self.mainFrame,text=self.sName+'\n'+interpretation_word_second+'\n'+self.interpretation_concern_second, wraplength=800,font=('',18))
        self.sLabel.grid(column=1,row=1)


        for n in range(len(self.list_tarot_deck_mixed)+1):
            if self.second[0]==cards[n]['name']:
                self.sImagePath=cards[n]['card']
                self.sImage=ImageTk.PhotoImage(Image.open(self.sImagePath).resize(self.originSize))

        self.sImageLabel=Label(self.mainFrame,image=self.sImage)
        self.sImageLabel.grid(column=0,row=1)

        self.nextTButton=Button(self.mainFrame,text='다음 카드',command=self.showPromptThird)
        self.nextTButton.grid(column=0,row=2)

    def showPromptThird(self):
        self.sLabel.destroy()
        self.sImageLabel.destroy()
        self.nextTButton.destroy()

        reader.set_meaning_by_idx(2)
        reader.set_interpretation_by_idx(2)
        interpretations = reader.cards
        interpretation_word_third = interpretations[2]["meaning"]
        self.interpretation_concern_third = interpretations[2]["interpretation"]
        
        self.tName=self.third[1]
        self.tLabel=Label(self.mainFrame,text=self.tName+'\n'+interpretation_word_third+'\n'+self.interpretation_concern_third, wraplength=800,font=('',18))
        self.tLabel.grid(column=1,row=1)

        for n in range(len(self.list_tarot_deck_mixed)+1):
            if self.third[0]==cards[n]['name']:
                self.tImagePath=cards[n]['card']
                self.tImage=ImageTk.PhotoImage(Image.open(self.tImagePath).resize(self.originSize))
        self.tImageLabel=Label(self.mainFrame,image=self.tImage)
        self.tImageLabel.grid(column=0,row=1)

        self.overallButton=Button(self.mainFrame,text='종합',command=self.showOverall)
        self.overallButton.grid(column=0,row=2)
        

    def showOverall(self):
        if len(self.selected_card)==3:
            self.tLabel.destroy()
            self.tImageLabel.destroy()
        else:
            self.fLabel.destroy()
            self.fImageLabel.destroy()
        self.overallButton.destroy()
        reader.set_interpretation_overall()
        self.interpretation_overall = reader.interpretation_overall

        self.oLabel=Label(self.mainFrame,text=self.interpretation_overall, wraplength=800,font=('',18))
        self.oLabel.grid(column=2,row=1)

        self.endButton=Button(self.mainFrame,text='끝내기',command=self.end)
        self.endButton.grid(column=0,row=1)
        self.deepButton=Button(self.mainFrame,text='추가 질문',command=self.deep)
        self.deepButton.grid(column=1,row=1)
        
    def end(self):
        self.mainFrame.destroy()
        global pdf
        pdf = PDF(f"{name}")
        pdf.add_page()
        pdf.add_concern(self.concern)
        pdf.add_block(
            self.fImagePath,
            self.first[0],
            self.interpretation_concern_first,
        )
        if len(self.selected_card) == 3:
            pdf.add_block(
                self.sImagePath,
                self.second[0],
                self.interpretation_concern_second,
            )
            pdf.add_block(
                self.tImagePath,
                self.third[0],
                self.interpretation_concern_third,
            )
        pdf.add_result(self.interpretation_overall)
        # pdf.output(f"{name}_TarotAI_Result.pdf")
        # send_message.message_data(name, Google_Drive_Api.main(f'{name}_TarotAI_Result.pdf'), self.interpretation_overall)   
        classicEndApp=ClassicEndApp(self.root)
    def deep(self):
        self.oLabel.destroy()
        self.endButton.destroy()
        self.deepButton.destroy()
        
        self.deepString='추가적인 질문이 있다면 어떤 질문인지 얘기해줄래?'
        self.deepLabel=Label(self.mainFrame,text=self.deepString)
        self.deepLabel.grid(column=0,row=1)
        self.deepText=Text(self.mainFrame)
        self.deepText.grid(column=0,row=2)
        self.deepConfirmButton=Button(self.mainFrame,text='이게 궁금해',command=self.additionalAnswer)
        self.deepConfirmButton.grid(column=0,row=3)
    def additionalAnswer(self):
        reader.set_interpretation_overall_add(self.deepText.get(1.0,'end'), self.interpretation_overall)
        interpretation_overall_add=reader.interpretation_overall_add
        self.deepLabel.destroy()
        self.deepText.destroy()
        self.deepConfirmButton.destroy()
        self.deepFinal=Label(self.mainFrame,text=interpretation_overall_add, wraplength=500)
        self.deepFinal.grid(column=0,row=1)
        self.endButton=Button(self.mainFrame,text='끝내기', command=self.end)
        self.endButton.grid(column=0,row=2)

class ClassicEndApp():
    def __init__(self,root):
        self.root=root
        self.mainFrame=Frame(self.root)
        self.mainFrame.grid(column=0,row=0)

        self.titleLabel=Label(self.mainFrame,text='타로점 보기',font=big_font)
        self.titleLabel.grid(column=0,row=0)

        self.descString='여기까지가 내가 본 미래의 전부야.\n'
        self.descString+='어땠어? 결과가 마음에 들었으면 좋겠네.\n'
        self.descString+='이제 헤어질 시간이야.\n'
        self.descString+='오늘 본 점의 결과는 pdf 파일로 정리해서 카카오톡으로 보내줄게!\n'
        self.descLabel=Label(self.mainFrame,text=self.descString,font=('',18))
        self.descLabel.grid(column=0,row=1)

        descString=f'안녕, {name}!\n'
        descString+='오늘 타로 보러 와줘서 다시 한 번 고마워!!\n'
        descString+='타로 결과를 다시 보고 싶을 땐 카카오톡을 확인해봐.\n'
        descString+='그럼, 안녕!\n'
        descString+='TarotAI 올림.'
        self.descLabel=Label(self.mainFrame,text=descString,font=('',18))
        self.descLabel.grid(column=0,row=2)
        self.descLabel=Label(self.mainFrame,text=descString,font=('',18))
        self.descLabel.grid(column=0,row=2)
        

        self.endConfirmButton=Button(self.mainFrame,command=self.end,text='끝내기')
        self.endConfirmButton.grid(column=0,row=3)
    def end(self):
        self.mainFrame.destroy()
        beforeStartApp=BeforeStartApp(self.root)
        

        
window=Tk()
window.geometry("1440x900")
app=BeforeStartApp(window)
window.mainloop()