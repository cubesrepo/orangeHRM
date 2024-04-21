import pytest

from pages.pim_page import PimPage
from tests.base_test import BaseTest

@pytest.mark.order(2)
class TestPim(BaseTest):

    def test_pim_page_delete_all_records(self, driver):
        pimpage = PimPage(driver)
        pimpage.got_to_pim_and_delete_all_records()

    def test_10_added_employees_and_search_them_using_their_employee_id(self, driver):
        pimpage = PimPage(driver)
        pimpage.search_all_added_employee_using_employee_id()

    def test_edit_employee_and_check_if_its_updated(self, driver):
        pimpage = PimPage(driver)
        pimpage.edit_employee()