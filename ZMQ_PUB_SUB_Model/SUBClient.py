#!/usr/bin/python

__author__ = "Weqaar Janjua & Ahmer Malik"
__copyright__ = "Copyright (C) 2016 Linux IoT"
__revision__ = "$Id$"
__version__ = "1.0"

import zmq
import threading
from time import *

from PrintHeader import _header

_thread_pool = []


# This function can be used in multi-threaded applications

class ZMQ_SUBClient(threading.Thread):
    def __init__(self,_meg_device_ip,_port_low_latency):
        threading.Thread.__init__(self)
        self._meg_device_ip = _meg_device_ip
        self._port_low_latency = _port_low_latency

    def run(self):
        context = zmq.Context()
        print "Starting Low-latency Service"
        socket = context.socket(zmq.SUB)
        socket.setsockopt (zmq.SUBSCRIBE, '')
        socket.connect ("tcp://" + self._meg_device_ip + ":%s" % self._port_low_latency)
        print "Started, listening for messages (SUB) from: " + self._meg_device_ip + "\n"
        while True:
            sleep(0.02)
            message = socket.recv()
            print message
            if message is None:
                pass
            else:
                print "MESSAGE PUT: " + message + "\n"


if __name__ == '__main__':
    x = _header(__file__,__author__,__copyright__,__version__)
    x._print()
    IP = "127.0.0.1"
    PORT = "5678"
    t1 = ZMQ_SUBClient(IP,PORT)
    t1.start()
    _thread_pool.append(t1)
    
    
    
                
