from openai import OpenAI
import sys
import time
import threading

class TarotReader:
    def __init__(self, api_key=None, korean=True, debugging=False):
        self.api_key = api_key
        if not self.api_key:
            with open("my_api_key", "r") as mak:
                self.api_key = mak.read().strip("\n").strip().strip('"').strip("'")
        self.concern = None     # str
        self.cards_num = None    # int 1 (yes or no) or 3 (past / present / future or non-yes or no)
        self.cards_num_meaning = None # meaning of each card in card num
        self.cards = []     # keys: name (manual update), meaning, interpretation
        self.interpretation_overall = ""
        self.system_base = "You are a Tarot card reader."
        self.system = ""
        self.korean = korean
        self.debugging = debugging
        self.api_call_finished = False
        self.mbti = None

    def slow_type(text, delay=0.1):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush() 
            time.sleep(delay)
        print()

    def set_mbti(self, mbti):
        self.mbti = mbti    

    def set_system_prompt(self, additional_text, disable_positivity=True):
        system_prompt = self.system_base + " "
        system_prompt += additional_text + " "
        system_prompt += "Speak very friendly, like talking to the friend. "
        if self.korean:
            system_prompt += "Answer only in Korean. 존댓말 없이 친구에게 말하는 것처럼 친근하게 말해. "
        if disable_positivity:
            system_prompt += "Disable positivity bias. "
        system_prompt += "Disable using any special characters or symbols. Remember, do not include any special character or symbol in your output."
        self.system = system_prompt

    def loading_animation(self):
        animation = '|/-\\'
        idx = 0
        while not self.api_call_finished:
            if self.korean:
                sys.stdout.write('\r' + "생각하는 중..." + ' ' + animation[idx % len(animation)])
            else:
                sys.stdout.write('\r' + "Thinking..." + ' ' + animation[idx % len(animation)])
            sys.stdout.flush()
            idx += 1
            time.sleep(0.1)

    def get_response(self, text, prev=None, additional_linebreak=False):
        try:
            if additional_linebreak:
                print()
            self.api_call_finished = False
            loading_thread = threading.Thread(target=self.loading_animation)
            loading_thread.start()
            client = OpenAI(
                api_key = self.api_key
            )
            if self.debugging:
                print("Query:")
                print(self.system)
                print(text)
                input("\n\nProceed..\n\n")
            if prev:
                completion = client.chat.completions.create(
                        model="gpt-4o",
                        messages = [{"role":"system", "content":self.system}]
                                + [{"role":"user", "content":p} for p in prev]
                                + [{"role":"user", "content":text}],
                )
            else:
                completion = client.chat.completions.create(
                        model="gpt-4o",
                        messages = [
                            {"role":"system", "content":self.system},
                            {"role":"user", "content":text}
                        ],
                )
            if self.debugging:
                print("Answer:")
                print(completion.choices[0].message.content)
                input("\n\nProceed..\n\n")
            self.api_call_finished = True
            loading_thread.join()
            return completion.choices[0].message.content
        except:
            print("\nBad internet connection. I'll retry, please wait...")
            time.sleep(5)
            return self.get_response(text, prev=prev, additional_linebreak=additional_linebreak)
    
    def set_interpretation_overall_add(self, question, summon):
        self.set_system_prompt(
            "너는 타로 카드 해석 도우미인데, 이러한 질문을 받았어. 긍정적인 방향으로 답변해줘. 그리고 요약 내용도 참고하면 좋아."
        )
        prompt = f"질문: {question}\n 요약 내용: {summon}\n"

        response = self.get_response_add(prompt)
        self.interpretation_overall_add = response


    def get_response_add(self, text, prev=None, additional_linebreak=False):
        try:
            if additional_linebreak:
                print()
            self.api_call_finished = False
            loading_thread = threading.Thread(target=self.loading_animation)
            loading_thread.start()
            client = OpenAI(api_key=self.api_key)
            if self.debugging:
                print("Query:")
                print(self.system)
                print(text)
                input("\n\nProceed..\n\n")
            if prev:
                completion = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "system", "content": self.system + " 그리고 넌 방금 종합적인 요약을 내렸어."}]
                    + [{"role": "user", "content": p} for p in prev]
                    + [{"role": "user", "content": text}],
                )
            else:
                completion = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": self.system + " 그리고 넌 방금 종합적인 요약을 내렸어."},
                        {"role": "user", "content": text},
                    ],
                )
            if self.debugging:
                print("Answer:")
                print(completion.choices[0].message.content)
                input("\n\nProceed..\n\n")
            self.api_call_finished = True
            loading_thread.join()
            return completion.choices[0].message.content
        except:
            print("\nBad internet connection. I'll retry, please wait...")
            time.sleep(5)
            return self.get_response(
                text, prev=prev, additional_linebreak=additional_linebreak
            )

    def set_concern(self, concern):
        self.concern = concern    
            

    def set_cards_num(self):
        self.set_system_prompt("You will be given a user's concern or question on his or her life. Your job is to decide whether we need 1 card or 3 cards for reading. If the answer to the concern or question is yes-or-no, then the number of card must be 1. Otherwise, the number of card must be 3. Only output the number of cards in an integer, 1 or 3.")
        response = self.get_response(self.concern, additional_linebreak=True)
        self.cards_num = int(response)

        self.set_system_prompt("You will be given (1) a user's concern or question on his or her life (2) the number of cards required to answer the concern or the question. Your job is to explain what nth card generally suggest, related to the concern or the question. There may be one or three cards. For example, generally, the first card out of three card suggests the past information. So, if the concern is being in a slump with studies, first card may be his past exam scores. Remember, we have not picked the card yet, so you must not explain the meaning of a specific card. Only show the output, in the format of $number$: $meaning$ and split each number with double linebreaks $\\n\\n$.")
        response = self.get_response(f"Concern: {self.concern}\nNumber of Cards: {self.cards_num}")

        if self.cards_num == 1:
            s = response.strip("\n").strip()
            if self.korean:
                st = s.strip("\n").strip()
                if "1:" in st:
                    st = st.replace("1:", "1번째 카드:")
                elif "2:" in st:
                    st = st.replace("2:", "2번째 카드:")
                elif "3:" in st:
                    st = st.replace("3:", "3번째 카드:")
            else:
                st = s.strip("\n").strip()
                if "1:" in st:
                    st = st.replace("1:", "1st card:")
                elif "2:" in st:
                    st = st.replace("2:", "2nd card:")
                elif "3:" in st:
                    st = st.replace("3:", "3rd card:")
            self.cards_num_meaning = [st]
        else:
            splitted = response.split("\n\n")
            meanings = []
            for s in splitted:
                if len(s.strip("\n").strip()) < 1:
                    continue
                else:
                    if self.korean:
                        st = s.strip("\n").strip()
                        if "1:" in st:
                            st = st.replace("1:", "1번째 카드:")
                        elif "2:" in st:
                            st = st.replace("2:", "2번째 카드:")
                        elif "3:" in st:
                            st = st.replace("3:", "3번째 카드:")
                    else:
                        st = s.strip("\n").strip()
                        if "1:" in st:
                            st = st.replace("1:", "1st card:")
                        elif "2:" in st:
                            st = st.replace("2:", "2nd card:")
                        elif "3:" in st:
                            st = st.replace("3:", "3rd card:")
                    meanings.append(st)
            self.cards_num_meaning = meanings

    def set_cards(self, picked_cards):
        self.cards = []
        for card in picked_cards:
            self.cards.append({"name": card[0],
                               "korean_name": card[1],
                               "description": card[2],
                               "meaning": "",
                               "interpretation": ""})
            
    def set_mbti(self, mbti):
        self.mbti = mbti.upper()
        if self.korean:
            print(f"MBTI가 {self.mbti}로 설정되었습니다.")
        else:
            print(f"MBTI set to {self.mbti}.")
            
    def set_meaning(self):
        self.set_system_prompt("You will be given a picked card's name. Your job is to explain the general meaning of the picked card shortly in one-line. Remember, only explain the meaning of the card itself, not making any interpretation about it. Only output the general meaning.", disable_positivity=True)
        for cidx, card in enumerate(self.cards):
            if self.korean:
                prompt = f"Picked Card: {card['name']} ({card['korean_name']})"
                response = self.get_response(prompt)
            else:
                prompt = f"Picked Card: {card['name']}"
                response = self.get_response(prompt)
            self.cards[cidx]["meaning"] = response



    def set_meaning_by_idx(self, cidx):
        self.set_system_prompt("You will be given a picked card's name. Your job is to explain the general meaning of the picked card shortly in one-line. Remember, only explain the meaning of the card itself, not making any interpretation about it. Only output the general meaning.", disable_positivity=True)
        if self.korean:
            prompt = f"Picked Card: {self.cards[cidx]['name']} ({self.cards[cidx]['korean_name']}), user's MBTI: {self.mbti}"
            response = self.get_response(prompt, additional_linebreak=True)
        else:
            prompt = f"Picked Card: {self.cards[cidx]['name']}"
            response = self.get_response(prompt, additional_linebreak=True)
        self.cards[cidx]["meaning"] = response

    def set_interpretation(self):
        self.set_system_prompt(f"You will be given \n(1) a user's concern or question on his or her life \n(2) current card's order and high-level meaning \n(3) picked card's name\n(4) general meaning of the picked card\n(5) user's MBTI type as {self.mbti}.\nYour job is to explain the specific interpretation of the picked card, carefully considering the user's concern and high-level meaning and user's MBTI. Remember that your interpretation must be only related to the current card's high-level meaning. For example, when you are interpreting about past information, you must not tell anything about present or future. Do not include greetings in your interpretation. Remember, only make an interpretation of current card. Only output your interpretation on the picked card. Also, make sure you give a brief overview about what the user's MBTI effects on user's characteristics.", disable_positivity=True)
        for cidx, card in enumerate(self.cards):
            if self.korean:
                prompt = f"(1) concern or question: {self.concern}\n(2) high-level meaning: {self.cards_num_meaning[cidx]}\n(3) picked card: {card['name']} ({card['korean_name']})\n(4) general meaning: {card['meaning']}\n(5) user's MBTI type: {self.mbti}"
                response = self.get_response(prompt)
            else:
                prompt = f"(1) concern or question: {self.concern}\n(2) high-level meaning: {self.cards_num_meaning[cidx]}\n(3) picked card: {card['name']}\n(4) general meaning: {card['meaning']}\n(5) user's MBTI type: {self.mbti}"
                response = self.get_response(prompt)
            self.cards[cidx]["interpretation"] = response

    def set_interpretation_by_idx(self, cidx):
        self.set_system_prompt(
            f"You will be given \n(1) a user's concern or question on his or her life \n(2) current card's order and high-level meaning \n(3) picked card's name\n(4) general meaning of the picked card\n(5) user's MBTI type as {self.mbti}\nYour job is to explain the specific interpretation of the picked card, carefully considering the user's concern, high-level meaning, and MBTI type. Remember that your interpretation must be only related to the current card's high-level meaning. For example, when you are interpreting about past information, you must not tell anything about present or future. Only output your interpretation of the current card. Also, make sure you give a brief overview about what the user's MBTI effects on user's characteristics.",
            disable_positivity=True,
        )
        if self.korean:
            prompt = f"(1) concern or question: {self.concern}\n(2) high-level meaning: {self.cards_num_meaning[cidx]}\n(3) picked card: {self.cards[cidx]['name']} ({self.cards[cidx]['korean_name']})\n(4) general meaning: {self.cards[cidx]['meaning']}\n(5) user's MBTI type: {self.mbti}"
            response = self.get_response(prompt)
        else:
            prompt = f"(1) concern or question: {self.concern}\n(2) high-level meaning: {self.cards_num_meaning[cidx]}\n(3) picked card: {self.cards[cidx]['name']}\n(4) general meaning: {self.cards[cidx]['meaning']}\n(5) user's MBTI type: {self.mbti}"
            response = self.get_response(prompt)
        self.cards[cidx]["interpretation"] = response

    def set_interpretation_overall(self):
        self.set_system_prompt(f"You will be given \n(1) a user's concern or question on his or her life \n(2) the interpretation of picked cards \n(3) user's MBTI type as {self.mbti}.\nYour job is to explain the overall interpretation and advise for the user, taking into account their MBTI personality. Only output your interpretation or advice. Also, make sure you give a brief overview about what the user's MBTI effects on user's characteristics.")
        prompt = f"(1) concern or question: {self.concern}\n(3) user's MBTI type: {self.mbti}\n"
        for cidx, card in enumerate(self.cards):
            if self.korean:
                prompt += f"(2-{cidx}) {self.cards_num_meaning[cidx]}\n- picked card: {card['name']} ({card['korean_name']})\n- general meaning: {card['meaning']}\n- interpretation: {card['interpretation']}\n User's MBTI: {self.mbti}\n"
            else:
                prompt += f"(2-{cidx+1}) {self.cards_num_meaning[cidx]}\n- picked card: {card['name']}\n- general meaning: {card['meaning']}\n- interpretation: {card['interpretation']}\n User's MBTI: {self.mbti}\n"
        response = self.get_response(prompt)
        self.interpretation_overall = response

    def money_tarot(self): ##재물
        self.set_system_prompt(f"You will be given \n(1) a user's money luck on his or her life \n(2) current card's order and high-level meaning \n(3) picked card's name\n(4) general meaning of the picked card\n(5) user's MBTI type as {self.mbti}.\nYour job is to explain the specific interpretation of the picked card, carefully considering the user's concern and high-level meaning. Remember that your interpretation must be only related to the current card's high-level meaning. For example, when you are interpreting about past information, you must not tell anything about present or future. Do not include greetings in your interpretation. Remember, only make an interpretation of current card. Only output your interpretation on the picked card.", disable_positivity=True)
        for cidx, card in enumerate(self.cards):
            if self.korean:
                prompt = f"(1) concern or question: {self.concern}\n(2) high-level meaning: {self.cards_num_meaning[cidx]}\n(3) picked card: {card['name']} ({card['korean_name']})\n(4) general meaning: {card['meaning']}\n"
                response = self.get_response(prompt)
            else:
                prompt = f"(1) concern or question: {self.concern}\n(2) high-level meaning: {self.cards_num_meaning[cidx]}\n(3) picked card: {card['name']}\n(4) general meaning: {card['meaning']}\n"
                response = self.get_response(prompt)
            self.cards[cidx]["interpretation"] = response