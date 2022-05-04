from time import sleep
from kivy.lang import Builder
from kivymd.app import MDApp
from threading import Thread
from random import choice

screen_h = """
MDBoxLayout:
    orientation: "vertical"
    spacing: "10dp"
    padding: "20dp"
    md_bg_color: 0.1,0.1,0.1,1
    MDBoxLayout:
        orientation: "vertical"
        padding: "50dp"
        md_bg_color: 0,1,0,1
        spacing: "40dp"
        MDLabel:
            id: yttwo
            text: ""
            halign: "center"
            font_size: "30dp"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
        MDRectangleFlatButton:
            id: spinbtnone
            disabled: True
            text: "nipS"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            line_color: 0,0,0,1
            font_size: "50dp"
            pos_hint: {"center_x":0.50}
            on_release: app.spining_thread()
            font_name: app.font_style
    MDBoxLayout:
        orientation: "vertical"
        padding: "50dp"
        md_bg_color: 0.1,0.1,0.1,1
        spacing: "10dp"
        MDLabel:
            id: tdnn
            text: ""
            halign: "center"
            font_size: "60dp"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            font_name: app.font_style
        MDLabel:
            id: tdn
            text: "Welcome"
            halign: "center"
            font_size: "60dp"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
    MDBoxLayout:
        orientation: "vertical"
        padding: "50dp"
        md_bg_color: 0,0,1,1
        spacing: "40dp"
        MDRectangleFlatButton:
            id: spinbtntwo
            text: "Spin"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            line_color: 0,0,0,1
            font_size: "50dp"
            pos_hint: {"center_x":0.50}
            on_release: app.spining_thread()
        MDLabel:
            id: ytone
            text: "Your turn"
            halign: "center"
            font_size: "30dp"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
"""

class TruthDare(MDApp):
    def build(self):
        screen_elements = Builder.load_string(screen_h)
        return screen_elements

    def spining_thread(self):
        Thread(target=self.spining).start()

    choice_list = ["Truth","Dare","Nothing","Truth","Dare","Nothing","Truth","Dare","Nothing","Truth","Dare","Nothing"]
    turn = "green"
    font_style = "f.ttf"
    def spining(self):
        for i in range(10):
            self.root.ids.tdn.text = self.choice_list[i]
            self.root.ids.tdnn.text = self.choice_list[i][len(self.choice_list[i])::-1]
            sleep(0.10)
        c = choice(self.choice_list)
        self.root.ids.tdn.text = c
        self.root.ids.tdnn.text = c[len(c)::-1]
        self.root.ids.yttwo.font_name = self.font_style
        if self.turn == "green":
            self.root.ids.yttwo.text = "nruT ruoY"
            self.root.ids.ytone.text = ""
            self.root.ids.spinbtntwo.disabled = True
            self.root.ids.spinbtnone.disabled = False
            self.turn = "blue"
        elif self.turn == "blue":
            self.root.ids.yttwo.text = ""
            self.root.ids.ytone.text = "Your Turn"
            self.root.ids.spinbtntwo.disabled = False
            self.root.ids.spinbtnone.disabled = True
            self.turn = "green"

if __name__ == "__main__":
    TruthDare().run()