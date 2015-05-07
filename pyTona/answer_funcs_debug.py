import getpass
import random
import socket
import subprocess
import threading
import time
from time import strftime
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

seq_finder = None

def feet_to_miles(feet):
    return "{0} miles".format(float(feet) / 5280)

def hal_20():
    return "I'm afraid I can't do that {0}".format(getpass.getuser())

def get_git_branch():
    try:
        process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "Unknown"

    if not output:
        return "Unknown"
    return output.strip()

def get_git_url():
    try:
        process = subprocess.Popen(['git', 'config', '--get', 'remote.origin.url'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "Unknown"

    if not output:
        return "Unknown"
    return output.strip()

def get_other_users():
    try:
        host = '192.168.64.3'
        port = 1337

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send('Who?')
        data = s.recv(255)
        s.close()
        return data.split('$')

    except:
        return "IT'S A TRAAAPPPP"


class FibSeqFinder(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(FibSeqFinder, self).__init__(*args, **kwargs)
        self.sequence = [0, 1]
        self._stop = threading.Event()
        self.num_indexes = 0

    def stop(self):
        self._stop.set()

    def run(self):
        logging.debug('running thread... ')
        self.num_indexes = 0
        while not self._stop.isSet() and self.num_indexes <= 1000:
            self.sequence.append(self.sequence[-1] + self.sequence[-2])
            self.num_indexes += 1
            logging.debug( 'num_indexes=' + str(self.num_indexes))
            time.sleep(.04)

def get_fibonacci_seq(index):
    index = int(index)
    global seq_finder
    logging.debug(seq_finder)
    if seq_finder is None:
        
        seq_finder = FibSeqFinder(name='inner thread')
        seq_finder.start()

    logging.debug('passed in index='+str(index))
    logging.debug('seq_finder.num_indexes='+ str(seq_finder.num_indexes))
    if index > seq_finder.num_indexes:
        value = random.randint(0, 10)
        if value > 4:
            return "Thinking..."
        elif value > 1:
            return "One second"
        else:
            return "cool your jets"
    else:
        return seq_finder.sequence[index]

def get_fibonacci_seq_list(index):
    index = int(index)
    global seq_finder
    logging.debug(seq_finder)
    if seq_finder is None:
        
        seq_finder = FibSeqFinder(name='get_fibonacci_seq_list')
        seq_finder.start()
        seq_finder.join()

    logging.debug('passed in index='+str(index))
    logging.debug('seq_finder.num_indexes='+ str(seq_finder.num_indexes))
    if index > seq_finder.num_indexes:
        value = random.randint(0, 10)
        if value > 4:
            return "Thinking..."
        elif value > 1:
            return "One second"
        else:
            return "cool your jets"
    else:
        return seq_finder.sequence[:index]        

def write_to_file():
    my_list = [i**2 for i in range(1,1)]
    try:
        f = open("output.txt", "a")

        for item in my_list:
            f.write(strftime("%Y-%m-%d %H:%M:%S ") + str(item) + "\n")

        f.close()
        return 'Successfully write to file!'
    except:
        return 'IO Error'

# seq_finder = FibSeqFinder(name='Main')
# seq_finder.start()
# time.sleep(0.6)
# # logging.debug(get_fibonacci_seq(3))
# # time.sleep(0.6)
# logging.debug('seq_finder.num_indexes='+ str(seq_finder.num_indexes))
# logging.debug(get_fibonacci_seq(3))

#print get_fibonacci_seq_list(20)
write_to_file()