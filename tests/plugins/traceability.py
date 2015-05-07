import logging
import os

#from ReqTracer import *
from nose2.events import Plugin

log = logging.getLogger('nose2.plugins.traceability')


class Traceability(Plugin):
    configSection = 'traceability'
    commandLineSwitch = (None, 'traceability', 'trace!')


    # def getTestCaseNamesEvent(self, event):
    #     print "+++++",event.testcase.id()

    def startTestRun(self, event):
        log.info("requirement ++++++")
        # log.info(Requirements['#0001'])
        # flog = open("ReqTracer.log", "w")
        # for key,value in Requirements.iteritems():
        #     flog.write(key + " " + value + "\n")
        # flog.close()           
        # for r in Requirements:
        #   log.info(r)

    def testOutCome(self, event):
        log.info('outcome++++++++' + event.outcome)

    def startTest(self, event):
        log.info('startTest++++++++' + event.test)      

    def stopTest(self, event):
        log.info("stop test")        

    def outcomeDetail(self, event):
        log.info("outcome detail")        

"""
    def reportFailure(self, event):
        log.info("test failed!")
"""     

