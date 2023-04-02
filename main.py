from typing import Union
from kivy.config import Config
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker, MDDatePicker, MDColorPicker

Config.set('graphics', 'Resizable', '0')
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('time.kv')

    def get_time(self, instance, time):
        self.root.ids.time_label.text = str(time)

    def on_cancel(self, instance, time):
        self.root.ids.time_label.text = "You Clicked Cancel!"

    def show_time_picker(self):
        from datetime import datetime

        # Define default time
        default_time = datetime.strptime("4:20:00", '%H:%M:%S').time()

        time_dialog = MDTimePicker()
        # Set default Time
        time_dialog.set_time(default_time)
        time_dialog.bind(on_cancel=self.on_cancel, time=self.get_time)
        time_dialog.open()

    def on_save(self, instance, value, date_range):
         self.root.ids.date_label.text = str(value)

    def on_cancel_date(self, instance, value):
        self.root.ids.date_label.text = "Вы закрыли выбор даты!"

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel_date)
        date_dialog.open()

    def open_color_picker(self):
        color_picker = MDColorPicker(size_hint=(0.45, 0.85))
        color_picker.open()
        color_picker.bind(
            on_select_color=self.on_select_color,
            on_release=self.get_selected_color,
        )

    def update_color(self, color: list) -> None:
        self.root.ids.toolbar.md_bg_color = color

    def get_selected_color(
        self,
        instance_color_picker: MDColorPicker,
        type_color: str,
        selected_color: Union[list, str],
    ):
        print(f"Selected color is {selected_color}")
        self.update_color(selected_color[:-1] + [1])

    def on_select_color(self, instance_gradient_tab, color: list) -> None:
        '''Called when a gradient image is clicked.'''


if __name__ == '__main__':
    MainApp().run()