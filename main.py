from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from phonenumbers import geocoder
import phonenumbers
from phonenumbers import carrier
class ConverterApp(MDApp):

    def press(self, args):


        ivedimas = self.input.text

        try:
            ch_number = phonenumbers.parse(ivedimas, "CH")
            #print(geocoder.description_for_number(ch_number, "en"))


            self.valstybe.text = geocoder.description_for_number(ch_number, "en")

            service_number = phonenumbers.parse(ivedimas, "RO")
            if carrier.name_for_number(service_number, "en") == "BITÄ":
                self.tiekejas.text = "BITĖ"
            else:
                self.tiekejas.text = carrier.name_for_number(service_number, "en")







        except:
            self.valstybe.text = "This is not a number"
            self.tiekejas.text = "Try again"






    def build(self):
        self.state = 0
        self.theme_cls.primary_palette = "Teal"
        screen = MDScreen()
        self.icon = "logo1.png"
        self.toolbar = MDToolbar(title="Phone number information", size_hint=(1,1))
        self.toolbar.pos_hint = {"top": 1}

        screen.add_widget(self.toolbar)
        screen.add_widget(Image(
            source="logo.png",
            pos_hint = {"center_x": 0.5, "center_y": 0.7},
            size_hint= (0.6,0.6)


        ))
        self.input = MDTextField(
            hint_text="Type here",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y": 0.45},
            font_size = 22,



        )
        self.label = MDLabel(
            text="Enter a phone number:",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            theme_text_color = "Secondary",

            
        )

        self.valstybe= MDLabel(

            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            theme_text_color="Primary",
            font_style = "H5",
            size_hint=(1,1)
        )

        self.tiekejas = MDLabel(

            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            theme_text_color="Primary",
            font_style="H5",
            size_hint=(1,1)
        )

        screen.add_widget(self.input)
        #screen.add_widget(self.label)
        screen.add_widget(self.valstybe)
        screen.add_widget(self.tiekejas)
        screen.add_widget(MDFillRoundFlatButton(
            text="SUBMIT",
            font_size = 17,
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            on_press = self.press,
            size_hint=(0.05,0.05)

        ))
        return screen

if __name__ == '__main__':
    ConverterApp().run()
