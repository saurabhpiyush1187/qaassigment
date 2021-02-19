from testdata.page_properties.login_locators import Loginlocators
from utilities.customLogger import LogGen
from testdata.page_properties.homepage_locators import Homepagelocators
from testdata.page_properties.createboard_locators import Boardlocators
import os
from utilities.readProperties import ReadConfig
from core.ui.ui_helper import UIHelper

class BoardPage(Loginlocators,Homepagelocators, Boardlocators,LogGen):
    # Board Page
    explicit_wait = ReadConfig.getexplicitwait()

    def __init__(self,driver):
        self.driver=driver
        self.ui_helper = UIHelper(self.driver)


    def go_to_create_board(self):
        bln_createboard_link = self.ui_helper.is_element_displayed(self.pstr_createboard_link)
        if bln_createboard_link:
            self.ui_helper.click(self.pstr_createboard_link)
            self.loggen().info("****Create Board link clicked****")
            assert True
        else:
            self.loggen().info("****Create Board link Not present or clickable****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createBoard_link.png")
            self.driver.close()
            assert False


    def verify_page_header(self,str_pageheader):
        pstr_page_header = self.pstr_page_header.format(str_pageheader)
        bln_page_header = self.ui_helper.is_element_displayed(pstr_page_header)
        if bln_page_header:
            self.loggen().info("****Page Header is Create a Board****")
            return True
        else:
            self.loggen().info("****Page header is different****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createBoard_header.png")
            self.driver.close()
            return False


    def create_board(self,str_session_name, owner, str_succes_message):
        """
                Description:
                    |  This method allows user to create_board

                :param str_session_name: Name of the session
                :type str_session_name: String
                :param owner: Select owner
                :type owner: String
                :param str_succes_message: Success message after board is created
                :type str_succes_message: String
                :return: boolean: if the board is created successfully
        """
        bln_session_name = self.ui_helper.is_element_displayed(self.pstr_input_session_name)
        if bln_session_name:
            self.ui_helper.type(self.pstr_input_session_name,str_session_name)
            self.loggen().info("****Entered session name****   " + str(str_session_name))
        else:
            self.loggen().info("****Unable to enter session name****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createBoard_session.png")
            self.driver.close()
            return False

        bln_owner_drop_down = self.ui_helper.is_element_displayed(self.pstr_owner_drop_down)
        if bln_owner_drop_down:
            self.ui_helper.select_dropdown_value(self.pstr_owner_drop_down,visible_text=owner)
            self.loggen().info("****Selected Owner name****   " + str(owner))
        else:
            self.loggen().info("****Unable to select session name****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createBoard_owner.png")
            self.driver.close()
            return False

        bln_submit_create_board = self.ui_helper.is_element_displayed(self.pstr_createboard_button)
        if bln_submit_create_board:
            self.ui_helper.click(self.pstr_createboard_button)
            self.loggen().info("****Clicked create board button***")
        else:
            self.loggen().info("****Unable to click create board button****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createBoard_button.png")
            self.driver.close()
            return False

        bln_pop_up= self.ui_helper.is_element_displayed(self.pstr_pop_up)
        if bln_pop_up:
            str_text= self.driver.find_element_by_class_name('swal-title').text
            if str_text== str_succes_message:
                self.loggen().info("***Success message verified****")
                return True
            else:
                self.loggen().info("***Success message not verified****" + "Expected message: " + str_succes_message + "Actual message: " + str_text)
                self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createBoard_message.png")
                self.driver.close()
                return False


