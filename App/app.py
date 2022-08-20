#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# Telegram : @DIBIBl , @TDTDI ,@ruks3
# Coded by ruks,or,muntazir
# YouTube : https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA
# Instagram : https://instagram.com/_v_go?utm_medium=copy_link
# github : https://github.com/muntazir-halim
# ---------------------
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.utils.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.utils import get_color_from_hex
from pytube import YouTube
from kivymd.uix.menu import MDDropdownMenu
import arabic_reshaper
from kivymd.uix.list import OneLineAvatarIconListItem
from kivy.metrics import dp
import bidi.algorithm
import webbrowser,threading
from kivymd.uix.progressbar import MDProgressBar 
import asynckivy as ak
import os
Window.softinput_mode = "below_target"



class app(MDApp): 
	previousprogress = 0
	def open_ga(self): 
		webbrowser.open("https://t.me/DIBIBl")		
	def Menu(self):
		data = {
            "1080p":"youtube",
            "720p": "youtube",
            "480p": "youtube",
            "360p": "youtube",
            "240p": "youtube",
            "144p": "youtube",
        }
		menu_items = [
            {                
            	 "viewclass": "OneLineAvatarIconListItem",
                "text": f"{i[0]}",
                "height": dp(50),
                "on_release": lambda x=i[0]: self.set_item(x),
            }for i in data.items() ]
		self.menu = MDDropdownMenu( 
            caller=self.screen.ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=4,
        )       
		self.menu.bind()       
		self.menu.open()      
	def set_item(self, text_item): 
		self.screen.ids.drop_item.set_item(text_item)
		self.menu.dismiss()			
	def build(self):
		self.screen=Builder.load_file("Frontend/style.kv")		
		self.theme_cls.theme_style = "Light"
		return self.screen
		#self.theme_cls.primary_palette = 'Red'
	def on_start(self): 
		if not os.path.exists("/sdcard/Movies/VideoTube"): 
			os.makedirs("/sdcard/Movies/VideoTube")
		#file=open("sdcard/kk/u.txt", "w")   
	def open_video(self,obj):
		webbrowser.open(text)		
	def Thread(self): 
		ak.start(self.data_on())
	async def data_on(self): 
		global text
		text=self.root.ids.input.text
		self.root.ids.input.text = ""
		self.root.ids.VA.value =0
		if "https://" in text:			
			video = YouTube(text)
			Title=video.title			
			self.root.ids.info.md_bg_color =(0,0,0,0)
			self.root.ids.lab.text =bidi_text = bidi.algorithm.get_display(arabic_reshaper.reshape("[size=50][font=fonts/Arabic.ttf]. . . جاري التحميل[/size]")) 
			self.root.ids.img_move.source =""
			self.root.ids.info.add_widget(FitImage(source=video.thumbnail_url,size_hint_y= .94,pos_hint= {'center_x':0.5,'center_y':0.5}))		
			if Title[0] in ("جحخهعغفقثصضطكمنتالبيسشدظزوةىرؤءذ") :
				bidi_text = bidi.algorithm.get_display(arabic_reshaper.reshape(Title))		 
				self.root.ids.info.add_widget(MDLabel(text= f'[size=40][font=fonts/Arabic.ttf]{bidi_text}[/size]',markup=True,pos_hint= {"center_x": .52, "center_y": .1},theme_text_color= "Custom",text_color= get_color_from_hex("#57c2f8")))
			else:
				self.root.ids.info.add_widget(MDLabel(text= f'[size=40][font=fonts/Ubuntu-Medium.ttf]{Title}[/size]',markup=True,pos_hint= {"center_x": .52, "center_y": .2},theme_text_color= "Custom",text_color= get_color_from_hex("#57c2f8")))																		
			self.root.ids.info.add_widget(MDIconButton(icon="youtube",pos_hint= {"center_x": .5, "center_y": .5},size_hint_x=1,user_font_size="80sp" ,theme_text_color= 'Custom',text_color=get_color_from_hex("#F87474"),ripple_scale=0,on_press=self.open_video))
		await ak.sleep(0)
		threading.Thread(target=self.Download ,args=(text,)).start() 	
		
	def on_progress(self,stream, chunk, bytes_remaining): 
		previousprogress= self.previousprogress
		total_size = stream.filesize
		bytes_downloaded = total_size - bytes_remaining 
		liveprogress = (int)(bytes_downloaded / total_size * 100)
		if liveprogress > previousprogress: 
			previousprogress = liveprogress
			self.root.ids.VA.value =liveprogress
			if previousprogress ==100:
				self.root.ids.lab.text =bidi_text = bidi.algorithm.get_display(arabic_reshaper.reshape("[size=50][font=fonts/Arabic.ttf]اكتمل التحميل[/size]")) 			
	def Download(self,text): 
		yt = YouTube(text)
			
		yt.register_on_progress_callback(self.on_progress)
		yt.streams.filter(res=self.root.ids.drop_item.text).first().download("/sdcard/Movies/VideoTube")
if __name__ == '__main__':
    
    app().run()