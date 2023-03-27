import kivymd.uix.pickers
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker, MDDatePicker, MDColorPicker


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('time.kv')

    # Get Time
    def get_time(self, instance, time):
        self.root.ids.time_label.text = str(time)

    # Cancel
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

    def on_cancel(self, instance, value):
        self.root.ids.date_label.text = "Вы закрыли выбор даты!"

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def show_theme_picker(self):
        theme_dialog = MDColorPicker()
        theme_dialog.open()

MainApp().run()