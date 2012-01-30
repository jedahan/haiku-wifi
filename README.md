Haiku-Wifi will turn your router into a virtual billboard, letting anyone put up messages to be seen on thier wifi ssid list :)

Created at the 2012 [arthackday](http://arthackday.net) by [Toby Schachman](https://github.com/electronicwhisper) and [Jonathan Dahan](http://jonathan.is)

Some [pics](http://www.flickr.com/photos/37234044@N07/sets/72157629094958315/) of people enjoying the poetry.


Install
-------

 1. Install python with `opkg install python`
 2.  Install [setuptools](http://pypi.python.org/pypi/setuptools#cygwin-mac-os-x-linux-other)
 3.  Install flask with `easy_install Flask'
 4.  Create three interfaces for a radio on your router
 5.  Edit haiku.py to make sure the offset for the three wifi interfaces you want to use (`uci show wireless` will help here)
 6.  Edit dnsmasq if you want to turn this into a captive portal
 7. `python haiku.py`
 8. If you want to have it start on boot, `cp haiku-wifi /etc/init.d && /etc/init.d/haiku-wifi enable`
