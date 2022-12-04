import customtkinter
import time
from difflib import SequenceMatcher

import speech_recognition as sr

# Record Audio
r = sr.Recognizer()
m = sr.Microphone()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Speech recognition using Google Speech Recognition
def checkspeech():
    global r
    global entry
    global score
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        string1 = entry.get().replace(" ", "")
        string2 = str(r.recognize_google(audio, language='en-EN')).replace(" ", "")
        scorenumber = float("{:.2f}".format(similar(string1, string2) * 100))
        score.configure(text="ความแม่นยำ : "+str(scorenumber)+"%")
        window1.destroy()
        return ()
    except sr.UnknownValueError:
        window1.destroy()
        return ()

current_lang = ""
entry = ""
score = ""
window1 = ""
class FullApp(customtkinter.CTk):
    def __init__(self):
        global score

        super().__init__()

        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        self.geometry("800x600")
        self.title("Accents Checker")

        #Text
        title = customtkinter.CTkLabel(master=self, text="Accents Checker", text_font=("TH SarabunPSK",30))
        title.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
        title2 = customtkinter.CTkLabel(master=self, text="สร้างโดย จรณะ สุขโรจน์", text_font=("TH SarabunPSK",28))
        title2.place(relx=0.5, rely=0.26, anchor=customtkinter.CENTER)
        title3 = customtkinter.CTkLabel(master=self, text="คำศัพท์ไม่ควรมีตัวใหญ่ตัวเล็ก และควรมีแค่ตัวอักษรหรือตัวเลข และไม่ควรย่อคำ", text_font=("TH SarabunPSK",18), text_color=("#ff2323"))
        title3.place(relx=0.5, rely=0.33, anchor=customtkinter.CENTER)
        score = customtkinter.CTkLabel(master=self, text="ความแม่นยำ : 0%", text_font=("TH SarabunPSK",20), text_color=("#ff9900"))
        score.place(relx=0.5, rely=0.41, anchor=customtkinter.CENTER)

        # Use CTkButton instead of tkinter Button
        button = customtkinter.CTkButton(master=self, text="เริ่มต้น", command=self.create_main1)
        button.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        #Language Choose
        optionmenu_var = customtkinter.StringVar(value="ภาษา")  # set initial value

        def optionmenu_callback(choice):
            global current_lang
            current_lang = choice

        combobox = customtkinter.CTkComboBox(master=self,
                                            values=["en_US"],
                                            command=optionmenu_callback,
                                            variable=optionmenu_var)
        combobox.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        #Create Word box
        global entry
        entry = customtkinter.CTkEntry(master=self,
                               placeholder_text="คำศัพท์ที่ต้องการตรวจสอบ",
                               width=200,
                               height=25,
                               border_width=2,
                               corner_radius=10)
        entry.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
    def create_main1(self):
        global window1
        global entry
        if (current_lang == ""):
            window = customtkinter.CTkToplevel(self)
            window.geometry("400x200")
            window.title("คำเตือน")

            label = customtkinter.CTkLabel(window, text="กรุณาเลือกภาษาก่อน", text_font=("TH SarabunPSK",24))
            label.pack(side="top", fill="both", expand=True, padx=50, pady=50)
            return
        elif (entry.get() == ""):
            window = customtkinter.CTkToplevel(self)
            window.geometry("400x200")
            window.title("คำเตือน")

            label = customtkinter.CTkLabel(window, text="กรุณากรอกคำศัพท์ที่ต้องการตรวจสอบ", text_font=("TH SarabunPSK",18))
            label.pack(side="top", fill="both", expand=True, padx=50, pady=50)
            return
        window1 = customtkinter.CTkToplevel(self)
        window1.geometry("400x200")
        window1.title("หน้าต่างทำการ")
        label = customtkinter.CTkLabel(window1, text="คุณควรรอสัก 1 วินาทีแล้วจึงเริ่มพูดหลังจากกดปุ่ม", text_color=("#ff2323"), text_font=("TH SarabunPSK",15))
        label.pack(side="top", fill="both", expand=True, padx=50, pady=5)
        button = customtkinter.CTkButton(master=window1,
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=8,
                                        text="คลิกเพื่อเริ่มพูด",
                                        command=checkspeech)
        button.pack(side="top", fill="both", expand=True, padx=50, pady=50)
        return

app = FullApp()
app.mainloop()