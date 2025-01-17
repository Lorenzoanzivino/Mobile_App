
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class SommaApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # bianco (R, G, B, A)
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8, 0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.4}
        Window.size = (360, 640)
        
        self.window.add_widget(Image(source="soldi.png"))
        
        self.input_testo = TextInput(
            size_hint =(1, 0.2),
            font_size = '20sp',
            padding = (10, 12),
            halign = 'center'
            )
        self.window.add_widget(self.input_testo)
        
        self.bottone = Button(
            text="CALCOLA!",
            size_hint = (1, 0.2),
            bold = True,
            background_color = '#0099ff'
            )
        self.window.add_widget(self.bottone)
        self.bottone.bind(on_press = self.calcola_somma)
        
        self.etichetta = Label(
            text="Inserisci un numero intero...",
            font_size = '18sp',
            color = '#007dd1',
            halign ='center',
            valign='middle',
            )
        self.window.add_widget(self.etichetta)
        

        return self.window

    def calcola_somma(self, instance):
        try:
            # Ottieni il numero inserito dall'utente
            N1 = int(self.input_testo.text)
            
            # Calcola la somma dei numeri da 1 a N1
            somma1 = (N1 * (N1 + 1)) // 2
            self.etichetta.text = f"La somma dei numeri da 1 a {N1} è:\n{somma1}"
        
        except ValueError:
            self.etichetta.text = "Errore: Devi inserire un numero intero. Riprova."

# Esegui l'app
if __name__ == "__main__":
    SommaApp().run()