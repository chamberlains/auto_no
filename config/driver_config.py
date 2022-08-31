from selenium.webdriver.common.by import By


class DriverConfig:
    origin_url = "https://inner-sso-qa.weizhipin.com/iuc/user/login?token=zhipinhr-v2&callback=https%3A%2F%2Fnoah-qa" \
                 ".weizhipin.com%2Fdashboard%2Fpages%2Fhome "
    url = "https://noah-qa.weizhipin.com/dashboard/pages/home"
    cookie = {
        "name": "t_zhipinhr-v2",
        "value": "6juCLACCt2EA3y3UvLxPV3",
    }
    iuc_cookie = {
        "name": "t_uc",
        "value": "6juCLACCt2EA3y3UvLxPV3",
    }
