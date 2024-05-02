#02/05/2024
#@PLima
#aprendendo custom tkinter

import customtkinter as ctk
import pyautogui




#============================================================ EXECUCAO ============================================================
if __name__ == "__main__":
    try:
        print("\n============================== inicio ========================\n")
    except Exception as err:
        print(f"Erro Inexperado: {err=}, \n{type(err)=}")
        pyautogui.alert(f"Erro Inexperado: {err=}, \n{type(err)=}")

