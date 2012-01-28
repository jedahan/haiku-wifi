from flask import Flask
app = Flask(__name__)

import os
import datetime

@app.route('/say/<line1>/<line2>/<line3>')
def say_three(line1,line2,line3):
  timestamp = datetime.datetime.now().strftime("%y/%m/%d %H:%M")
  lines = [line1, line2, line3]

  for i in range(len(lines))
    os.system("echo [%s] %s >> history.log" % (timestamp, lines[i]))
    os.system("tail -n1 history.log")
    os.system("uci set wireless.@wifi-iface[%d].ssid='-%d %s'" % (i,i,lines[i]))
    os.system("uci commit wireless")
    os.system("ifup wan")
    os.system("wifi")

  return "At %s, you said %s, %s, %s" % (timestamp, lines[1], lines[2], lines[3])

@app.route('/say/<line1>/<line2>')
def say_two(line1,line2):
  say_three(line1,line2,'')

@app.route('/say/<line1>')
def say_one(line1,line2):
  say_three(line1,'','')

if __name__ == "__main__":
  app.run(port=8888,host='0.0.0.0',debug=True)
