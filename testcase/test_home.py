# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 测试首页
"""
import pytest,time,allure
from module.home import Home
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()
from config import *

@allure.feature("测试首页")
@pytest.mark.usefixtures('driver_setup')
class TestHome:

    @pytest.fixture()
    def init(self,scope="class"):
        self.home = Home(self.driver)
        logger.info("初始化首页")
        yield self.home
        logger.info("结束首页")


    @allure.story('测试首页搜索')
    def test_home_search(self,init):
        init.home_search()

    @allure.story('测试首页搜索参数化')
    @pytest.mark.parametrize(('kewords'), [("司机"), ("老师"), ("公寓")])
    def test_home_moresearch(self, init,kewords):
        init.home_more_search(kewords)

    @allure.story('测试首页更多')
    def test_home_more(self, init):
        init.home_more()

    @allure.story('测试推荐')
    def test_home_guesslike(self, init):
        init.home_guesslike()

