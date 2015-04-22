# -*- coding=utf-8 -*-
__author__ = 'hua'

import _otp_md
import os


class MarketDataSpi:
    def __init__(self):
        self.api = None

    def register_api(self, api):
        self.api = api

    def on_front_connected(self):
        pass

    def on_front_disconnected(self, reason, message):
        pass

    def on_rsp_user_login(self, rsp_user_login, rsp_err_id, rsp_err_msg, request_id, is_last):
        pass

    def on_rsp_user_logout(self, user_logout, rsp_err_id, rsp_err_msg, request_id, is_last):
        pass

    def on_rsp_error(self, rsp_err_id, rsp_err_msg, request_id, is_last):
        pass

    def on_rsp_sub_market_data(self, specific_instrument, rsp_err_id, rsp_err_msg, request_id, is_last):
        pass

    def on_rsp_unsub_market_data(self, specific_instrument, rsp_err_id, rsp_err_msg, request_id, is_last):
        pass

    def on_rtn_depth_market_data(self, depth_market_data):
        pass


class MarketDataApi:
    @staticmethod
    def create_api(flow_path="", is_using_udp=False):
        if flow_path:
            flow_path = os.path.abspath(flow_path)
        api_ptr = _otp_md.create_MdApi(flow_path, is_using_udp, False)
        return MarketDataApi(api_ptr)

    def __init__(self, api_ptr):
        self.api_ptr = api_ptr

    def ReqUserLogout(self, pUserLogout, nRequestID):
        '''登出请求'''
        return _otp_md.ReqUserLogout(self.api_ptr, pUserLogout, nRequestID)

    def Join(self, ):
        '''等待接口线程结束运行
        @return 线程退出代码'''
        return _otp_md.Join(self.api_ptr)


    def UnSubscribeMarketData(self, InstrumentIDs):
        """订阅/退订行情。
        @param ppInstrumentIDs list of 合约ID
        """
        return _otp_md.UnSubscribeMarketData(self.api_ptr, InstrumentIDs)

    def RegisterFront(self, pszFrontAddress):
        '''注册前置机网络地址
        @param pszFrontAddress：前置机网络地址。
        @remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。'''
        return _otp_md.RegisterFront(self.api_ptr, pszFrontAddress)

    def Init(self):
        '''初始化
        @remark 初始化运行环境,只有调用后,接口才开始工作'''
        return _otp_md.Init(self.api_ptr)

    def ReqUserLogin(self, pReqUserLoginField, nRequestID):
        '''用户登录请求'''
        return _otp_md.ReqUserLogin(self.api_ptr, pReqUserLoginField, nRequestID)

    def Release(self, ):
        '''删除接口对象本身
        @remark 不再使用本接口对象时,调用该函数删除接口对象'''
        return _otp_md.Release(self.api_ptr)

    def GetTradingDay(self, ):
        '''获取当前交易日
        @retrun 获取到的交易日
        @remark 只有登录成功后,才能得到正确的交易日'''
        return _otp_md.GetTradingDay(self.api_ptr)


    def SubscribeMarketData(self, InstrumentIDs):
        """订阅/退订行情。
        @param ppInstrumentIDs list of 合约ID
        """
        return _otp_md.SubscribeMarketData(self.api_ptr, InstrumentIDs)

    def RegisterSpi(self, pSpi):
        '''注册回调接口
        @param pSpi 派生自回调接口类的实例'''
        ret = _otp_md.RegisterSpi(self.api_ptr, pSpi)
        pSpi.register_api(self)
        return ret