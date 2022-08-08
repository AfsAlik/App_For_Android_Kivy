from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.graphics import *
from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
from datetime import datetime

import requests
from bs4 import BeautifulSoup as BS
from prettytable import PrettyTable

import smtplib
from email.mime.text import MIMEText
from kivy.clock import Clock


data = dict()

class Nastroiki(Screen):
    def switch(self, switchObject, switchValue):
        if (switchValue):
            f = open('E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val3.txt', "w", encoding="utf-8")
            f.write("1")
            f.close()
            with self.canvas.before:
                Rectangle(source = "Img\\bg.png", size = self.size)
        else:
            f = open('E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val3.txt', "w", encoding="utf-8")
            f.write("0")
            f.close()
            with self.canvas.before:
                Rectangle(source = "Img\\Main_theme.jpg", size = self.size)


class Istor(Screen):
    def on_enter(self, **kwargs):
        d = open('E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\URLadresa.txt', "r", encoding='utf-8')
        self.ids.url.text = d.read()
        d.close()
        f = open('E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val3.txt', "r", encoding='utf-8')
        a = f.read()
        f.close()
        if a == "1":
            with self.canvas.before:
                Rectangle(source = "Img\\bg.png", size = self.size)
        elif a == "0":
            with self.canvas.before:
                Rectangle(source = "Img\\Main_theme.jpg", size = self.size)

class Parsing(Screen):
    def on_enter(self, **kawrgs):
        f = open('E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val3.txt', "r", encoding='utf-8')
        a = f.read()
        f.close()
        if a == "1":
            with self.canvas.before:
                Rectangle(source = "Img\\bg.png", size = self.size)
        elif a == "0":
            with self.canvas.before:
                Rectangle(source = "Img\\Main_theme.jpg", size = self.size)
                
    def clear(self):
        f = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\Vivod.txt", "w", encoding='utf-8')
        f.write("")
        f.close()
    
    def val2(self, value):
        match value:
            case "Файл":
                f = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val2.txt", "w", encoding='utf-8')
                f.write("0")
                f.close()
            case "На экран":
                f = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val2.txt", "w", encoding='utf-8')
                f.write("1")
                f.close()
   
    def val1(self, value):
        match value:
            case "Смартфоны":
                f = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("smartfony")
                f.close()
            case "Ноутбуки":
                f = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("noutbuki")
                f.close()
            case "Телевизоры":
                f = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("televizory")
                f.close()
            case "Повер банки":
                f = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("power-bank")
                f.close()
            case "Экшн камеры":
                f = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("ekshn-kamery")
                f.close()
            case "Автокресла":
                f = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("avtokresla")
                f.close()
            case "Экшн камеры":
                f = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("ekshn-kamery")
                f.close()
            case "Смарт-часы":
                f = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("smart-chasy")
                f.close()
            case "Компьютеры":
                f = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("kompyutery")
                f.close()
            case "Моноблоки":
                f = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("monobloki")
                f.close()
            case "Игровые компьютеры":
                f = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("kompyutery--igrovyie-comp")
                f.close()

    def sohrURL(self):
        f = open('E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\URLadresa.txt', "a", encoding='utf-8')
        f.write(self.ids.tx1.text + "\n")
        f.close()
        
    def bar2(self):
        self.bar = Clock.schedule_interval(self.bar1, 0.005)
        Clock.schedule_once(self.stop_interval, 1.637)
        
    def stop_interval(self, *args):
        self.bar.cancel()
    
    def bar1(self, *args):
        current = self.ids.bar.value
        if current == 1:
            current = 0
            self.main()
        current += .01
        self.ids.bar.value = current

    data = dict()

    def parse(self, html):

        self.html = BS(html.text, features="html.parser")

        self.group = self.html\
            .find('div', class_="MainWrapper")\
            .find('div', class_="ProductCardCategoryList__list")

        self.tov=[]
        self.cen=[]
        self.val=[]


        # with alive_bar(100, bar='blocks') as bar:
        #         for self.i in range (100):
        #             time.sleep(.05)
        #             bar()

        for self.m1 in self.group.find_all('div', class_="product_data__gtm-js")[0:]:

            self.m2 = self.m1.find('div', class_="ProductCardHorizontal__header-block")
            self.m3 = self.m2.find('a').text.strip()

            # tov.append(m3)

            self.m4 = self.m1.find('div', class_="ProductCardHorizontal__buy-block")
            self.m5 = self.m4.find('span', class_="ProductCardHorizontal__price_current-price").text.strip()

            # cen.append(m5)

            self.m6 = self.m4.find('span', class_="ProductPrice__rouble").text.strip()

            # val.append(m6) 

            # Определяем шапку и данные.
            self.th = ['Товар','Цена','Валюта']
            self.td = [self.m3,self.m5,self.m6]

            self.columns = len(self.th)  # Подсчитаем кол-во столбцов на будущее.

            self.table = PrettyTable(self.th)  # Определяем таблицу.

            # Cкопируем список td, на случай если он будет использоваться в коде дальше.
            # td_data = td[:]
            # Входим в цикл который заполняет нашу таблицу.
                # Цикл будет выполняться до тех пор пока у нас не кончатся данные
                # для заполнения строк таблицы (список td_data).

            while self.td:
                    # Используя срез добавляем первые пять элементов в строку.
                    # (columns = 5).
                self.table.add_row(self.td[:self.columns])
                    # Используя срез переопределяем td_data так, чтобы он
                    # больше не содержал первых 5 элементов.
                self.td = self.td[self.columns:]
            
            # print(self.table)  # Печатаем таблицу

            with open('E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\Vivod.txt', "a", encoding="utf-8") as fp:
                # создаем строку для записи в файл
                self.table = self.table.get_string()
                # пишем данные
                fp.write(self.table)
                # дописываем символ начала строки 
                fp.write('\n')
                fp.close()

            d = open('E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val2.txt', "r", encoding='utf-8')
            s = d.read()
            if s == "1":
                d = open('E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\Vivod.txt', "r", encoding='utf-8')
                a = d.read()
                self.ids['VivodPars'].text = a
                d.close()
                

        return self.data

    def print_pretty_table(data, self, cell_sep=' | ', header_separator=True):
        self.rows = len(data)
        self.cols = len(data[0])

        self.col_width = []
        for self.col in range(self.cols):
            self.columns = [self.data[self.row][self.col] for self.row in range(self.rows)]
            self.col_width.append(len(max(self.columns, key=len)))

        self.separator = "-+-".join('-' * n for n in self.col_width)

        self.lines = []

        for self.i, self.row in enumerate(range(self.rows)):
            if self.i == 1 and header_separator:
                self.lines.append(self.separator)

            self.result = []
            for self.col in range(self.cols):
                self.item = self.data[self.row][self.col].rjust(self.col_width[self.col])
                self.result.append(self.item)

            self.lines.append(cell_sep.join(self.result))

        return '\n'.join(self.lines)

    def main(self):
        f = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "r", encoding='utf-8')
        b = f.read()
        f.close()
        if self.ids.tx1.text == "www.citilink.ru":
            url = 'https://www.citilink.ru/catalog/'+ b +'/?view_type=list&f=discount.any,rating.any'
            self.page = requests.get(url)
            self.parse(self.page)
        else:
            invalidSerc()
            
