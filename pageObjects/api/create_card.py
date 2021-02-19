import os
import json
from utilities.config_utils import ConfigUtils
from core.api.api_helper import RequestBuilder
from pageObjects.api.common_utils import CommonUtils
from utilities.customLogger import LogGen



class Createcard(RequestBuilder, CommonUtils,LogGen):
    config_utils = ConfigUtils(os.getcwd())

    def __init__(self):
        self.response = ""
        self.response_content= ""
        self.str_request_url = ""
        self.str_auth_token =""


    def validate_reponse(self):
        """
        Description:
        	|  This method calls the is_responsevalid from comon_utils to validate the response code
        :return: None
        """
        bln_response = self.is_responsevalid(self.response)
        return bln_response


    def get_card_column_uuid(self,board_uuid, str_token, pstr_card_type):
        """
                                        Description:
                                            |  This method allows user to get card column uuid

                                        :param uuid: uuid of the created board
                                        :type uuid: String
                                        :param str_token: auth_token
                                        :type str_token: String
                                        :param pstr_card_type: card type e.g. Went well
                                        :type pstr_card_type: String


                                        :return: boolean
                                """
        self.str_auth_token = str_token
        dict_service_disc = self.config_utils.get_servicedescription("springboard_description.yml", "get_board")
        str_request_url = dict_service_disc["target_url"] + dict_service_disc["endpoint"] +"/"+ str(board_uuid)+ dict_service_disc[
            "queryparams"]
        headers = dict_service_disc["headers"]
        headers["Authorization"] = "Bearer "+self.str_auth_token
        payload = dict_service_disc["payload"]
        self.response = self.call_request(dict_service_disc["method"], str_request_url,
                                                       headers, pstr_payload=payload)
        self.response_content = self.response.content
        bln_response1 = self.is_reponsegenerated(self.response)
        bln_validate_response = self.validate_reponse()
        response_json = json.loads(self.response_content)
        if bln_response1 and bln_validate_response:
            for i in range(0,3):
                if response_json['data']['columns'][i]['title']==pstr_card_type:
                    self.loggen().info("*****Card Column found***")
                    str_uuid= response_json['data']['columns'][i]['uuid']
                    return str_uuid
            else:
                self.loggen().info("*****Card Column not found***")
                return None
        else:
            self.loggen().info("*****Board is not verified successfully***Response code"+ str(self.response.status_code) )
            return None


    def create_card(self,str_card_column_uuid, str_token,card_type):
        """
                                                Description:
                                                    |  This method allows user to create_card

                                                :param str_card_column_uuid: uuid of the card
                                                :type str_card_column_uuid: String
                                                :param str_token: auth_token
                                                :type str_token: String
                                                :param card_type: card type e.g. Went well
                                                :type card_type: String
                                                :return: boolean
                                        """
        dict_service_disc={}
        self.str_auth_token = str_token
        if card_type=="Went well":
            dict_service_disc = self.config_utils.get_servicedescription("springboard_description.yml", "create_well_card")
        elif card_type=="Didn't go well":
            dict_service_disc = self.config_utils.get_servicedescription("springboard_description.yml","create_not_well_card")
        str_request_url = dict_service_disc["target_url"] + dict_service_disc["endpoint"] + dict_service_disc["queryparams"]
        headers = dict_service_disc["headers"]
        headers["Authorization"] = "Bearer " + self.str_auth_token
        payload = dict_service_disc["payload"] +"," + "\"" + "column_uuid" + "\"" + ":" + "\"" + str_card_column_uuid + "\"" +"}"
        self.response = self.call_request(dict_service_disc["method"], str_request_url,
                                                          headers, pstr_payload=payload)
        self.response_content = self.response.content
        bln_response1 = self.is_reponsegenerated(self.response)
        bln_validate_response = self.validate_reponse()
        response_json = json.loads(self.response_content)
        if bln_response1 and bln_validate_response:
            self.loggen().info("*****Card is created successfully***")
            card_uuid = response_json['data']['uuid']
            return card_uuid
        else:
            self.loggen().info("*****Card is not created successfully***Response code"+ str(self.response.status_code) )
            return None



    def like_card(self,str_card_uuid, str_token):
        """
                                                        Description:
                                                            |  This method allows user to like_card

                                                        :param str_card_uuid: uuid of the card
                                                        :type str_card_uuid: String
                                                        :param str_token: auth_token
                                                        :type str_token: String
                                                        :return: boolean
                                                """
        self.str_auth_token = str_token
        dict_service_disc = self.config_utils.get_servicedescription("springboard_description.yml", "like_card")
        str_request_url = dict_service_disc["target_url"] + dict_service_disc["endpoint"] +"/"+ str(str_card_uuid)+"/like"+ dict_service_disc["queryparams"]
        headers = dict_service_disc["headers"]
        headers["Authorization"] = "Bearer " + self.str_auth_token
        payload = dict_service_disc["payload"]
        self.response = self.call_request(dict_service_disc["method"], str_request_url,
                                                          headers, pstr_payload=payload)
        self.response_content = self.response.content
        bln_response1 = self.is_reponsegenerated(self.response)
        bln_validate_response = self.validate_reponse()
        response_json = json.loads(self.response_content)
        if bln_response1 and bln_validate_response:
            self.loggen().info("*****Like request send successfully***")
            status = response_json['status']
            return status
        else:
            self.loggen().info("*****Like request unsuccessfull***Response code"+ str(self.response.status_code) )
            return None


    def delete_card(self,str_card_uuid, str_token):
        """
                                                                Description:
                                                                    |  This method allows user to delete_card

                                                                :param str_card_uuid: uuid of the card
                                                                :type str_card_uuid: String
                                                                :param str_token: auth_token
                                                                :type str_token: String
                                                                :return: boolean
                                                        """
        self.str_auth_token = str_token
        dict_service_disc = self.config_utils.get_servicedescription("springboard_description.yml", "delete_card")
        str_request_url = dict_service_disc["target_url"] + dict_service_disc["endpoint"] +"/"+ str(str_card_uuid)+ dict_service_disc["queryparams"]
        headers = dict_service_disc["headers"]
        headers["Authorization"] = "Bearer " + self.str_auth_token
        payload = dict_service_disc["payload"]
        self.response = self.call_request(dict_service_disc["method"], str_request_url,
                                                          headers, pstr_payload=payload)
        self.response_content = self.response.content
        bln_response1 = self.is_reponsegenerated(self.response)
        bln_validate_response = self.validate_reponse()
        response_json = json.loads(self.response_content)
        if bln_response1 and bln_validate_response:
            self.loggen().info("*****Delete request send successfully***")
            status = response_json['status']
            return status
        else:
            self.loggen().info("*****Delete request unsuccessfull***Response code"+ str(self.response.status_code) )
            return None



