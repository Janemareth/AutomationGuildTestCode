"""
//******************************************************************************
//
// Copyright (c) 2016 Microsoft Corporation. All rights reserved.
//
// This code is licensed under the MIT License (MIT).
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//
//******************************************************************************
"""

import unittest
from appium import webdriver
import time

class TicTacToeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
    #def setUp(self):
        #set up appium
        desired_caps = {}
        desired_caps["app"] = "21206Escogitare.118907EF0A6F8_pf25qgb8cxswy!App"
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= desired_caps)      
    @classmethod
    def tearDownClass(cls):
    #def tearDown(self):
        cls.driver.quit()

    def test_initialize(self):

        #Player1Box = self.driver.find_element_by_accessibility_id("tbPlayer1Name")
        #Player2Box = self.driver.find_element_by_accessibility_id("tbPlayer2Name")
        time.sleep(10)
        self.driver.find_element_by_accessibility_id("rb2Players").click()

        #TextSettingsButton
        time.sleep(5)
        self.driver.find_element_by_name("Preferences").click()

        #btnStyle0

        self.driver.find_element_by_accessibility_id("btnStyle0").click()

        #tbPlayer1Name

        self.driver.find_element_by_accessibility_id("tbPlayer1Name").click()

        self.driver.find_element_by_accessibility_id("tbPlayer1Name").clear()

        self.driver.find_element_by_accessibility_id("tbPlayer1Name").send_keys("Unicorncode")

        #tbPlayer2Name

        self.driver.find_element_by_accessibility_id("tbPlayer2Name").click()

        self.driver.find_element_by_accessibility_id("tbPlayer2Name").clear()
        
        self.driver.find_element_by_accessibility_id("tbPlayer2Name").send_keys("Jane")

        #ButtonOk

        self.driver.find_element_by_accessibility_id("ButtonOk").click()

        #txtName1

        Player1 = self.driver.find_element_by_accessibility_id("txtName1")
        self.assertTrue(str(Player1.text), "Unicorncode")

        #txtName2

        Player2 = self.driver.find_element_by_accessibility_id("txtName2")
        self.assertTrue(str(Player2.text), "Jane")

       



    def test_play(self):
        #b00 = self.driver.find_element_by_id("2A.410A02.3.1A").click()
        #b00 = self.driver.find_element_by_xpath("//Button[contains(.,'1')]").click
        #self.assertTrue(str(b00.text),"1: X")

        #b22 = self.driver.find_element_by_accessibility_id("b22").click()
        #self.assertTrue(str(b22.text),"9: X")
    
        #player 1 is X and player 2 is O
        
        #Player 1 and Player 2 first turn 
        X1 = self.driver.find_element_by_name("1.").click()
        time.sleep(3)
        b00 = self.driver.find_element_by_accessibility_id("b00")
        self.assertTrue(str(b00.text),"1: X")
        
        O1 = self.driver.find_element_by_name("9.").click()
        time.sleep(3)
        b22 = self.driver.find_element_by_accessibility_id("b22")
        self.assertTrue(str(b00.text),"9: O")

        #player 1 and player 2 second turn
        X2 = self.driver.find_element_by_name("8.").click()
        time.sleep(3)
        b21 =self.driver.find_element_by_accessibility_id("b21")
        self.assertTrue(str(b00.text),"8: X")

        O2 = self.driver.find_element_by_name("6.").click()
        time.sleep(3)
        b12 = self.driver.find_element_by_accessibility_id("b12")
        self.assertTrue(str(b00.text),"6: O")
        
        #player 1 and player 2 third turn
        X3 = self.driver.find_element_by_name("3.").click()
        time.sleep(2)
        b02 = self.driver.find_element_by_accessibility_id("b02")
        self.assertTrue(str(b00.text),"3: X")

        O3 = self.driver.find_element_by_name("2.").click()
        time.sleep(2)
        b01 = self.driver.find_element_by_accessibility_id("b01")
        self.assertTrue(str(b00.text),"2: O")
        

        #Player 1 and player 2 last turn 
        X4 = self.driver.find_element_by_name("7.").click()
        time.sleep(2)
        b20 = self.driver.find_element_by_accessibility_id("b20")
        self.assertTrue(str(b00.text),"7: X")

        O4 = self.driver.find_element_by_name("4.").click()
        time.sleep(2)
        b10 = self.driver.find_element_by_accessibility_id("b10")
        self.assertTrue(str(b00.text),"4: O")

        #Player 1 wins on this turn
        X5 = self.driver.find_element_by_name("5.").click()
        time.sleep(2)
        b11 = self.driver.find_element_by_accessibility_id("b11")
        self.assertTrue(str(b00.text),"5: X")





if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TicTacToeTest)
        unittest.TextTestRunner(verbosity=2).run(suite)