class Rassilka(Screen):
    def on_enter(self, **kawrgs):
        f = open('E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val3.txt', "r", encoding='utf-8')
        a = f.read()
        f.close()
        if a == "1":
            with self.canvas.before:
                Rectangle(source = "Img\\bg.png", size = self.size)
        elif a == "0":
            with self.canvas.before:
                Rectangle(source = "Img\\Main_theme.jpg", size = self.size)
                
    def on_save(self, instance, value, date_range):
        self.ids['date_label'].text = f'c {str(date_range[0])} по {str(date_range[-1])}'

    def on_cancel(self, instance, value):
        self.ids['date_label'].text = "Вы не выбрали дату!"

    def show_date_picker(self):
        date_dialog = MDDatePicker(mode="range")
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def get_time(self, instance, time):
        self.ids['time_label'].text = str(time)

    def on_cancel2(self, instance, time):
        self.ids['time_label'].text = "Вы не выбрали время!"

    def show_time_picker(self):
        default_time = datetime.strptime("12:00:00", '%H:%M:%S').time()
        time_dialog = MDTimePicker()
        time_dialog.set_time(default_time)
        time_dialog.bind(on_cancel=self.on_cancel2, time=self.get_time)
        time_dialog.open()

    def send_email(self):
        try:
            email = 'AnyFind@yandex.ru'
            password = 'PrilANYFIND'

            server = smtplib.SMTP('smtp.yandex.ru', 587)
            server.ehlo()
            server.starttls()
            server.login(email, password)

            dest_email = self.ids['rassil_poluch'].text
            email_text = self.ids['rassil'].text

            msg = MIMEText(email_text)
            msg["Subject"] = "Приложение - парсер AnyFind"
            
            server.set_debuglevel(1)
            server.sendmail(email, dest_email, msg.as_string())
            server.quit()

            return MailSend()
        except Exception:
            return MailSendInv()

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def on_enter(self, **kwargs):
        d = open("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\URLadresa.txt", "w", encoding="utf-8")
        d.write("")
        d.close()

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    # created = ObjectProperty(None)
    # email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"
    
    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = name
        # self.email.text = self.current
        # self.created.text = created
        f = open('E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\val3.txt', "r", encoding='utf-8')
        a = f.read()
        f.close()
        if a == "1":
            with self.canvas.before:
                Rectangle(source = "Img\\bg.png", size = self.size)
        elif a == "0":
            with self.canvas.before:
                Rectangle(source = "Img\\Main_theme.jpg", size = self.size)

class WindowManager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title='Такого аккаунта нет',
                  content=Label(text='Пожалуйста, проверьте данные'),
                  size_hint=(None, None), size=(300, 200))
    pop.open()


def invalidForm():
    pop = Popup(title='Ошибка',
                  content=Label(text='   Пожалуйста, заполните все поля\nили проверьте корректность формы'),
                  size_hint=(None, None), size=(300, 200))

    pop.open()
    
def invalidSerc():
    pop = Popup(title='Ошибка',
                  content=Label(text=' Введите коректный адресс\nТакой адресс не доступен'),
                  size_hint=(None, None), size=(300, 200))

    pop.open()

def MailSend():
    pop = Popup(title='Уведомление',
                  content=Label(text='Уведомление успешно отправлено!'),
                  size_hint=(None, None), size=(300, 200))
    pop.open()

def MailSendInv():
    pop = Popup(title='Ошибка отправки уведомления',
                  content=Label(text='Проверьте правильность почты'),
                  size_hint=(None, None), size=(300, 200))
    pop.open()

class MyMainApp(MDApp):
    
    def build(self):
        self.title = 'Приложение "AnyFind"'
        return sm

kv = Builder.load_file("my.kv")
sm = WindowManager()
db = DataBase("E:\\Ucheba\\Pril\\Parseeer\\UserRegistration_Kivy-main\\users.txt")
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),Nastroiki(name="nast"),Rassilka(name="rass"),Parsing(name="pars"),Istor(name="ist")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

if __name__ == "__main__":
    MyMainApp().run()