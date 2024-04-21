import pytest

from pages.recruitment_page import RecruitmentPage
from tests.base_test import BaseTest

@pytest.mark.order(3)
class Testrecruitment(BaseTest):


    def test_valid_candidates(self, driver):
        recruitmentpage = RecruitmentPage(driver)
        recruitmentpage.go_to_recruiment_page()
        recruitmentpage.add_valid_candidates()