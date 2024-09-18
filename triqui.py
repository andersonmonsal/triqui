import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

kivy.require('2.0.0')

class TriquiApp(App):
    def build(self):
        self.title = "Triqui"
        self.grid = GridLayout(cols=3)
        self.buttons = [Button(text='', font_size=40) for _ in range(9)]
        self.current_player = 'X'
        self.game_over = False

        for button in self.buttons:
            button.bind(on_press=self.on_button_press)
            self.grid.add_widget(button)

        return self.grid

    def on_button_press(self, button):
        if button.text == '' and not self.game_over:
            button.text = self.current_player
            if self.check_winner():
                self.show_winner(self.current_player)
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columnas
            [0, 4, 8], [2, 4, 6]              # diagonales
        ]
        for combo in winning_combinations:
            if (self.buttons[combo[0]].text == self.buttons[combo[1]].text == self.buttons[combo[2]].text) and (self.buttons[combo[0]].text != ''):
                self.game_over = True
                return True
        return False

    def show_winner(self, winner):
        popup = Popup(title='¡Ganador!', content=Label(text=f'Jugador {winner} ha ganado!'), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    TriquiApp().run()
