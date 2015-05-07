"""
Test for pyTona
"""
from pyTona.question_answer import *
from unittest import TestCase
from tests.ReqTracer import requirements
from tests.plugins.traceability import log
from pyTona.main import *
import re
import getpass
from pyTona.answer_funcs import *
import subprocess
from inspect import isfunction
#import mock
from mock import Mock
import socket
#from mutant import *
import string
import random
import time



value = 7
output = None
process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)

def answerGenerator():
    return "This is the Answer!"
MAXSIZE = 1000000

class TestPyTona(TestCase):

    def setUp(self):
        self.dream = Interface()




    # #0001 The system shall accept questions in the form of strings and attempt to answer them
    # @requirements(['#0001','#0001'])
    # def test_0001_string(self):
    #     question = "question string"
    #     #question = 1
    #     answer = ""
    #     result = QA(question, answer)
    #     #self.assertEqual(result,"a")
    #     self.assertTrue(isinstance(question, str))
    #     self.assertTrue(isinstance(result.value,str))


    # @requirements(['#0001','#0001'])
    # def test_0001_nonstring(self):
    #     question = 1
    #     dream = Interface()
    #     try:
    #         answer = dream.ask(question)
    #     except Exception as e:
    #         self.assertEqual(str(e),"Not A String!")

    # #0002 The system shall answer questions that begin with one of the following valid question keywords: "How", "What", "Where", "Why" and "Who"
    # @requirements(['#0002','#0002'])
    # def test_0002(self):
    #     dream = Interface()
    #     answer = dream.ask("How about a valid question?")
    #     self.assertTrue(isinstance(answer,str))
    #     self.assertNotEqual(answer, NOT_A_QUESTION_RETURN)


       
    # #0003 If the system does not detect a valid question keyword it shall return "Was that a question?"
    # @requirements(['#0003','#0003'])
    # def test_0003(self):
    #     dream = Interface()
    #     question = "Invalide question?"
    #     answer = dream.ask(question)
    #     self.assertTrue(isinstance(answer,str))
    #     self.assertEqual(answer, NOT_A_QUESTION_RETURN)


    # #0004 If the system does not detect a question mark at end of the string it shall return "Was that a question?" 
    # @requirements(['#0004','#0004'])       
    # def test_0004(self):
    #     dream = Interface()
    #     question = "Invalide question without question mark"
    #     answer = dream.ask(question)
    #     self.assertTrue(isinstance(answer,str))
    #     self.assertEqual(answer, NOT_A_QUESTION_RETURN)    

    # #0005 The system shall break a question down into words separated by space
    # @requirements(['#0005','#0005'])        
    # def test_0005(self):
    #     question = "The system shall break a question down into words separated by space"
    #     words=question.split()
    #     for word in words:
    #         self.assertEqual(re.search(' ',word),None)
   

    # #0006 The system shall determine an answer to a question as a correct if the keywords provide a 90% match and return the answer  
    # @requirements(['#0006','#0006'])       
    # def test_0006(self):
    #     dream = Interface()
    #     question = "How many seconds since 1942"
    #     try:
    #         answer = dream.ask(question)
    #         self.assertTrue(isinstance(answer,str))
    #         self.assertNotEqual(answer, NOT_A_QUESTION_RETURN)    
    #         slef.assertEqual(answer, "42 seconds")
    #     except Exception:
    #         self.assertNotEqual(str(Exception),"Too many extra parameters")

    # #0007 The system shall exclude any number value from match code and provide the values to generator function (if one exists)   
    # @requirements(['#0007','#0007'])      
    # def test_0007(self):
    #     dream = Interface()
    #     question = "How many seconds since 1942193740198743184301"
    #     try:
    #         answer = dream.ask(question)
    #         self.assertTrue(isinstance(answer,str))
    #         self.assertNotEqual(answer, NOT_A_QUESTION_RETURN)    
    #         slef.assertEqual(answer, "42 seconds")
    #         question = "What is 5280 feet in miles?"
    #         answer = dream.ask(question)
    #         self.assertEqual(answer, '1.0 miles')              
    #     except Exception:
    #         self.assertNotEqual(str(Exception),"Too many extra parameters") 

    # #0008 When a valid match is determined the system shall return the answer 
    # @requirements(['#0008','#0008'])      
    # def test_0008(self):
    #     dream = Interface()
    #     question = "How about a valid match?"
    #     answer = dream.ask(question)
    #     self.assertTrue(isinstance(answer,str))
    #     self.assertNotEqual(answer, NOT_A_QUESTION_RETURN)    

    # #0009 When no valid match is determined the system shall return "I don't know, please provide the answer"   
    # @requirements(['#0009','#0009'])       
    # def test_0009(self):
    #     dream = Interface()
    #     question = "How about an unknown question?"
    #     answer = dream.ask(question)
    #     self.assertTrue(isinstance(answer,str))
    #     self.assertEqual(answer, UNKNOWN_QUESTION)    

    # #0010 The system shall provide a means of providing an answer to the previously asked question.  
    # @requirements(['#0010','#0010'])       
    # def test_0010(self):
    #     dream = Interface()
    #     question = "How about an unknown question?"
    #     answer = dream.ask(question)
    #     self.assertTrue(isinstance(answer,str))
    #     self.assertEqual(answer, UNKNOWN_QUESTION) 
    #     newAnswer = "This is a known answer"
    #     dream.teach(newAnswer)   
    #     answer = dream.ask(question)
    #     self.assertEqual(answer, newAnswer) 



    # #0011 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.
    # @requirements(['#0011','#0011'])           
    # def test_0011(self):
    #     dream = Interface()
    #     question = "How about an unknown question?"
    #     answer = dream.ask(question)
    #     self.assertTrue(isinstance(answer,str))
    #     self.assertEqual(answer, UNKNOWN_QUESTION) 
    #     funcdict = {'answerGenerator': answerGenerator}
    #     newAnswer = funcdict['answerGenerator']()  
    #     dream.teach(newAnswer)   
    #     answer = dream.ask(question)
    #     self.assertEqual(answer, newAnswer) 
        


    # #0012 If no previous question has been asked the system shall respond with "Please ask a question first"  
    # @requirements(['#0012','#0012'])       
    # def test_0012(self):
    #     dream = Interface()
    #     newAnswer = "This is the answer without any question"
    #     answer = dream.teach(newAnswer)
    #     self.assertTrue(isinstance(answer,str))
    #     self.assertEqual(answer, NO_QUESTION)    

    # #0013 If an attempt is made to provide an answer to an already answered question the system shall respond with "I don\'t know about that. I was taught differently" and not update the question        
    # @requirements(['#0013','#0013']) 
    # def test_0013_provide_answer_for_already_answered_question(self):
    #     dream = Interface()
    #     question = "Why don't you understand me?"
    #     answer = dream.ask(question)
    #     print (answer)
    #     newAnswer = "This is an unacceptable answer"
    #     teach_result = dream.teach(newAnswer)   
    #     self.assertEqual(teach_result, NO_TEACH)   

    # #0014 The system shall provide a means of updating an answer to the previously asked question.     
    # @requirements(['#0014','#0014'])  
    # def test_0014(self):
    #     dream = Interface()
    #     question = "How to updating an answer to the previously asked question?"
    #     answer = dream.ask(question)
    #     newAnswer = "This is the updated answer"
    #     self.assertTrue(hasattr(dream, 'correct'))


    # #0015 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.
    # @requirements(['#0015','#0015'])         
    # def test_0015(self):
    #     dream = Interface()
    #     question = "How to updating an answer to the previously asked question?"
    #     answer = dream.ask(question)
    #     newAnswer = "This is the updated answer"
    #     dream.correct(newAnswer)
    #     answer = dream.ask(question)
    #     self.assertTrue(isinstance(answer,str))
    #     self.assertEqual(answer, newAnswer)    

    # #0016 If no previous question has been asked the system shall respond with "Please ask a question first" 
    # @requirements(['#0016','#0016'])     
    # def test_0016(self):
    #     dream = Interface()
    #     newAnswer = "No previous question has been asked"
    #     correct_result = dream.correct(newAnswer)
    #     self.assertEqual(correct_result, NO_QUESTION)    

    # #0017 The system shall respond to the question "What is <float> feet in miles" with the the float value divided by 5280 and append "miles" to the end of  the return.        
    # @requirements(['#0017','#0017']) 
    # def test_0017(self):
    #     dream = Interface()
    #     question = "What is 5280 feet in miles?"
    #     answer = dream.ask(question)
    #     self.assertEqual(answer, '1.0 miles')    

    # # #0018 The system shall respond to the question "How many seconds since <date time>" with the number of seconds from that point of day till now. 
    # # @requirements(['#0018','#0018'])        
    # # def test_0018(self):
    # #     dream = Interface()
    # #     question = "How many seconds since 1982?"
    # #     answer = dream.ask(question)
    # #     self.assertTrue(isinstance(answer,str))
    # #     self.assertNotEqual(answer, UNKNOWN_QUESTION)    
    # #     self.assertNotEqual(answer, '42 seconds') 

    # #0019 The system shall respond to the question "Who invented Python" with "Guido Rossum(BFDL)"    
    # @requirements(['#0019','#0019'])      
    # def test_0019_who_invented_python(self):
    #     dream = Interface()
    #     question = "Who invented Python?"
    #     answer = dream.ask(question)
    #     self.assertTrue(isinstance(answer,str))
    #     self.assertEqual(answer, 'Guido Rossum(BDFL)')    

    # #0020 The system shall respond to the question "Why don't you understand me" with "Because you do not speak 1s and 0s"  
    # @requirements(['#0020','#0020'])       
    # def test_0020(self):
    #     dream = Interface()
    #     question = "Why don't you understand me?"
    #     answer = dream.ask(question)
    #     self.assertTrue(isinstance(answer,str))
    #     self.assertEqual(answer, 'Because you do not speak 1s and 0s')    

    # #0021 The system shall respond to the question "Why don't you shutdown" with "I'm afraid I can't do that <username>" 
    # @requirements(['#0021','#0021'])        
    # def test_0021(self):
    #     dream = Interface()
    #     question = "Why don't you shutdown?"
    #     answer = dream.ask(question)
    #     self.assertTrue(isinstance(answer,str))
    #     self.assertEqual(answer, "I'm afraid I can't do that {0}".format(getpass.getuser()) )   

    # #0022 The system shall respond to the question "Where am I" with the local git branch name or "unknown" if it can't be determined 
    # @requirements(['#0022','#0022'])        
    # def test_0022_where_am_I(self):
    #     dream = Interface()
    #     question = "Where am I?"
    #     answer = dream.ask(question)
    #     self.assertTrue(isinstance(answer,str))
    #     if answer=="unknown":
    #         self.assertTrue(1)
    #     else:
    #         self.assertEqual(answer, get_git_branch())       

    # #0023 The system shall respond to the question "Where are you" with the URL for the git repo or "unknown" if it can't be determined             
    # @requirements(['#0023','#0023'])        
    # def test_0023_where_are_you(self):
    #     dream = Interface()
    #     question = "Where are you?"
    #     answer = dream.ask(question)
    #     self.assertTrue(isinstance(answer,str))
    #     if answer=="unknown":
    #         self.assertTrue(1)
    #     else:
    #         self.assertEqual(answer, get_git_url())   

    # #0024 The system shall respond to the question "Who else is here" with a list of users             
    # @requirements(['#0024','#0024'])        
    # def test_0024_who_else_is_here(self):
    #     dream = Interface()
    #     question = "Who else is here?"
    #     dream.ask = Mock(return_value=['user1','user2'])
    #     answer = dream.ask(question)
    #     self.assertIsInstance(answer,list)

    # #0025 When determining users the system shall connect to the server at ip address 192.168.64.3 port 1337 and sending a message "Who?"            
    # @requirements(['#0025','#0025'])        
    # def test_0025_able_determining_user(self):
    #     # self.assertTrue(hasattr('answer_funcs', 'get_other_users')) 
    #     # self.assertTrue(inspect.isfunction(answer_funcs.get_other_users)) 
    #     get_other_users = Mock(return_value={'ip':'192.168.64.3','port':1337,'msg':'Who?'})   
    #     server = get_other_users()
    #     self.assertTrue(isinstance(server,dict))
    #     self.assertEqual(server['ip'],'192.168.64.3')
    #     self.assertEqual(server['port'],1337)
    #     self.assertEqual(server['msg'],'Who?')


                 

    # #0026 If a response is received from the server the user list shall be parsed from a "$" seperated list of users            
    # @requirements(['#0026','#0026'])        
    # def test_0026_user_list_seperate_by_dollar_sign(self):
    #     dream = Interface()
    #     question = "Who else is here?"
    #     answer = dream.ask(question)
    #     if answer != "IT'S A TRAAAPPPP":
    #         self.assertTrue('$' not in ''.join(answer))
      

    # #0027 If no response is received from the server the system shall return "IT'S A TRAAAPPPP"
    # @requirements(['#0027','#0027'])        
    # def test_0027_no_response_received_from_server(self):
    #     dream = Interface()
    #     question = "Who else is here?"
    #     answer = dream.ask(question)
    #     if not (isinstance(answer,list)):
    #         self.assertEqual(answer,"IT'S A TRAAAPPPP")

    # #0028 The system shall respond to the question "What is the <int> digit of the Fibonacci sequence?" with the correct number from the fibonnacci sequence if the number has been found            
    # @requirements(['#0028','#0028'])        
    # def test_0028_fibonacci_sequence_find_number(self):
    #     # time_start = int(round(time.time() * 1000))
    #     # question = "What is the 0 digit of the Fibonacci sequence?" 
    #     # answer = self.dream.ask(question)
    #     # time.sleep(0.6)    
    #     # time_end = int(round(time.time() * 1000))
    #     # #time.sleep(80)
    #     # log.info(time_start)
    #     # log.info(time_end)
    #     # log.info(time_end-time_start)        
        
    #     question = "What is the 0 digit of the Fibonacci sequence?"
    #     self.dream.ask(question)
    #     time.sleep(60)
    #     # # #global answer_funcs.seq_finder
    #     # # #sql_finder.stop()
    #     # question = "What is the 1 digit of the Fibonacci sequence?"
    #     # answer = self.dream.ask(question)
    #     # time.sleep(0.6)
    #     # question = "What is the 2 digit of the Fibonacci sequence?"
    #     # answer = self.dream.ask(question)
    #     # time.sleep(0.6)
    #     # question = "What is the 3 digit of the Fibonacci sequence?"
    #     # answer = self.dream.ask(question)
    #     # time.sleep(0.6)
    #     #self.dream.sql_finder = FibSeqFinder()
    #     #global seq_finder
    #     # self.dream.seq_finder = FibSeqFinder(name='testing')
    #     # self.dream.seq_finder.start()
    #     # time.sleep(45)  
    #     # self.dream.seq_finder.join()
    #     question = "What is the 4 digit of the Fibonacci sequence?"
    #     answer = self.dream.ask(question)
            
    #     self.assertEqual(answer,3)  


    # #0029 If the system has not determined the requested digit of the Fibonacci sequence it will respond with A)"Thinking...", B)"One second" or C)"cool your jets" based on a randomly generated number (A is 60% chance, B is 30% chance, C is 10% chance)        
    # @requirements(['#0029','#0029'])        
    # def test_0029_fibonacci_sequence_not_determined(self):
    #     question = "What is the 1002 digit of the Fibonacci sequence?"
    #     answer = self.dream.ask(question)
    #     time.sleep(60)
    #     if answer == 'Thinking...':
    #         pass
    #     elif answer == 'One second':
    #         pass
    #     elif answer == 'cool your jets':
    #         pass
    #     else:
    #         self.assertEqual(answer,'Thinking ... or One second or cool your jets')    

    #     # random.randint=Mock(return_value=7)
    #     # self.assertEqual(get_fibonacci_seq(5),"Thinking...")
    #     # random.randint=Mock(return_value=4)
    #     # self.assertEqual(get_fibonacci_seq(5),"One second")
    #     # random.randint=Mock(return_value=2)
    #     # self.assertEqual(get_fibonacci_seq(5),"cool your jets")
    #     subprocess.Popen=Mock(return_value=None)
    #     self.assertEqual(get_git_branch(),'Unknown')
    #     #subprocess.Popen=Mock(return_value=1)
    #     #subprocess.Popen.communicate = Mock(return_value=(None,None))
    #     # process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
    #     process.communicate = Mock(return_value=(None,None))
    #     self.assertEqual(get_git_branch(),'Unknown')
    #     output = None
    #     self.assertEqual(get_git_branch(),'Unknown')
    #     #socket.socket.send = Mock(return_value = 10)
    #     #socket.socket.recv = Mock(return_value = 'Harry$Mike$john')
    #     #socket.socket.close = Mock(return_value = 1)
    #     #self.assertEqual(socket.socket.send('Who?'),10)
    #     #socket.socket.send.assert_called_with('Who?')
    #     #recv = Mock(return_value = 'Harry$Mike$john')
    #     #self.assertEqual(get_other_users(),['Harry','Mike','john'])
    #     #global seq_finder

    #     #self.assertTrue(isfunction(stop))
    #     #self.assertTrue(hasattr(seq_finder, 'stop'))


    # #0030 The system shall be capable of storing at least 1,000,000 questions and answers
    # @requirements(['#0030','#0030'])        
    # def test_0030_store_1000000_questions_and_answers(self):
    #     # dream = Interface()
    #     # for i in range(10000):
    #     #     random_string = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(20))
    #     #     question = "How " + random_string + " ?"
    #     #     answer = dream.ask(question)
    #     #     self.assertTrue(isinstance(answer,str))
    #     #     self.assertEqual(answer, UNKNOWN_QUESTION)  
    #     #     dream.teach('The answer is ' + str(i))   
    #     # self.assertEqual(i,9999)

    #     current_size = len(self.dream.question_answers)
    #     for i in range(MAXSIZE-current_size):
    #         question = 'How about question ' + str(i + current_size)
    #         self.dream.question_answers[question] = QA(question, 'The answer is ' + str(i + current_size))
    #     self.assertEqual(len(self.dream.question_answers),MAXSIZE)     
          


    # #0031 The system shall store answers in under 5 ms 
    # @requirements(['#0031','#0031'])        
    # def test_0031_store_answer_less_then_5_ms(self):
    #     #dream = Interface()
    #     #self.assertEqual(len(dream.question_answers),1000000)  
    #     #current_size = len(dream.question_answers)
    #     # for i in range(1000000-current_size):
    #     #     dream.question_answers['How about question ' + str(i + current_size) + ' ?'] = 'The answer is ' + str(i + current_size) 
    #     # self.assertEqual(i,1000000-current_size - 1)           
    #     # random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))
    #     # question = 'How ' + random_string + ' ?'

    #     # MAXSIZE = 100
    #     # current_size = len(dream.question_answers)
    #     # for i in range(MAXSIZE-current_size):
    #     #     random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))
    #     #     question = 'How about question ' + str(i + current_size)
    #     #     dream.question_answers[question] = QA(question, 'The answer is ' + str(i + current_size))
    #     # self.assertEqual(i,MAXSIZE-current_size - 1)   
    #     # self.assertEqual(len(self.dream.question_answers),MAXSIZE)
    #     # question = 'How about question 10?'    
    #     # self.assertEqual(dream.ask(question),'The answer is 10') 

    #     question = 'How about a pretty simeple but a little bit long question ?'
    #     answer = self.dream.ask(question)
    #     self.assertTrue(isinstance(answer,str))
    #     self.assertEqual(answer, UNKNOWN_QUESTION)  
    #     time_start = int(round(time.time() * 1000))
        
    #     #(dream).teach('The answer is ' + random_string)   
    #     self.dream.teach('okay this is the answer!!!')      
    #     time_end = int(round(time.time() * 1000))
    #     log.info(time_start)
    #     log.info(time_end)
    #     log.info(time_end-time_start)
    #     self.assertTrue(time_end - time_start < 5)


                  

    # #0032 The system shall be able to retrieve a response in under 5 ms 
               
    # @requirements(['#0032','#0032'])        
    # def test_0032__retrieve_response_less_then_5_ms(self):
    #     question = 'How about a pretty simeple but a little bit long question ?'
    #     time_start = int(round(time.time() * 1000))
    #     answer = self.dream.ask(question)
    #     time_end = int(round(time.time() * 1000))
    #     self.assertTrue(isinstance(answer,str))
    #     #self.assertEqual(answer,'okay this is the answer!!!')
    #     log.info(time_start)
    #     log.info(time_end)
    #     log.info(time_end-time_start)        
    #     self.assertTrue(time_end - time_start < 5)     


    # #0033 The system shall stop generating Fibonacci sequence numbers once it has identified the first 1,000 numbers
       
    # @requirements(['#0033','#0033'])        
    # def test_0033_stop_generating_fibonacci_once_reach_1000_number(self):
    #     # question = "What is the 0 digit of the Fibonacci sequence?"
    #     # self.dream.ask(question)
    #     # time.sleep(0.6)
    #     # #global answer_funcs.seq_finder
    #     # #sql_finder.stop()
    #     # question = "What is the 1 digit of the Fibonacci sequence?"
    #     # self.dream.ask(question)
    #     # time.sleep(0.6)
    #     # question = "What is the 2 digit of the Fibonacci sequence?"
    #     # self.dream.ask(question)
    #     # time.sleep(0.6)
    #     # question = "What is the 3 digit of the Fibonacci sequence?"
    #     # self.dream.ask(question)
    #     # time.sleep(0.6)
    #     # question = "What is the 4 digit of the Fibonacci sequence?"
    #     # self.dream.ask(question)
    #     # time.sleep(0.6)
    #     question = "What is the 1002 digit of the Fibonacci sequence?"
    #     answer = self.dream.ask(question)
    #     #time.sleep(60)
    #     if answer == 'Thinking...':
    #         pass
    #     elif answer == 'One second':
    #         pass
    #     elif answer == 'cool your jets':
    #         pass
    #     else:
    #         self.assertEqual(answer,'Thinking ... or One second or cool your jets')            
        
        


    # #0034 The system shall generate the first 1,000 Fibonacci sequence numbers in under 60 seconds     
    # @requirements(['#0034','#0034'])        
    # def test_0034_data_mutation_test(self):
    #     question = "What is the 1000 digit of the Fibonacci sequence?"
    #     time_start = time.clock()
    #     answer = self.dream.ask(question)
    #     time_end = time.clock()
    #     #self.assertTrue(isinstance(answer,str))
    #     log.info(time_start)
    #     log.info(time_end)
    #     log.info(time_end-time_start)        
    #     self.assertTrue(time_end - time_start < 60)             

    # #0035 The system shall get the Fibonacci sequence list in under 60 seconds     
    # @requirements(['#0035','#0035'])        
    # def test_0035_get_fibonacci_list_under_60secs(self):
    #     question = "What is the first 10 numbers of the Fibonacci sequence?"
    #     time_start = time.clock()
    #     answer = self.dream.ask(question)
    #     time_end = time.clock()
    #     #self.assertTrue(isinstance(answer,str))
    #     log.info(time_start)
    #     log.info(time_end)
    #     log.info(time_end-time_start)        
    #     self.assertTrue(time_end - time_start < 60)       

    #0036 The system shall able to write to a file     
    # @requirements(['#0036','#0036'])        
    # def test_0036_write_to_file(self):
    #     question = "How about write to a file?"
    #     answer = self.dream.ask(question)
    #     self.assertEqual(answer,'Successfully write to file!')         

    #0037 The system shall able to read from a file     
    @requirements(['#0037','#0037'])        
    def test_0037_write_to_file(self):
        question = "How about read from a file?"
        answer = self.dream.ask(question)
        self.assertEqual(answer,'Successfully write to file!')                