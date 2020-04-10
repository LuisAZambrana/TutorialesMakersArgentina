#!/usr/bin/python
# -*- coding: UTF-8 -*-
# www.makersargentina.com.ar
# deja tu huellamaker!
import telebot
bot = telebot.TeleBot("aca pone tu token");

import commands
import requests
import os
import time
import sys
import RPi.GPIO as gpio
import subprocess

owner == tuid

@bot.message_handler(func=lambda message: message.text.lower() == '18on' and message.chat.id == owner)
def prende_18(message):
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(18, gpio.OUT)
    gpio.output(18, True)
    bot.send_message(message.chat.id, "Pin 18 Encendido");

@bot.message_handler(func=lambda message: message.text.lower() == '18off'and message.chat.id == owner)
def prende_18(message):
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(18, gpio.OUT)
    gpio.output(18, True)
    bot.send_message(message.chat.id, "Pin 18 Apagado");

@bot.message_handler(func=lambda message: message.text.lower() == 'temperatura'and message.chat.id == owner)
def temperatura(message):
    temp    = round(int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3, 2)
    tempgpu = commands.getoutput('/opt/vc/bin/vcgencmd measure_temp').replace('temp=', '').replace("'C", '')
    bot.send_message(message.chat.id, "Temperatura:\nCPU: {} °C\nGPU: {} °C".format(temp, tempgpu));

@bot.message_handler(func=lambda message: message.text.lower() == 'uptime' and message.chat.id == owner)
def temperatura(message):
    uptime = commands.getoutput('uptime -p')
    bot.send_message(message.chat.id, "Uptime: {}".format(uptime));

@bot.message_handler(func=lambda message: message.text.lower() == 'ip'and message.chat.id == owner)
def miip(message):
    ip = requests.get("http://ipinfo.io/ip")
    bot.send_message(message.chat.id, "IP: {}".format(ip.text));

#bot.send_message(message.chat.id, "Bot iniciado");

bot.polling()

