#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import qrcode
from qrcode import main
import qrcode.image.svg
import os
import sys
# from qrcode.image.pure import PymagingImage
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import PIL
from PIL import ImageTk
from PIL import Image

from platform import system
import tkinter as tk

platformD = system()
if platformD == 'Darwin':
    logo_image = 'icones/cs_icon.icns'
elif platformD == 'Windows':
    logo_image = 'icones/cs_icon_win.ico'
else:
    logo_image = 'icones/cs_icon_png.xbm'


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Calibri", "11")
        self.fonteNegrito = ("Calibri", "12", "bold")
        self.fonteAviso = ("Arial", "12", "bold")

        # Adiciona 1 imagem
        # If the code is frozen, use this path:
        if getattr(sys, 'frozen', False):
            self.diretorio_programa = sys._MEIPASS
            print('Caminho diretório Frozen:', self.diretorio_programa)
            print(os.path.join(self.diretorio_programa, "/logo/logo.png"))
        # If it's not use the path we're on now
        else:
            self.diretorio_programa = os.path.dirname(__file__)
            print('Path Root Directory:', self.diretorio_programa)

        # Adiciona 1 imagem - Logo Programa
        self.my_img = ImageTk.PhotoImage(file=(self.diretorio_programa + "/logo/logo.png"))
        self.minha_imagem = Label(image=self.my_img)
        self.minha_imagem.pack()

        # Frame1 - URL
        self.container1 = Frame(main_window)
        self.container1.pack()

        # Frame2 - Matriz e Cores
        self.container2 = Frame(main_window)
        self.container2.pack()

        # Frame3 Imagem Central
        self.container3 = Frame(main_window)
        self.container3.pack()

        # Frame 4 Destino
        self.container4 = Frame(main_window)
        self.container4.pack()

        # Frame5 - Botoes finais
        self.container5 = Frame(main_window)
        self.container5.pack()

        # Frame6 - Versão
        self.container6 = Frame(main_window)
        self.container6.pack()

        # Labels
        self.label1 = Label(self.container1)
        self.label1["text"] = "URL:"
        self.label1.pack(side=LEFT)
        self.label1["font"] = self.fonteNegrito

        self.label1 = Label(self.container2)
        self.label1["text"] = "Matrix(px):"
        self.label1.pack(side=LEFT)
        self.label1["font"] = self.fonteNegrito

        self.tamanhoqr = Entry(self.container2)
        self.tamanhoqr["width"] = 2
        self.tamanhoqr["borderwidth"] = 3
        self.tamanhoqr.pack(side=LEFT)
        self.tamanhoqr["font"] = self.fontePadrao
        self.tamanhoqr.insert(0, "20")

        self.tipoqr = Label(self.container2)
        self.tipoqr["text"] = "PNG with Degrade:"
        self.tipoqr.pack(side=LEFT)
        self.tipoqr["font"] = self.fonteNegrito

        self.imgcenter = Label(self.container3)
        self.imgcenter["text"] = "PNG with Central Image(Optional):"
        self.imgcenter.pack(side=LEFT)
        self.imgcenter["font"] = self.fonteNegrito

        # Cor Externa RGB
        self.color3 = Label(self.container2)
        self.color3["text"] = "External Color"
        self.color3.pack(side=LEFT)
        self.color3["font"] = self.fontePadrao

        self.colorextb = Entry(self.container2)
        self.colorextb["width"] = 3
        self.colorextb["borderwidth"] = 2
        self.colorextb.pack(side=LEFT)
        self.colorextb["font"] = self.fontePadrao
        self.colorextb.insert(0, "125")

        self.colorextg = Entry(self.container2)
        self.colorextg["width"] = 3
        self.colorextg["borderwidth"] = 2
        self.colorextg.pack(side=LEFT)
        self.colorextg["font"] = self.fontePadrao
        self.colorextg.insert(0, "125")

        self.colorextr = Entry(self.container2)
        self.colorextr["width"] = 3
        self.colorextr["borderwidth"] = 2
        self.colorextr.pack(side=LEFT)
        self.colorextr["font"] = self.fontePadrao
        self.colorextr.insert(0, "255")

        def _from_rgb_ext(rgb):
            # Converte o RGB para HEXADECIMAL DO TKINTER
            r, g, b = rgb
            return f'#{r:02x}{g:02x}{b:02x}'

        self.boxcolor_ext = Label(self.container2)
        self.boxcolor_ext["text"] = ""
        self.boxcolor_ext["bg"] = _from_rgb_ext((int(self.colorextr.get()),
                                                 int(self.colorextg.get()), int(self.colorextb.get())))
        self.boxcolor_ext.pack(side=LEFT)
        self.boxcolor_ext["font"] = self.fontePadrao

        # Cor Interna RGB

        self.color = Label(self.container2)
        self.color["text"] = "Internal Color"
        self.color.pack(side=LEFT)
        self.color["font"] = self.fontePadrao

        self.colorintb = Entry(self.container2)
        self.colorintb["width"] = 3
        self.colorintb["borderwidth"] = 2
        self.colorintb.pack(side=LEFT)
        self.colorintb["font"] = self.fontePadrao
        self.colorintb.insert(0, "255")

        self.colorintg = Entry(self.container2)
        self.colorintg["width"] = 3
        self.colorintg["borderwidth"] = 2
        self.colorintg.pack(side=LEFT)
        self.colorintg["font"] = self.fontePadrao
        self.colorintg.insert(0, "125")

        self.colorintr = Entry(self.container2)
        self.colorintr["width"] = 3
        self.colorintr["borderwidth"] = 2
        self.colorintr.pack(side=LEFT)
        self.colorintr["font"] = self.fontePadrao
        self.colorintr.insert(0, "125")

        def _from_rgb_int(rgb):
            # Converte o RGB para HEXADECIMAL DO TKINTER
            r, g, b = rgb
            return f'#{r:02x}{g:02x}{b:02x}'

        self.boxcolor_int = Label(self.container2)
        self.boxcolor_int["text"] = ""
        self.boxcolor_int["bg"] = _from_rgb_int((int(self.colorintr.get()),
                                                 int(self.colorintg.get()), int(self.colorintb.get())))
        self.boxcolor_int.pack(side=LEFT)
        self.boxcolor_int["font"] = self.fontePadrao

        def refresh_colors():
            self.boxcolor_int["bg"] = _from_rgb_int((int(self.colorintr.get()),
                                                     int(self.colorintg.get()), int(self.colorintb.get())))
            self.boxcolor_ext["bg"] = _from_rgb_ext((int(self.colorextr.get()),
                                                     int(self.colorextg.get()), int(self.colorextb.get())))

        # Button Refresh Colors
        self.bot_refresh = Button(self.container2)
        self.bot_refresh["text"] = "Refresh"
        self.bot_refresh["command"] = refresh_colors
        self.bot_refresh.pack(side=RIGHT)
        self.bot_refresh["font"] = self.fonteNegrito

        # Entrada de texto
        self.img = Entry(self.container3)
        self.img["width"] = 42
        self.img["borderwidth"] = 3
        self.img.pack(side=LEFT)
        self.img["font"] = self.fontePadrao

        self.label2 = Label(self.container4)
        self.label2["text"] = "Where save:"
        self.label2.pack(side=LEFT)
        self.label2["font"] = self.fonteNegrito

        self.versao = Label(self.container6)
        self.versao["text"] = "Created by por Rodrigo Fontanella - Version 1.0"
        self.versao["bd"] = "3"
        self.versao["bd"] = "2"
        self.versao["relief"] = "sunken"
        self.versao["width"] = "120"
        self.versao["bg"] = "#b6b6b6"
        self.versao.pack()
        self.versao["font"] = ("Arial", "9")

        # Text Input
        self.url = Entry(self.container1)
        self.url["width"] = 65
        self.url["borderwidth"] = 3
        self.url.pack(side=RIGHT)
        self.url["font"] = self.fontePadrao

        self.destino = Entry(self.container4)
        self.destino["width"] = 51
        self.destino["borderwidth"] = 3
        self.destino.pack(side=LEFT)
        self.destino["font"] = self.fontePadrao
        # self.destino_path = ""
        self.destino.insert(0, (os.path.dirname(__file__) + "/exported/"))

        # Buttons
        self.bot_destino = Button(self.container4)
        self.bot_destino["text"] = "Find"
        self.bot_destino["command"] = self.seleciona_destino
        self.bot_destino.pack(side=RIGHT)
        self.bot_destino["font"] = self.fonteNegrito

        self.bot_icone = Button(self.container3)
        self.bot_icone["text"] = "Find"
        self.bot_icone["command"] = self.seleciona_icone
        self.bot_icone.pack(side=RIGHT)
        self.bot_icone["font"] = self.fonteNegrito

        self.botao1 = Button(self.container5)
        self.botao1["text"] = "Generate QR Code"
        self.botao1["command"] = self.on_click
        self.botao1.pack(side=LEFT)
        self.botao1["font"] = self.fonteNegrito

        self.botao2 = Button(self.container5)
        self.botao2["text"] = "Quit"
        self.botao2["command"] = main_window.quit
        self.botao2.pack(side=RIGHT)
        self.botao2["font"] = self.fonteNegrito

    def seleciona_destino(self):
        self.destino_path = ""
        self.destino.delete(0, "end")
        self.destino_path = filedialog.askdirectory()
        self.destino.insert(0, self.destino_path)

    def seleciona_icone(self):
        # self.img_path = ""
        # self.img.delete(0, "end")
        self.img_path = filedialog.askopenfilename()
        self.img.insert(0, self.img_path)

    def on_click(self):

        self.continuar = messagebox.askyesno(
            "QR Code Generator", "The QR Code will be generated with the data typed. Do you wish to continue?")
        # print(self.continuar)

        if self.continuar:

            # joga resultado dos campos nas variaveis
            self.end_url = str(self.url.get())
            self.end_destino = self.destino.get()

            self.end_img = self.img.get()
            self.end_tamanho = self.tamanhoqr.get()

            # Testa se os campos principais foram preenchidos
            if self.end_url != "" and self.end_destino != "":

                print(self.end_url)
                print(self.end_destino)
                print(self.end_tamanho)
                print("Internal Color", self.colorintr.get(), self.colorintg.get(), self.colorintb.get())
                print("External Color", self.colorextr.get(), self.colorextg.get(), self.colorextb.get())
                print(self.end_img)

                # conta a quantidade de caracteres da url para criar o QR Code
                quantidade_caracteres = self.end_url
                # print(quantidade_caracteres)
                num_carac_url = len(quantidade_caracteres)

                # Nesta parte, configura a parte avancada do QR Code
                # Versao 1 - O menor - 21 x 21 modulos
                # Correcao de erro L M Q H
                # Box Size 10 - quantos pixels tem de tamanho
                # borda = 4  # - quantos quadros de espessura
                qr = qrcode.QRCode(
                    version=None,  # Deixei automático
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=self.end_tamanho,
                    border=4)

                qr.add_data(self.end_url)
                qr.make(fit=True)
                factory = qrcode.image.svg.SvgPathFillImage

                # Se for gerar QR em SVG
                # img_svg = qr.make_image(fill_color="black", back_color="white", image_factory=factory)
                # img_svg = qr.make_image(fill_color=(255, 195, 235), back_color=(55, 95, 35), image_factory=factory)
                img_svg = qr.make_image(fill_color=(255, 195, 235), back_color=(55, 95, 35),
                                        image_factory=factory)
                img_svg.save(self.end_destino + "/" + "default_svg.svg")
                print("SVG Generated")

                # Se for gerar QR em PNG
                img_png = qr.make_image(fill_color=(255, 195, 235),
                                        back_color=(55, 95, 35), image_factory=StyledPilImage)
                img_png.save(self.end_destino + "/" + "default_png.png")
                print("PNG Generated")

                # Salva com gradiente radial
                img_radial = qr.make_image(image_factory=StyledPilImage,
                                           color_mask=RadialGradiantColorMask(back_color=(255, 255, 255),
                                                                              center_color=(int(self.colorintr.get()),
                                                                                            int(self.colorintg.get()),
                                                                                            int(self.colorintb.get())),
                                                                              edge_color=(int(self.colorextr.get()),
                                                                                          int(self.colorextg.get()),
                                                                                          int(self.colorextb.get()))))
                img_radial.save(self.end_destino + "/" + "qrcode_radial.png")
                print("PNG Generated with degrade")

                # Salva com a imagem no centro se for diferente de vazio
                if self.end_img != "":
                    img_simbolo = qr.make_image(image_factory=StyledPilImage, embeded_image_path=self.end_img)
                    img_simbolo.save(self.end_destino + "/" + "qrcode_symbol.png")
                    print("PNG Generated with Image inside")

                # Salva arredondado
                img_round = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
                img_round.save(self.end_destino + "/" + "qrcode_round.png")
                print("PNG Generated with Rounded Corners")

                # Salva com gradiente radial, imagem no centro quadrado e cantos arredondados em imagem PNG
                img_tudo = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),
                                         embeded_image_path=self.end_img,
                                         color_mask=RadialGradiantColorMask(back_color=(255, 255, 255),
                                                                            center_color=(int(self.colorextr.get()),
                                                                                          int(self.colorextg.get()),
                                                                                          int(self.colorextb.get())),
                                                                            edge_color=(int(self.colorintr.get()),
                                                                                        int(self.colorintg.get()),
                                                                                        int(self.colorintb.get()))))
                img_tudo.save(self.end_destino + "/" + "qrcode_all.png")
                print("PNG Generated with all effets")

                self.showinfo = messagebox.showinfo("QR Code Generator", "QR Code generated with Success!")

            elif self.end_url == "":
                self.showinfo = messagebox.showinfo("Attention",
                                                    "Please fill URL address.")

            elif self.end_destino == "":
                self.showinfo = messagebox.showinfo("Attention",
                                                    "Please fill destiny path.")

            else:
                # messagebox.showinfo, messagebox.showwarning, messagebox.showerror,
                # messagebox.askquestion, messagebox.askokcancel, messagebox.askyesno
                self.showinfo = messagebox.showinfo("Attention",
                                                    "Please fill data! Minimum: URL and Destiny.")


main_window = Tk()
main_window.maxsize(660, 340)
main_window.minsize(660, 340)
Application(main_window)

# Quando tenta colocar uma imagem PNG como ícone, ele mostra um ícone genérico de imagem
# main_window.iconbitmap("/Users/rodrigofontanella/Desktop/01_curso_python_udemy/
# Curso-Python/qrcode_generator/icons/cs_icon.icns")

# Quando tenta colocar um ícone o ícone fica uma página branca
# main_window.iconbitmap("/Users/rodrigofontanella/Desktop/01_curso_python_udemy/
# Curso-Python/qrcode_generator/icons/cs_icon_png.png")

main_window.title("SIMPLE QR CODE GENERATOR")

main_window.mainloop()
