from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.screen_manager = BoxLayout()
        self.tela_login = TelaLogin(manager=self.screen_manager)
        self.tela_cadastro = TelaCadastro(manager=self.screen_manager)
        self.screen_manager.add_widget(self.tela_login)
        layout.add_widget(self.screen_manager)
        return layout

class TelaLogin(BoxLayout):
    def __init__(self, manager, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.manager = manager
        button_login = Button(text='Login', size_hint_y=None, height=50, on_press=self.login)
        button_register = Button(text='Registrar', size_hint_y=None, height=50, on_press=self.registrar)
        self.add_widget(button_login)
        self.add_widget(button_register)

    def login(self, *args):
        print("Implemente a lógica de login aqui")

    def registrar(self, *args):
        self.manager.clear_widgets()
        self.manager.add_widget(TelaCadastro(manager=self.manager))

class TelaCadastro(BoxLayout):
    def __init__(self, manager, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.manager = manager
        button_register = Button(text='Cadastrar', size_hint_y=None, height=50, on_press=self.cadastrar)
        button_back = Button(text='Voltar', size_hint_y=None, height=50, on_press=self.voltar)
        self.add_widget(button_register)
        self.add_widget(button_back)

    def cadastrar(self, *args):
        print("Implemente a lógica de cadastro aqui")
        self.manager.clear_widgets()
        self.manager.add_widget(TelaLogin(manager=self.manager))

    def voltar(self, *args):
        self.manager.clear_widgets()
        self.manager.add_widget(TelaLogin(manager=self.manager))

if __name__ == '__main__':
    TestApp().run()
