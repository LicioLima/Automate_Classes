import pyautogui as pa
import time

pa.PAUSE = 1

pa.press('win')
pa.write("chrome")
pa.press('enter')
pa.write("https://moodle.ifrs.edu.br/login/index.php")
pa.press('enter')
pa.press('enter', 'btn btn-primary btn-block mt-3')