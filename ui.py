import toga
from toga.style.pack import COLUMN, Pack,ROW

class LoginForm():
    def __init__(self):
        self.username_text = None
        self.password_text = None
        self.box  = None

    def button_handler(self,widget):
        print( self.username_text.value +" : "+self.password_text.value)


    def build(self,app):
        box = toga.Box()
        left_container = toga.Box( style=Pack( direction=COLUMN, padding_top=20))
        right_container = toga.Box(style=Pack(direction=COLUMN, padding_top=20))
        login_label = toga.Label('Username')
        login_label.style.update( width=100, padding= 5, flex=1)
        username_text = toga.TextInput()

        username_text.style.padding = 5
        self.username_text = username_text
        password_label = toga.Label('Password')
        password_label.style.update( width=100, padding=5, flex=1)
        password_text = toga.PasswordInput()
        password_text.style.padding = 5
        self.password_text = password_text
        button = toga.Button('LOGIN', on_press=self.button_handler)

        button.style.update( width=200, padding=5)

        left_container.add( login_label)
        left_container.add( password_label)
        right_container.add( username_text)
        right_container.add( password_text)

        box.add( left_container)
        box.add( right_container)
        right_container.add(button)
        self.box = box

        return box


class LoginWindow(toga.App):
    def _create_impl(self):
        factory_app = self.factory.App
        factory_app.create_menus = lambda _: None
        return factory_app(interface=self)

    def __init__(
            self,
            formal_name=None,
            app_id=None,
            app_name=None,
            id=None,
            icon=None,
            author=None,
            version=None,
            home_page=None,
            description=None,
            startup=None,
            on_exit=None,
            factory=None,
    ):
        super().__init__(formal_name=formal_name,app_id=app_id,app_name=app_name, id=id,icon=icon,author=author,version=version,home_page=home_page,description=description,
                       startup=startup,on_exit = on_exit, factory=factory)
        box = toga.Box()
        left_container = toga.Box(style=Pack(direction=COLUMN, padding_top=20))
        right_container = toga.Box(style=Pack(direction=COLUMN, padding_top=20))
        login_label = toga.Label('Username')
        login_label.style.update(width=100, padding=5, flex=1)
        username_text = toga.TextInput()

        username_text.style.padding = 5
        self.username_text = username_text
        password_label = toga.Label('Password')
        password_label.style.update(width=100, padding=5, flex=1)
        password_text = toga.PasswordInput()
        password_text.style.padding = 5
        self.password_text = password_text
        button = toga.Button('LOGIN', on_press=self.button_handler)

        button.style.update(width=200, padding=5)

        left_container.add(login_label)
        left_container.add(password_label)
        right_container.add(username_text)
        right_container.add(password_text)

        box.add(left_container)
        box.add(right_container)
        right_container.add(button)
        self.box = box
    def button_handler(self,widget):
        print( self.username_text.value +" : "+self.password_text.value)

    def startup(self):
        print(super().main_window)
def main():
    return LoginWindow('Facebook Management Tool', 'org.beeware.helloworld')


if __name__ == '__main__':
    main().main_loop()
