import pytest
from utilities.customLogger import LogGen
from pageObjects.api.common_utils import CommonUtils
from pageObjects.api.create_board import CreateBoard
from pageObjects.api.create_card import Createcard


class Test_springboard_api:
    """
                        Description:
                            |  This class provides methods to test the workflow through api calls
            """
    logger = LogGen.loggen()
    common_utils = CommonUtils()
    create_board = CreateBoard()
    create_card = Createcard()
    board_uuid=''
    str_token=''

    @pytest.mark.api
    @pytest.mark.smoke
    def test_login(self):
        """
            Description:
                |  This is a login test.

            """
        self.logger.info("****Started Login  api Test****")
        token = self.common_utils.springboard_get_authtoken()
        if token is not None:
            self.logger.info("*** Test Login api passed****")
            assert True
        else:
            self.logger.info("*** Test Login api failed****")
            assert False


    @pytest.mark.api
    @pytest.mark.smoke
    def test_create_and_verify_board(self):
        """
                    Description:
                        |  This is a test for creation and verification of board.
        """
        self.logger.info("****Started create and verify Board Test****")
        uuid= self.create_board.create_board()[0]
        if uuid is not None:
            assert self.create_board.verify_created_board(uuid)
            self.logger.info("*** Test verify board passed****")
            assert True
        else:
            self.logger.info("*** Test verify board failed****")
            assert False


    @pytest.mark.api
    @pytest.mark.smoke
    def test_create_and_like_card(self):
        """
                            Description:
                                |  This is a test for creating and liking a went well card
                """
        card_type= "Went well"
        self.logger.info("****Started create and like card Test****")
        self.board_uuid,self.str_token = self.create_board.create_board()
        if self.board_uuid is not None:
            card_column_uuid= self.create_card.get_card_column_uuid(self.board_uuid,self.str_token, card_type)
            if card_column_uuid is not None:
                card_uuid = self.create_card.create_card(card_column_uuid,self.str_token,card_type)
                if card_uuid is not None:
                    status = self.create_card.like_card(card_uuid,self.str_token)
                    if status:
                        self.logger.info("*** Card is liked ****")
                        self.logger.info("****Ended create and like card Test Successfully****")
                        assert True
                else:
                    self.logger.info("****Some error in card creation--Test case failed****")
                    assert False
            else:
                self.logger.info("****Some error in card column --Test case failed****")
                assert False
        else:
            self.logger.info("****Some error in Board creation--Test case failed****")
            assert False


    @pytest.mark.api
    @pytest.mark.smoke
    def test_create_and_delete_card(self):
        """
                            Description:
                                |  This is a test for creating and deleting a didn't go well card
                """
        self.logger.info("****Started create and delete card Test****")
        card_type = "Didn't go well"
        self.board_uuid, self.str_token = self.create_board.create_board()
        if self.board_uuid is not None:
            card_column_uuid = self.create_card.get_card_column_uuid(self.board_uuid, self.str_token, card_type)
            if card_column_uuid is not None:
                card_uuid = self.create_card.create_card(card_column_uuid, self.str_token,card_type)
                if card_uuid is not None:
                    status = self.create_card.delete_card(card_uuid, self.str_token)
                    if status:
                        self.logger.info("*** Card is Deleted ****")
                        self.logger.info("****Ended create and Deleted card Test Successfully****")
                        assert True
                else:
                    self.logger.info("****Some error in card creation--Test case failed****")
                    self.logger.info("****Ended create and Deleted card Test Unsuccessfull****")
                    assert False
            else:
                self.logger.info("****Some error in card column --Test case failed****")
                self.logger.info("****Ended create and Deleted card Test Unsuccessfull****")
                assert False
        else:
            self.logger.info("****Some error in Board creation--Test case failed****")
            self.logger.info("****Ended create and Deleted card Test Unsuccessfull****")
            assert False