Haiku-Wifi will turn your router into a virtual billboard, letting anyone put up messages to be seen on thier wifi ssid list :)

Created at the 2012 [arthackday](http://arthackday.net) by [Toby Schachman](https://github.com/electronicwhisper) and [Jonathan Dahan](http://jonathan.is)

Some [pics](http://www.flickr.com/photos/37234044@N07/sets/72157629094958315/) of people enjoying the poetry.


Install
-------

 1. Install software dependencies
   * Install python with `opkg install python`
   * Install [setuptools](http://pypi.python.org/pypi/setuptools#cygwin-mac-os-x-linux-other)
   * Install flask with `easy_install Flask'

 2. Configure the radio
   * Create three wifi interfaces to be used for the haiku
   * Edit haiku.py to make sure the offset for the three wifi interfaces you want to use (`uci show wireless` will help here)
   * Add a fourth called '-4 --- ☁ haiku wifi ☁ ---'

 3. Configure the router
   * Change uhttpd to run on port 81 by editing `/etc/config/uhttpd` and restart with `/etc/init.d/uhttpd restart`
   * Edit dnsmasq to route all traffic to localhost
   * Run manually with `python haiku.py`
   * Or install and enable the init script, `cp haiku-wifi /etc/init.d && /etc/init.d/haiku-wifi enable`
