import pytest

from pages.recruitment_page import RecruitmentPage


@pytest.mark.recruitment
class TestRecruitment:
    @pytest.fixture
    def recruitment_page(self, login_driver, delay):
        return RecruitmentPage(login_driver, delay)

    def test_added_candidate_info(self, recruitment_page):
        current_result_values, expected_result_values = recruitment_page.verify_add_valid_candidate()

        for current_result_value, expected_result_value in zip(current_result_values, expected_result_values):
            assert current_result_value == expected_result_value, \
                f"Expected result to be {expected_result_value}, but got {current_result_value} instead."