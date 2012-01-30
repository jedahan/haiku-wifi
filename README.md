Haiku-Wifi will turn your router into a virtual billboard, letting anyone put up messages to be seen on thier wifi ssid list :)

Created at the 2012 [arthackday](http://arthackday.net) by [Toby Schachman](https://github.com/electronicwhisper) and [Jonathan Dahan](http://jonathan.is)



Install
-------

  Install python with `opkg install python`
  Install [setuptools](http://pypi.python.org/pypi/setuptools#cygwin-mac-os-x-linux-other)
  Install flask with `easy_install Flask'
  Create three interfaces for a radio on your router
  Edit haiku.py to make sure the offset for the three wifi interfaces you want to use (`uci show wireless` will help here)
  Edit dnsmasq if you want to turn this into a captive portal
  `python haiku.py`
