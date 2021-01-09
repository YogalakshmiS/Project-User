from unittest import TestCase
import unittest
#target = __import__("user.py")
#tot_user_details = target.tot_user_details
from user import tot_user_details 

class test1(unittest.TestCase):
    def tot_user_details(self,get_call):
        get_call.return_value.status_code=200
        get_call.return_value.json.return_value="Load file"
        staus_code,response_data=get_gitup_user_detail("default")
        self.assertEqual(200,status_code)

class test2(unittest.TestCase):
    def users_log(self,get_call):
        get_call.return_value.status_code=200
        get_call.return_value.json.return_value="Load file"
        staus_code,response_data=get_gitup_user_detail("default")
        self.assertEqual(200,status_code)
        
class test3(unittest.TestCase):
     def tot_followers_details(self,get_call):
        get_call.return_value.status_code=200
        get_call.return_value.json.return_value="Load file"
        staus_code,response_data=get_gitup_user_detail("default")
        self.assertEqual(200,status_code)
        


if __name__ =='__main__':
    unittest.main()
        
    
