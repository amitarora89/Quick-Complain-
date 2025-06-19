from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import random

Window.clearcolor = (1, 1, 0, 1)  # Yellow background

def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

def bold_maroon(text):
    return f"[b][color=#800000]{capitalize_words(text)}[/color][/b]"

class ComplaintApp(App):
    def build(self):
        self.user_data = {}
        self.stage = 0

        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.header = Label(
            text=bold_maroon("Quick Complain"),
            font_size=78,
            markup=True,
            size_hint=(1, 0.1),
            halign='center',
            valign='middle'
        )
        self.header.bind(size=self.adjust_label)
        self.root.add_widget(self.header)

        self.message = Label(
            text=bold_maroon("Apki Complaint Register Karne Me Hum Aapki Sahayata Karenge.\nKripya Apna Naam Bataye:"),
            font_size=60,
            markup=True,
            size_hint=(1, 0.3),
            halign='center',
            valign='middle'
        )
        self.message.bind(size=self.adjust_label)
        self.root.add_widget(self.message)

        self.input_area = BoxLayout(orientation='vertical', size_hint=(1, 0.3), spacing=10)

        self.user_input = TextInput(
            hint_text="Apna Naam Likhein...",
            font_size=50,
            size_hint=(1, 0.25),
            multiline=False,
            foreground_color=(0.5, 0, 0, 1),
            background_color=(1, 1, 0.8, 1)
        )

        self.send_button = Button(
            text="Aagey Badhein",
            font_size=62,
            size_hint=(1, 0.25),
            background_color=(1, 0, 0, 1),
            color=(1, 1, 0, 1)
        )
        self.send_button.bind(on_press=self.next_stage)

        self.input_area.add_widget(self.user_input)
        self.input_area.add_widget(self.send_button)
        self.root.add_widget(self.input_area)

        return self.root

    def adjust_label(self, instance, value):
        instance.text_size = instance.size

    def next_stage(self, instance):
        text = self.user_input.text.strip()
        if text == "":
            return

        if self.stage == 0:
            formatted_name = capitalize_words(text) + " Ji"
            self.user_data['Naam'] = formatted_name
            self.message.text = bold_maroon(f"Dhanyawaad {formatted_name}!\nKis Product Me Samasya Hai?")
            self.user_input.hint_text = "Product Ka Naam Likhein..."
            self.stage += 1

        elif self.stage == 1:
            self.user_data['Product'] = capitalize_words(text)
            self.message.text = bold_maroon("Kripya Samasya Ki Thodi Aur Jankari Dein:")
            self.user_input.hint_text = "Samasya Ki Detail Likhein..."
            self.stage += 1

        elif self.stage == 2:
            self.user_data['Details'] = capitalize_words(text)
            self.message.text = bold_maroon(f"{self.user_data['Naam']}, Apna Pata Bataye:")
            self.user_input.hint_text = "Pata Likhein..."
            self.stage += 1

        elif self.stage == 3:
            self.user_data['Address'] = capitalize_words(text)
            self.message.text = bold_maroon("Apna Mobile Number Prastut Kijiye:")
            self.user_input.hint_text = "Phone Number Likhein..."
            self.stage += 1

        elif self.stage == 4:
            self.user_data['Phone'] = text
            summary = (
                bold_maroon("Kripya Jankari Ki Pushti Kijiye:") + "\n\n" +
                bold_maroon("Naam: " + self.user_data['Naam']) + "\n" +
                bold_maroon("Product: " + self.user_data['Product']) + "\n" +
                bold_maroon("Detail: " + self.user_data['Details']) + "\n" +
                bold_maroon("Pata: " + self.user_data['Address']) + "\n" +
                bold_maroon("Phone: " + self.user_data['Phone']) + "\n\n" +
                bold_maroon("Sab Sahi Hai?")
            )
            self.message.text = summary
            self.root.remove_widget(self.input_area)
            self.show_confirmation_buttons()
            self.stage += 1

        self.user_input.text = ""

    def show_confirmation_buttons(self):
        self.confirm_area = BoxLayout(size_hint=(1, 0.2), spacing=10)
        yes_btn = Button(text="Haan", font_size=44, background_color=(0, 0.6, 0, 1), color=(1, 1, 1, 1))
        no_btn = Button(text="Nahi", font_size=44, background_color=(0.6, 0, 0, 1), color=(1, 1, 1, 1))
        yes_btn.bind(on_press=self.finalize_complaint)
        no_btn.bind(on_press=self.reset_all)
        self.confirm_area.add_widget(yes_btn)
        self.confirm_area.add_widget(no_btn)
        self.root.add_widget(self.confirm_area)

    def finalize_complaint(self, instance):
        self.user_data['Complaint No'] = "C" + str(random.randint(1000, 9999))
        msg = bold_maroon(
            f"{self.user_data['Naam']}, Dhanyawaad!\n"
            f"Aapki Complaint Sankhya {self.user_data['Complaint No']} Register Ki Gayi Hai.\n"
            f"Hamara Technician 24-48 Ghante Me Aap Se Sampark Karega.\n\n"
            "Apka Din Shubh Ho! "
        )
        self.message.text = msg
        self.root.remove_widget(self.confirm_area)

    def reset_all(self, instance):
        self.user_data = {}
        self.stage = 0
        self.message.text = bold_maroon("Chaliye Dobara Shuru Karte Hain.\nKripya Apna Naam Bataye:")
        self.user_input.hint_text = "Apna Naam Likhein..."
        if hasattr(self, 'confirm_area') and self.confirm_area.parent:
            self.root.remove_widget(self.confirm_area)
        if self.input_area.parent is None:
            self.root.add_widget(self.input_area)

if __name__ == "__main__":
    ComplaintApp().run()
