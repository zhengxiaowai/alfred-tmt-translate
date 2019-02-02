# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.live.v20180801 import models


class LiveClient(AbstractClient):
    _apiVersion = '2018-08-01'
    _endpoint = 'live.tencentcloudapi.com'


    def AddDelayLiveStream(self, request):
        """对流设置延播时间
        注意：如果在推流前设置延播，需要提前5分钟设置。

        :param request: 调用AddDelayLiveStream所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.AddDelayLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddDelayLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddDelayLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddDelayLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddLiveWatermark(self, request):
        """添加水印

        :param request: 调用AddLiveWatermark所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.AddLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddLiveWatermark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddLiveWatermarkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindLiveDomainCert(self, request):
        """域名绑定证书

        :param request: 调用BindLiveDomainCert所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.BindLiveDomainCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.BindLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindLiveDomainCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindLiveDomainCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveCallbackRule(self, request):
        """创建回调规则

        :param request: 调用CreateLiveCallbackRule所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveCallbackRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveCallbackRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveCallbackTemplate(self, request):
        """创建回调模板

        :param request: 调用CreateLiveCallbackTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveCallbackTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveCallbackTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveCert(self, request):
        """添加证书

        :param request: 调用CreateLiveCert所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveRecord(self, request):
        """- 使用前提
          1. 录制文件存放于点播平台，所以用户如需使用录制功能，需首先自行开通点播服务。
          2. 录制文件存放后相关费用（含存储以及下行播放流量）按照点播平台计费方式收取，具体请参考 [对应文档](https://cloud.tencent.com/document/product/266/2838)。

        - 模式说明
          该接口支持两种录制模式：
          1. 定时录制模式。
            需要传入开始时间与结束时间，录制任务根据时间自动开始与结束。
          2. 实时视频录制模式。
            忽略传入的开始时间，在录制任务创建后立即开始录制，录制时长支持最大为30分钟，如果传入的结束时间与当前时间差大于30分钟，则按30分钟计算，实时视频录制主要用于录制精彩视频场景，时长建议控制在5分钟以内。

        - 注意事项
          1. 调用接口超时设置应大于3秒，小于3秒重试以及频繁调用都有可能产生重复录制任务。

        :param request: 调用CreateLiveRecord所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveRecordRule(self, request):
        """创建录制规则

        :param request: 调用CreateLiveRecordRule所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveRecordRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveRecordRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveRecordTemplate(self, request):
        """创建录制模板

        :param request: 调用CreateLiveRecordTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveRecordTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveRecordTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveSnapshotRule(self, request):
        """创建截图规则

        :param request: 调用CreateLiveSnapshotRule所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveSnapshotRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveSnapshotRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveSnapshotTemplate(self, request):
        """创建截图模板

        :param request: 调用CreateLiveSnapshotTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveSnapshotTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveTranscodeRule(self, request):
        """创建转码规则

        :param request: 调用CreateLiveTranscodeRule所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveTranscodeRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveTranscodeRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveTranscodeTemplate(self, request):
        """创建转码模板

        :param request: 调用CreateLiveTranscodeTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveTranscodeTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveWatermarkRule(self, request):
        """创建水印规则

        :param request: 调用CreateLiveWatermarkRule所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveWatermarkRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveWatermarkRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveWatermarkRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveWatermarkRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePullStreamConfig(self, request):
        """添加拉流配置，目前限制添加10条任务。

        :param request: 调用CreatePullStreamConfig所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.CreatePullStreamConfigRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreatePullStreamConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePullStreamConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePullStreamConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveCallbackRule(self, request):
        """删除回调规则

        :param request: 调用DeleteLiveCallbackRule所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveCallbackRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveCallbackRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveCallbackTemplate(self, request):
        """删除回调模板

        :param request: 调用DeleteLiveCallbackTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveCallbackTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveCallbackTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveCert(self, request):
        """删除域名对应的证书

        :param request: 调用DeleteLiveCert所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveRecord(self, request):
        """用于删除录制任务

        :param request: 调用DeleteLiveRecord所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveRecordRule(self, request):
        """删除录制规则

        :param request: 调用DeleteLiveRecordRule所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveRecordRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveRecordRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveRecordTemplate(self, request):
        """删除录制模板

        :param request: 调用DeleteLiveRecordTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveRecordTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveRecordTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveSnapshotRule(self, request):
        """删除截图规则

        :param request: 调用DeleteLiveSnapshotRule所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveSnapshotRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveSnapshotRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveSnapshotTemplate(self, request):
        """删除截图模板

        :param request: 调用DeleteLiveSnapshotTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveSnapshotTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveTranscodeRule(self, request):
        """删除转码规则

        :param request: 调用DeleteLiveTranscodeRule所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveTranscodeRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveTranscodeRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveTranscodeTemplate(self, request):
        """删除转码模板

        :param request: 调用DeleteLiveTranscodeTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveTranscodeTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveWatermark(self, request):
        """删除水印

        :param request: 调用DeleteLiveWatermark所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveWatermark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveWatermarkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveWatermarkRule(self, request):
        """删除水印规则

        :param request: 调用DeleteLiveWatermarkRule所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveWatermarkRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveWatermarkRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePullStreamConfig(self, request):
        """删除直播拉流配置

        :param request: 调用DeletePullStreamConfig所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DeletePullStreamConfigRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeletePullStreamConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePullStreamConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePullStreamConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveCallbackRules(self, request):
        """获取回调规则列表

        :param request: 调用DescribeLiveCallbackRules所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveCallbackRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveCallbackRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveCallbackTemplate(self, request):
        """获取单个回调模板

        :param request: 调用DescribeLiveCallbackTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveCallbackTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveCallbackTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveCallbackTemplates(self, request):
        """获取回调模板列表

        :param request: 调用DescribeLiveCallbackTemplates所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveCallbackTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveCallbackTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveCert(self, request):
        """获取证书信息

        :param request: 调用DescribeLiveCert所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveCerts(self, request):
        """获取证书信息列表

        :param request: 调用DescribeLiveCerts所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveCerts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveCertsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveDomainCert(self, request):
        """获取域名证书信息

        :param request: 调用DescribeLiveDomainCert所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveDomainCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveDomainCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLivePlayAuthKey(self, request):
        """查询播放鉴权key

        :param request: 调用DescribeLivePlayAuthKey所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePlayAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePlayAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLivePlayAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLivePlayAuthKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLivePushAuthKey(self, request):
        """查询直播推流鉴权key

        :param request: 调用DescribeLivePushAuthKey所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePushAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePushAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLivePushAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLivePushAuthKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveRecordRules(self, request):
        """获取录制规则列表

        :param request: 调用DescribeLiveRecordRules所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveRecordRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveRecordRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveRecordTemplate(self, request):
        """获取单个录制模板

        :param request: 调用DescribeLiveRecordTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveRecordTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveRecordTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveRecordTemplates(self, request):
        """获取录制模板列表

        :param request: 调用DescribeLiveRecordTemplates所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveRecordTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveRecordTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveSnapshotRules(self, request):
        """获取截图规则列表

        :param request: 调用DescribeLiveSnapshotRules所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveSnapshotRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveSnapshotRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveSnapshotTemplate(self, request):
        """获取单个截图模板

        :param request: 调用DescribeLiveSnapshotTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveSnapshotTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveSnapshotTemplates(self, request):
        """获取截图模板列表

        :param request: 调用DescribeLiveSnapshotTemplates所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveSnapshotTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveSnapshotTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveStreamOnlineInfo(self, request):
        """查询在线推流信息列表

        :param request: 调用DescribeLiveStreamOnlineInfo所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamOnlineInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamOnlineInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamOnlineInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamOnlineInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveStreamOnlineList(self, request):
        """返回正在直播中的流列表

        :param request: 调用DescribeLiveStreamOnlineList所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamOnlineListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamOnlineListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamOnlineList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamOnlineListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveStreamPublishedList(self, request):
        """返回已经推过流的流列表

        :param request: 调用DescribeLiveStreamPublishedList所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamPublishedListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamPublishedListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamPublishedList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamPublishedListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveStreamState(self, request):
        """返回直播中、无推流或者禁播等状态

        :param request: 调用DescribeLiveStreamState所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamStateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamStateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveTranscodeRules(self, request):
        """获取转码规则列表

        :param request: 调用DescribeLiveTranscodeRules所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveTranscodeRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveTranscodeRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveTranscodeTemplate(self, request):
        """获取单个转码模板

        :param request: 调用DescribeLiveTranscodeTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveTranscodeTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveTranscodeTemplates(self, request):
        """获取转码模板列表

        :param request: 调用DescribeLiveTranscodeTemplates所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveTranscodeTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveTranscodeTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveWatermark(self, request):
        """获取单个水印信息

        :param request: 调用DescribeLiveWatermark所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveWatermark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveWatermarkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveWatermarkRules(self, request):
        """获取水印规则列表

        :param request: 调用DescribeLiveWatermarkRules所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveWatermarkRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveWatermarkRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveWatermarks(self, request):
        """查询水印列表

        :param request: 调用DescribeLiveWatermarks所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarksRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveWatermarks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveWatermarksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePullStreamConfigs(self, request):
        """查询拉流配置

        :param request: 调用DescribePullStreamConfigs所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribePullStreamConfigsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribePullStreamConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePullStreamConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePullStreamConfigsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DropLiveStream(self, request):
        """断开推流连接，但可以重新推流

        :param request: 调用DropLiveStream所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DropLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DropLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DropLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DropLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ForbidLiveStream(self, request):
        """禁止某条流的推送，可以预设某个时刻将流恢复。

        :param request: 调用ForbidLiveStream所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ForbidLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ForbidLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ForbidLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ForbidLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLiveCallbackTemplate(self, request):
        """修改回调模板

        :param request: 调用ModifyLiveCallbackTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveCallbackTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveCallbackTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLiveCert(self, request):
        """修改证书

        :param request: 调用ModifyLiveCert所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLiveDomainCert(self, request):
        """修改域名和证书绑定信息

        :param request: 调用ModifyLiveDomainCert所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveDomainCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveDomainCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveDomainCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLivePlayAuthKey(self, request):
        """修改播放鉴权key

        :param request: 调用ModifyLivePlayAuthKey所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLivePlayAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLivePlayAuthKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLivePushAuthKey(self, request):
        """修改直播推流鉴权key

        :param request: 调用ModifyLivePushAuthKey所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePushAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePushAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLivePushAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLivePushAuthKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLiveRecordTemplate(self, request):
        """修改录制模板配置

        :param request: 调用ModifyLiveRecordTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveRecordTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveRecordTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLiveSnapshotTemplate(self, request):
        """修改截图模板配置

        :param request: 调用ModifyLiveSnapshotTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveSnapshotTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLiveTranscodeTemplate(self, request):
        """修改转码模板配置

        :param request: 调用ModifyLiveTranscodeTemplate所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveTranscodeTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPullStreamConfig(self, request):
        """更新拉流配置

        :param request: 调用ModifyPullStreamConfig所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyPullStreamConfigRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyPullStreamConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPullStreamConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPullStreamConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPullStreamStatus(self, request):
        """修改直播拉流配置状态

        :param request: 调用ModifyPullStreamStatus所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyPullStreamStatusRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyPullStreamStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPullStreamStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPullStreamStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeDelayLiveStream(self, request):
        """恢复延迟播放设置

        :param request: 调用ResumeDelayLiveStream所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ResumeDelayLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ResumeDelayLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResumeDelayLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResumeDelayLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeLiveStream(self, request):
        """恢复某条流的推送。

        :param request: 调用ResumeLiveStream所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ResumeLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ResumeLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResumeLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResumeLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetLiveWatermarkStatus(self, request):
        """设置水印是否启用

        :param request: 调用SetLiveWatermarkStatus所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.SetLiveWatermarkStatusRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.SetLiveWatermarkStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetLiveWatermarkStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetLiveWatermarkStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopLiveRecord(self, request):
        """说明：录制后的文件存放于点播平台。用户如需使用录制功能，需首先自行开通点播账号并确保账号可用。录制文件存放后，相关费用（含存储以及下行播放流量）按照点播平台计费方式收取，请参考对应文档。

        :param request: 调用StopLiveRecord所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.StopLiveRecordRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.StopLiveRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopLiveRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopLiveRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnBindLiveDomainCert(self, request):
        """解绑域名证书

        :param request: 调用UnBindLiveDomainCert所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.UnBindLiveDomainCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.UnBindLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnBindLiveDomainCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnBindLiveDomainCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateLiveWatermark(self, request):
        """更新水印

        :param request: 调用UpdateLiveWatermark所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.UpdateLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.UpdateLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateLiveWatermark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateLiveWatermarkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)