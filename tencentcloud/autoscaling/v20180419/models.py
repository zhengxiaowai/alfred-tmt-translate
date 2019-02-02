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

from tencentcloud.common.abstract_model import AbstractModel


class Activity(AbstractModel):
    """符合条件的伸缩活动相关信息。

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param ActivityId: 伸缩活动ID。
        :type ActivityId: str
        :param ActivityType: 伸缩活动类型。取值如下：<br>
<li>SCALE_OUT：扩容活动<li>SCALE_IN：缩容活动<li>ATTACH_INSTANCES：添加实例<li>REMOVE_INSTANCES：销毁实例<li>DETACH_INSTANCES：移出实例<li>TERMINATE_INSTANCES_UNEXPECTEDLY：实例在CVM控制台被销毁<li>REPLACE_UNHEALTHY_INSTANCE：替换不健康实例）
        :type ActivityType: str
        :param StatusCode: 伸缩活动状态。取值如下：<br>
<li>INIT：初始化中
<li>RUNNING：运行中
<li>SUCCESSFUL：活动成功
<li>PARTIALLY_SUCCESSFUL：活动部分成功
<li>FAILED：活动失败
<li>CANCELLED：活动取消
        :type StatusCode: str
        :param StatusMessage: 伸缩活动状态描述。
        :type StatusMessage: str
        :param Cause: 伸缩活动起因。
        :type Cause: str
        :param Description: 伸缩活动描述。
        :type Description: str
        :param StartTime: 伸缩活动开始时间。
        :type StartTime: str
        :param EndTime: 伸缩活动结束时间。
        :type EndTime: str
        :param CreatedTime: 伸缩活动创建时间。
        :type CreatedTime: str
        :param ActivityRelatedInstanceSet: 伸缩活动相关实例信息集合。
        :type ActivityRelatedInstanceSet: list of ActivtyRelatedInstance
        :param StatusMessageSimplified: 伸缩活动状态简要描述。
        :type StatusMessageSimplified: str
        """
        self.AutoScalingGroupId = None
        self.ActivityId = None
        self.ActivityType = None
        self.StatusCode = None
        self.StatusMessage = None
        self.Cause = None
        self.Description = None
        self.StartTime = None
        self.EndTime = None
        self.CreatedTime = None
        self.ActivityRelatedInstanceSet = None
        self.StatusMessageSimplified = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.ActivityId = params.get("ActivityId")
        self.ActivityType = params.get("ActivityType")
        self.StatusCode = params.get("StatusCode")
        self.StatusMessage = params.get("StatusMessage")
        self.Cause = params.get("Cause")
        self.Description = params.get("Description")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("ActivityRelatedInstanceSet") is not None:
            self.ActivityRelatedInstanceSet = []
            for item in params.get("ActivityRelatedInstanceSet"):
                obj = ActivtyRelatedInstance()
                obj._deserialize(item)
                self.ActivityRelatedInstanceSet.append(obj)
        self.StatusMessageSimplified = params.get("StatusMessageSimplified")


class ActivtyRelatedInstance(AbstractModel):
    """与本次伸缩活动相关的实例信息。

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param InstanceStatus: 实例在伸缩活动中的状态。取值如下：
<li>SUCCESSFUL：活动成功
<li>FAILED：活动失败
        :type InstanceStatus: str
        """
        self.InstanceId = None
        self.InstanceStatus = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceStatus = params.get("InstanceStatus")


class AttachInstancesRequest(AbstractModel):
    """AttachInstances请求参数结构体

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param InstanceIds: CVM实例ID列表
        :type InstanceIds: list of str
        """
        self.AutoScalingGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.InstanceIds = params.get("InstanceIds")


class AttachInstancesResponse(AbstractModel):
    """AttachInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AutoScalingGroup(AbstractModel):
    """伸缩组

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param AutoScalingGroupName: 伸缩组名称
        :type AutoScalingGroupName: str
        :param AutoScalingGroupStatus: 伸缩组状态
        :type AutoScalingGroupStatus: str
        :param CreatedTime: 创建时间，采用UTC标准计时
        :type CreatedTime: str
        :param DefaultCooldown: 默认冷却时间，单位秒
        :type DefaultCooldown: int
        :param DesiredCapacity: 期望实例数
        :type DesiredCapacity: int
        :param EnabledStatus: 启用状态，取值包括`ENABLED`和`DISABLED`
        :type EnabledStatus: str
        :param ForwardLoadBalancerSet: 应用型负载均衡器列表
        :type ForwardLoadBalancerSet: list of ForwardLoadBalancer
        :param InstanceCount: 实例数量
        :type InstanceCount: int
        :param InServiceInstanceCount: 状态为`IN_SERVICE`实例的数量
        :type InServiceInstanceCount: int
        :param LaunchConfigurationId: 启动配置ID
        :type LaunchConfigurationId: str
        :param LaunchConfigurationName: 启动配置名称
        :type LaunchConfigurationName: str
        :param LoadBalancerIdSet: 传统型负载均衡器ID列表
        :type LoadBalancerIdSet: list of str
        :param MaxSize: 最大实例数
        :type MaxSize: list of int non-negative
        :param MinSize: 最小实例数
        :type MinSize: list of int non-negative
        :param ProjectId: 项目ID
        :type ProjectId: list of int non-negative
        :param SubnetIdSet: 子网ID列表
        :type SubnetIdSet: list of str
        :param TerminationPolicySet: 销毁策略
        :type TerminationPolicySet: list of str
        :param VpcId: VPC标识
        :type VpcId: str
        :param ZoneSet: 可用区列表
        :type ZoneSet: list of str
        :param RetryPolicy: 重试策略
        :type RetryPolicy: str
        """
        self.AutoScalingGroupId = None
        self.AutoScalingGroupName = None
        self.AutoScalingGroupStatus = None
        self.CreatedTime = None
        self.DefaultCooldown = None
        self.DesiredCapacity = None
        self.EnabledStatus = None
        self.ForwardLoadBalancerSet = None
        self.InstanceCount = None
        self.InServiceInstanceCount = None
        self.LaunchConfigurationId = None
        self.LaunchConfigurationName = None
        self.LoadBalancerIdSet = None
        self.MaxSize = None
        self.MinSize = None
        self.ProjectId = None
        self.SubnetIdSet = None
        self.TerminationPolicySet = None
        self.VpcId = None
        self.ZoneSet = None
        self.RetryPolicy = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.AutoScalingGroupName = params.get("AutoScalingGroupName")
        self.AutoScalingGroupStatus = params.get("AutoScalingGroupStatus")
        self.CreatedTime = params.get("CreatedTime")
        self.DefaultCooldown = params.get("DefaultCooldown")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.EnabledStatus = params.get("EnabledStatus")
        if params.get("ForwardLoadBalancerSet") is not None:
            self.ForwardLoadBalancerSet = []
            for item in params.get("ForwardLoadBalancerSet"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self.ForwardLoadBalancerSet.append(obj)
        self.InstanceCount = params.get("InstanceCount")
        self.InServiceInstanceCount = params.get("InServiceInstanceCount")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        self.LoadBalancerIdSet = params.get("LoadBalancerIdSet")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.ProjectId = params.get("ProjectId")
        self.SubnetIdSet = params.get("SubnetIdSet")
        self.TerminationPolicySet = params.get("TerminationPolicySet")
        self.VpcId = params.get("VpcId")
        self.ZoneSet = params.get("ZoneSet")
        self.RetryPolicy = params.get("RetryPolicy")


class AutoScalingGroupAbstract(AbstractModel):
    """伸缩组简明信息。

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param AutoScalingGroupName: 伸缩组名称。
        :type AutoScalingGroupName: str
        """
        self.AutoScalingGroupId = None
        self.AutoScalingGroupName = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.AutoScalingGroupName = params.get("AutoScalingGroupName")


class CreateAutoScalingGroupRequest(AbstractModel):
    """CreateAutoScalingGroup请求参数结构体

    """

    def __init__(self):
        """
        :param AutoScalingGroupName: 伸缩组名称，在您账号中必须唯一。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超55个字节。
        :type AutoScalingGroupName: str
        :param LaunchConfigurationId: 启动配置ID
        :type LaunchConfigurationId: str
        :param MaxSize: 最大实例数，取值范围为0-2000。
        :type MaxSize: int
        :param MinSize: 最小实例数，取值范围为0-2000。
        :type MinSize: int
        :param VpcId: VPC ID，基础网络则填空字符串
        :type VpcId: str
        :param DefaultCooldown: 默认冷却时间，单位秒，默认值为300
        :type DefaultCooldown: int
        :param DesiredCapacity: 期望实例数，大小介于最小实例数和最大实例数之间
        :type DesiredCapacity: int
        :param LoadBalancerIds: 传统负载均衡器ID列表，目前长度上限为1，LoadBalancerIds 和 ForwardLoadBalancers 二者同时最多只能指定一个
        :type LoadBalancerIds: list of str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param ForwardLoadBalancers: 应用型负载均衡器列表，目前长度上限为1，LoadBalancerIds 和 ForwardLoadBalancers 二者同时最多只能指定一个
        :type ForwardLoadBalancers: list of ForwardLoadBalancer
        :param SubnetIds: 子网ID列表，VPC场景下必须指定子网
        :type SubnetIds: list of str
        :param TerminationPolicies: 销毁策略，目前长度上限为1。取值包括 OLDEST_INSTANCE 和 NEWEST_INSTANCE，默认取值为 OLDEST_INSTANCE。
<br><li> OLDEST_INSTANCE 优先销毁伸缩组中最旧的实例。
<br><li> NEWEST_INSTANCE，优先销毁伸缩组中最新的实例。
        :type TerminationPolicies: list of str
        :param Zones: 可用区列表，基础网络场景下必须指定可用区
        :type Zones: list of str
        :param RetryPolicy: 重试策略，取值包括 IMMEDIATE_RETRY 和 INCREMENTAL_INTERVALS，默认取值为 IMMEDIATE_RETRY。
<br><li> IMMEDIATE_RETRY，立即重试，在较短时间内快速重试，连续失败超过一定次数（5次）后不再重试。
<br><li> INCREMENTAL_INTERVALS，间隔递增重试，随着连续失败次数的增加，重试间隔逐渐增大，重试间隔从秒级到1天不等。
        :type RetryPolicy: str
        :param ZonesCheckPolicy: 可用区校验策略，取值包括 ALL 和 ANY，默认取值为ANY。
<br><li> ALL，所有可用区（Zone）或子网（SubnetId）都可用则通过校验，否则校验报错。
<br><li> ANY，存在任何一个可用区（Zone）或子网（SubnetId）可用则通过校验，否则校验报错。

可用区或子网不可用的常见原因包括该可用区CVM实例类型售罄、该可用区CBS云盘售罄、该可用区配额不足、该子网IP不足等。
如果 Zones/SubnetIds 中可用区或者子网不存在，则无论 ZonesCheckPolicy 采用何种取值，都会校验报错。
        :type ZonesCheckPolicy: str
        """
        self.AutoScalingGroupName = None
        self.LaunchConfigurationId = None
        self.MaxSize = None
        self.MinSize = None
        self.VpcId = None
        self.DefaultCooldown = None
        self.DesiredCapacity = None
        self.LoadBalancerIds = None
        self.ProjectId = None
        self.ForwardLoadBalancers = None
        self.SubnetIds = None
        self.TerminationPolicies = None
        self.Zones = None
        self.RetryPolicy = None
        self.ZonesCheckPolicy = None


    def _deserialize(self, params):
        self.AutoScalingGroupName = params.get("AutoScalingGroupName")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.VpcId = params.get("VpcId")
        self.DefaultCooldown = params.get("DefaultCooldown")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.ProjectId = params.get("ProjectId")
        if params.get("ForwardLoadBalancers") is not None:
            self.ForwardLoadBalancers = []
            for item in params.get("ForwardLoadBalancers"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self.ForwardLoadBalancers.append(obj)
        self.SubnetIds = params.get("SubnetIds")
        self.TerminationPolicies = params.get("TerminationPolicies")
        self.Zones = params.get("Zones")
        self.RetryPolicy = params.get("RetryPolicy")
        self.ZonesCheckPolicy = params.get("ZonesCheckPolicy")


class CreateAutoScalingGroupResponse(AbstractModel):
    """CreateAutoScalingGroup返回参数结构体

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AutoScalingGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.RequestId = params.get("RequestId")


class CreateLaunchConfigurationRequest(AbstractModel):
    """CreateLaunchConfiguration请求参数结构体

    """

    def __init__(self):
        """
        :param LaunchConfigurationName: 启动配置显示名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。
        :type LaunchConfigurationName: str
        :param ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-8toqc6s3`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>
        :type ImageId: str
        :param ProjectId: 实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/378/4400) 的返回值中的`projectId`字段来获取。不填为默认项目。
        :type ProjectId: int
        :param InstanceType: 实例机型。不同实例机型指定了不同的资源规格，具体取值可通过调用接口 [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749) 来获得最新的规格表或参见[实例类型](https://cloud.tencent.com/document/product/213/11518)描述。
`InstanceType`和`InstanceTypes`参数互斥，二者必填一个且只能填写一个。
        :type InstanceType: str
        :param SystemDisk: 实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        :param DataDisks: 实例数据盘配置信息。若不指定该参数，则默认不购买数据盘，最多支持指定11块数据盘。
        :type DataDisks: list of DataDisk
        :param InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        :param LoginSettings: 实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。
        :type LoginSettings: :class:`tencentcloud.autoscaling.v20180419.models.LoginSettings`
        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的`SecurityGroupId`字段来获取。若不指定该参数，则默认不绑定安全组。
        :type SecurityGroupIds: list of str
        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。
        :type EnhancedService: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        :param UserData: 经过 Base64 编码后的自定义数据，最大长度不超过16KB。
        :type UserData: str
        :param InstanceChargeType: 实例计费类型，CVM默认值按照POSTPAID_BY_HOUR处理。
<br><li>POSTPAID_BY_HOUR：按小时后付费
<br><li>SPOTPAID：竞价付费
        :type InstanceChargeType: str
        :param InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数，若指定实例的付费模式为竞价付费则该参数必传。
        :type InstanceMarketOptions: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param InstanceTypes: 实例机型列表，不同实例机型指定了不同的资源规格，最多支持5种实例机型。
`InstanceType`和`InstanceTypes`参数互斥，二者必填一个且只能填写一个。
        :type InstanceTypes: list of str
        :param InstanceTypesCheckPolicy: 实例类型校验策略，取值包括 ALL 和 ANY，默认取值为ANY。
<br><li> ALL，所有实例类型（InstanceType）都可用则通过校验，否则校验报错。
<br><li> ANY，存在任何一个实例类型（InstanceType）可用则通过校验，否则校验报错。

实例类型不可用的常见原因包括该实例类型售罄、对应云盘售罄等。
如果 InstanceTypes 中一款机型不存在或者已下线，则无论 InstanceTypesCheckPolicy 采用何种取值，都会校验报错。
        :type InstanceTypesCheckPolicy: str
        """
        self.LaunchConfigurationName = None
        self.ImageId = None
        self.ProjectId = None
        self.InstanceType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.InternetAccessible = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.EnhancedService = None
        self.UserData = None
        self.InstanceChargeType = None
        self.InstanceMarketOptions = None
        self.InstanceTypes = None
        self.InstanceTypesCheckPolicy = None


    def _deserialize(self, params):
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        self.ImageId = params.get("ImageId")
        self.ProjectId = params.get("ProjectId")
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.UserData = params.get("UserData")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.InstanceTypes = params.get("InstanceTypes")
        self.InstanceTypesCheckPolicy = params.get("InstanceTypesCheckPolicy")


class CreateLaunchConfigurationResponse(AbstractModel):
    """CreateLaunchConfiguration返回参数结构体

    """

    def __init__(self):
        """
        :param LaunchConfigurationId: 当通过本接口来创建启动配置时会返回该参数，表示启动配置ID。
        :type LaunchConfigurationId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LaunchConfigurationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.RequestId = params.get("RequestId")


class CreateScheduledActionRequest(AbstractModel):
    """CreateScheduledAction请求参数结构体

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param ScheduledActionName: 定时任务名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。同一伸缩组下必须唯一。
        :type ScheduledActionName: str
        :param MaxSize: 当定时任务触发时，设置的伸缩组最大实例数。
        :type MaxSize: int
        :param MinSize: 当定时任务触发时，设置的伸缩组最小实例数。
        :type MinSize: int
        :param DesiredCapacity: 当定时任务触发时，设置的伸缩组期望实例数。
        :type DesiredCapacity: int
        :param StartTime: 定时任务的首次触发时间，取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。
        :type StartTime: str
        :param EndTime: 定时任务的结束时间，取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。<br><br>此参数与`Recurrence`需要同时指定，到达结束时间之后，定时任务将不再生效。
        :type EndTime: str
        :param Recurrence: 定时任务的重复方式。为标准[Cron](https://zh.wikipedia.org/wiki/Cron)格式<br><br>此参数与`EndTime`需要同时指定。
        :type Recurrence: str
        """
        self.AutoScalingGroupId = None
        self.ScheduledActionName = None
        self.MaxSize = None
        self.MinSize = None
        self.DesiredCapacity = None
        self.StartTime = None
        self.EndTime = None
        self.Recurrence = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.ScheduledActionName = params.get("ScheduledActionName")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Recurrence = params.get("Recurrence")


class CreateScheduledActionResponse(AbstractModel):
    """CreateScheduledAction返回参数结构体

    """

    def __init__(self):
        """
        :param ScheduledActionId: 定时任务ID
        :type ScheduledActionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ScheduledActionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ScheduledActionId = params.get("ScheduledActionId")
        self.RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """启动配置的数据盘配置信息。若不指定该参数，则默认不购买数据盘，当前仅支持购买的时候指定一个数据盘。

    """

    def __init__(self):
        """
        :param DiskType: 数据盘类型。数据盘类型限制详见[CVM实例配置](https://cloud.tencent.com/document/product/213/2177)。取值范围：<br><li>LOCAL_BASIC：本地硬盘<br><li>LOCAL_SSD：本地SSD硬盘<br><li>CLOUD_BASIC：普通云硬盘<br><li>CLOUD_PREMIUM：高性能云硬盘<br><li>CLOUD_SSD：SSD云硬盘<br><br>默认取值：LOCAL_BASIC。
        :type DiskType: str
        :param DiskSize: 数据盘大小，单位：GB。最小调整步长为10G，不同数据盘类型取值范围不同，具体限制详见：[CVM实例配置](https://cloud.tencent.com/document/product/213/2177)。默认值为0，表示不购买数据盘。更多限制详见产品文档。
        :type DiskSize: int
        :param SnapshotId: 数据盘快照 ID，类似 `snap-l8psqwnt`。
        :type SnapshotId: str
        """
        self.DiskType = None
        self.DiskSize = None
        self.SnapshotId = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.SnapshotId = params.get("SnapshotId")


class DeleteAutoScalingGroupRequest(AbstractModel):
    """DeleteAutoScalingGroup请求参数结构体

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        """
        self.AutoScalingGroupId = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")


class DeleteAutoScalingGroupResponse(AbstractModel):
    """DeleteAutoScalingGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLaunchConfigurationRequest(AbstractModel):
    """DeleteLaunchConfiguration请求参数结构体

    """

    def __init__(self):
        """
        :param LaunchConfigurationId: 需要删除的启动配置ID。
        :type LaunchConfigurationId: str
        """
        self.LaunchConfigurationId = None


    def _deserialize(self, params):
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")


class DeleteLaunchConfigurationResponse(AbstractModel):
    """DeleteLaunchConfiguration返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteScheduledActionRequest(AbstractModel):
    """DeleteScheduledAction请求参数结构体

    """

    def __init__(self):
        """
        :param ScheduledActionId: 待删除的定时任务ID。
        :type ScheduledActionId: str
        """
        self.ScheduledActionId = None


    def _deserialize(self, params):
        self.ScheduledActionId = params.get("ScheduledActionId")


class DeleteScheduledActionResponse(AbstractModel):
    """DeleteScheduledAction返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountLimitsRequest(AbstractModel):
    """DescribeAccountLimits请求参数结构体

    """


class DescribeAccountLimitsResponse(AbstractModel):
    """DescribeAccountLimits返回参数结构体

    """

    def __init__(self):
        """
        :param MaxNumberOfLaunchConfigurations: 用户账户被允许创建的启动配置最大数量
        :type MaxNumberOfLaunchConfigurations: int
        :param NumberOfLaunchConfigurations: 用户账户启动配置的当前数量
        :type NumberOfLaunchConfigurations: int
        :param MaxNumberOfAutoScalingGroups: 用户账户被允许创建的伸缩组最大数量
        :type MaxNumberOfAutoScalingGroups: int
        :param NumberOfAutoScalingGroups: 用户账户伸缩组的当前数量
        :type NumberOfAutoScalingGroups: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaxNumberOfLaunchConfigurations = None
        self.NumberOfLaunchConfigurations = None
        self.MaxNumberOfAutoScalingGroups = None
        self.NumberOfAutoScalingGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaxNumberOfLaunchConfigurations = params.get("MaxNumberOfLaunchConfigurations")
        self.NumberOfLaunchConfigurations = params.get("NumberOfLaunchConfigurations")
        self.MaxNumberOfAutoScalingGroups = params.get("MaxNumberOfAutoScalingGroups")
        self.NumberOfAutoScalingGroups = params.get("NumberOfAutoScalingGroups")
        self.RequestId = params.get("RequestId")


class DescribeAutoScalingActivitiesRequest(AbstractModel):
    """DescribeAutoScalingActivities请求参数结构体

    """

    def __init__(self):
        """
        :param ActivityIds: 按照一个或者多个伸缩活动ID查询。伸缩活动ID形如：`asa-5l2ejpfo`。每次请求的上限为100。参数不支持同时指定`ActivityIds`和`Filters`。
        :type ActivityIds: list of str
        :param Filters: 过滤条件。
<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>
<li> activity-status-code - String - 是否必填：否 -（过滤条件）按照伸缩活动状态过滤。（INIT：初始化中|RUNNING：运行中|SUCCESSFUL：活动成功|PARTIALLY_SUCCESSFUL：活动部分成功|FAILED：活动失败|CANCELLED：活动取消）</li>
<li> activity-type - String - 是否必填：否 -（过滤条件）按照伸缩活动类型过滤。（SCALE_OUT：扩容活动|SCALE_IN：缩容活动|ATTACH_INSTANCES：添加实例|REMOVE_INSTANCES：销毁实例|DETACH_INSTANCES：移出实例|TERMINATE_INSTANCES_UNEXPECTEDLY：实例在CVM控制台被销毁|REPLACE_UNHEALTHY_INSTANCE：替换不健康实例|UPDATE_LOAD_BALANCERS：更新负载均衡器）</li>
<li> activity-id - String - 是否必填：否 -（过滤条件）按照伸缩活动ID过滤。</li>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`ActivityIds`和`Filters`。
        :type Filters: list of Filter
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self.ActivityIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ActivityIds = params.get("ActivityIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeAutoScalingActivitiesResponse(AbstractModel):
    """DescribeAutoScalingActivities返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的伸缩活动数量。
        :type TotalCount: int
        :param ActivitySet: 符合条件的伸缩活动信息集合。
        :type ActivitySet: list of Activity
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ActivitySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ActivitySet") is not None:
            self.ActivitySet = []
            for item in params.get("ActivitySet"):
                obj = Activity()
                obj._deserialize(item)
                self.ActivitySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAutoScalingGroupsRequest(AbstractModel):
    """DescribeAutoScalingGroups请求参数结构体

    """

    def __init__(self):
        """
        :param AutoScalingGroupIds: 按照一个或者多个伸缩组ID查询。伸缩组ID形如：`asg-nkdwoui0`。每次请求的上限为100。参数不支持同时指定`AutoScalingGroups`和`Filters`。
        :type AutoScalingGroupIds: list of str
        :param Filters: 过滤条件。
<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>
<li> auto-scaling-group-name - String - 是否必填：否 -（过滤条件）按照伸缩组名称过滤。</li>
<li> launch-configuration-id - String - 是否必填：否 -（过滤条件）按照启动配置ID过滤。</li>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AutoScalingGroupIds`和`Filters`。
        :type Filters: list of Filter
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self.AutoScalingGroupIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeAutoScalingGroupsResponse(AbstractModel):
    """DescribeAutoScalingGroups返回参数结构体

    """

    def __init__(self):
        """
        :param AutoScalingGroupSet: 伸缩组详细信息列表。
        :type AutoScalingGroupSet: list of AutoScalingGroup
        :param TotalCount: 符合条件的伸缩组数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AutoScalingGroupSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AutoScalingGroupSet") is not None:
            self.AutoScalingGroupSet = []
            for item in params.get("AutoScalingGroupSet"):
                obj = AutoScalingGroup()
                obj._deserialize(item)
                self.AutoScalingGroupSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAutoScalingInstancesRequest(AbstractModel):
    """DescribeAutoScalingInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 待查询云服务器（CVM）的实例ID。参数不支持同时指定InstanceIds和Filters。
        :type InstanceIds: list of str
        :param Filters: 过滤条件。
<li> instance-id - String - 是否必填：否 -（过滤条件）按照实例ID过滤。</li>
<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`InstanceIds`和`Filters`。
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.InstanceIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAutoScalingInstancesResponse(AbstractModel):
    """DescribeAutoScalingInstances返回参数结构体

    """

    def __init__(self):
        """
        :param AutoScalingInstanceSet: 实例详细信息列表。
        :type AutoScalingInstanceSet: list of Instance
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AutoScalingInstanceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AutoScalingInstanceSet") is not None:
            self.AutoScalingInstanceSet = []
            for item in params.get("AutoScalingInstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self.AutoScalingInstanceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeLaunchConfigurationsRequest(AbstractModel):
    """DescribeLaunchConfigurations请求参数结构体

    """

    def __init__(self):
        """
        :param LaunchConfigurationIds: 按照一个或者多个启动配置ID查询。启动配置ID形如：`asc-ouy1ax38`。每次请求的上限为100。参数不支持同时指定`LaunchConfigurationIds`和`Filters`
        :type LaunchConfigurationIds: list of str
        :param Filters: 过滤条件。
<li> launch-configuration-id - String - 是否必填：否 -（过滤条件）按照启动配置ID过滤。</li>
<li> launch-configuration-name - String - 是否必填：否 -（过滤条件）按照启动配置名称过滤。</li>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`LaunchConfigurationIds`和`Filters`。
        :type Filters: list of Filter
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self.LaunchConfigurationIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.LaunchConfigurationIds = params.get("LaunchConfigurationIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeLaunchConfigurationsResponse(AbstractModel):
    """DescribeLaunchConfigurations返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的启动配置数量。
        :type TotalCount: int
        :param LaunchConfigurationSet: 启动配置详细信息列表。
        :type LaunchConfigurationSet: list of LaunchConfiguration
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LaunchConfigurationSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LaunchConfigurationSet") is not None:
            self.LaunchConfigurationSet = []
            for item in params.get("LaunchConfigurationSet"):
                obj = LaunchConfiguration()
                obj._deserialize(item)
                self.LaunchConfigurationSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeScheduledActionsRequest(AbstractModel):
    """DescribeScheduledActions请求参数结构体

    """

    def __init__(self):
        """
        :param ScheduledActionIds: 按照一个或者多个定时任务ID查询。实例ID形如：asst-am691zxo。每次请求的实例的上限为100。参数不支持同时指定ScheduledActionIds和Filters。
        :type ScheduledActionIds: list of str
        :param Filters: 过滤条件。
<li> scheduled-action-id - String - 是否必填：否 -（过滤条件）按照定时任务ID过滤。</li>
<li> scheduled-action-name - String - 是否必填：否 - （过滤条件） 按照定时任务名称过滤。</li>
<li> auto-scaling-group-id - String - 是否必填：否 - （过滤条件） 按照伸缩组ID过滤。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.ScheduledActionIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ScheduledActionIds = params.get("ScheduledActionIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeScheduledActionsResponse(AbstractModel):
    """DescribeScheduledActions返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的定时任务数量。
        :type TotalCount: int
        :param ScheduledActionSet: 定时任务详细信息列表。
        :type ScheduledActionSet: list of ScheduledAction
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ScheduledActionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ScheduledActionSet") is not None:
            self.ScheduledActionSet = []
            for item in params.get("ScheduledActionSet"):
                obj = ScheduledAction()
                obj._deserialize(item)
                self.ScheduledActionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DetachInstancesRequest(AbstractModel):
    """DetachInstances请求参数结构体

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param InstanceIds: CVM实例ID列表
        :type InstanceIds: list of str
        """
        self.AutoScalingGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.InstanceIds = params.get("InstanceIds")


class DetachInstancesResponse(AbstractModel):
    """DetachInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableAutoScalingGroupRequest(AbstractModel):
    """DisableAutoScalingGroup请求参数结构体

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        """
        self.AutoScalingGroupId = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")


class DisableAutoScalingGroupResponse(AbstractModel):
    """DisableAutoScalingGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableAutoScalingGroupRequest(AbstractModel):
    """EnableAutoScalingGroup请求参数结构体

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        """
        self.AutoScalingGroupId = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")


class EnableAutoScalingGroupResponse(AbstractModel):
    """EnableAutoScalingGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnhancedService(AbstractModel):
    """描述了实例的增强服务启用情况与其设置，如云安全，云监控等实例 Agent。

    """

    def __init__(self):
        """
        :param SecurityService: 开启云安全服务。若不指定该参数，则默认开启云安全服务。
        :type SecurityService: :class:`tencentcloud.autoscaling.v20180419.models.RunSecurityServiceEnabled`
        :param MonitorService: 开启云监控服务。若不指定该参数，则默认开启云监控服务。
        :type MonitorService: :class:`tencentcloud.autoscaling.v20180419.models.RunMonitorServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))


class Filter(AbstractModel):
    """>描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >
    > 以[DescribeInstances](https://cloud.tencent.com/document/api/213/9388)接口的`Filter`为例。若我们需要查询可用区（`zone`）为广州一区 ***并且*** 实例计费模式（`instance-charge-type`）为包年包月 ***或者*** 按量计费的实例时，可如下实现：
    ```
    Filters.1.Name=zone
    &Filters.1.Values.1=ap-guangzhou-1
    &Filters.2.Name=instance-charge-type
    &Filters.2.Values.1=PREPAID
    &Filters.3.Values.2=POSTPAID_BY_HOUR
    ```

    """

    def __init__(self):
        """
        :param Name: 需要过滤的字段。
        :type Name: str
        :param Values: 字段的过滤值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class ForwardLoadBalancer(AbstractModel):
    """应用型负载均衡器

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡器ID
        :type LoadBalancerId: str
        :param ListenerId: 应用型负载均衡监听器 ID
        :type ListenerId: str
        :param TargetAttributes: 目标规则属性列表
        :type TargetAttributes: list of TargetAttribute
        :param LocationId: 转发规则ID
        :type LocationId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.TargetAttributes = None
        self.LocationId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("TargetAttributes") is not None:
            self.TargetAttributes = []
            for item in params.get("TargetAttributes"):
                obj = TargetAttribute()
                obj._deserialize(item)
                self.TargetAttributes.append(obj)
        self.LocationId = params.get("LocationId")


class Instance(AbstractModel):
    """实例信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param LaunchConfigurationId: 启动配置ID
        :type LaunchConfigurationId: str
        :param LaunchConfigurationName: 启动配置名称
        :type LaunchConfigurationName: str
        :param LifeCycleState: 生命周期状态，取值包括IN_SERVICE, CREATING, TERMINATING, ATTACHING, DETACHING, ATTACHING_LB, DETACHING_LB等
        :type LifeCycleState: str
        :param HealthStatus: 健康状态，取值包括HEALTHY和UNHEALTHY
        :type HealthStatus: str
        :param ProtectedFromScaleIn: 是否加入缩容保护
        :type ProtectedFromScaleIn: bool
        :param Zone: 可用区
        :type Zone: str
        :param CreationType: 创建类型，取值包括AUTO_CREATION, MANUAL_ATTACHING。
        :type CreationType: str
        :param AddTime: 实例加入时间
        :type AddTime: str
        :param InstanceType: 实例类型
        :type InstanceType: str
        """
        self.InstanceId = None
        self.AutoScalingGroupId = None
        self.LaunchConfigurationId = None
        self.LaunchConfigurationName = None
        self.LifeCycleState = None
        self.HealthStatus = None
        self.ProtectedFromScaleIn = None
        self.Zone = None
        self.CreationType = None
        self.AddTime = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        self.LifeCycleState = params.get("LifeCycleState")
        self.HealthStatus = params.get("HealthStatus")
        self.ProtectedFromScaleIn = params.get("ProtectedFromScaleIn")
        self.Zone = params.get("Zone")
        self.CreationType = params.get("CreationType")
        self.AddTime = params.get("AddTime")
        self.InstanceType = params.get("InstanceType")


class InstanceMarketOptionsRequest(AbstractModel):
    """CVM竞价请求相关选项

    """

    def __init__(self):
        """
        :param SpotOptions: 竞价相关选项
        :type SpotOptions: :class:`tencentcloud.autoscaling.v20180419.models.SpotMarketOptions`
        :param MarketType: 市场选项类型，当前只支持取值：spot
        :type MarketType: str
        """
        self.SpotOptions = None
        self.MarketType = None


    def _deserialize(self, params):
        if params.get("SpotOptions") is not None:
            self.SpotOptions = SpotMarketOptions()
            self.SpotOptions._deserialize(params.get("SpotOptions"))
        self.MarketType = params.get("MarketType")


class InternetAccessible(AbstractModel):
    """描述了启动配置创建实例的公网可访问性，声明了实例的公网使用计费模式，最大带宽等

    """

    def __init__(self):
        """
        :param InternetChargeType: 网络计费类型。取值范围：<br><li>BANDWIDTH_PREPAID：预付费按带宽结算<br><li>TRAFFIC_POSTPAID_BY_HOUR：流量按小时后付费<br><li>BANDWIDTH_POSTPAID_BY_HOUR：带宽按小时后付费<br><li>BANDWIDTH_PACKAGE：带宽包用户<br>默认取值：TRAFFIC_POSTPAID_BY_HOUR。
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: 公网出带宽上限，单位：Mbps。默认值：0Mbps。不同机型带宽上限范围不一致，具体限制详见[购买网络带宽](https://cloud.tencent.com/document/product/213/509)。
        :type InternetMaxBandwidthOut: int
        :param PublicIpAssigned: 是否分配公网IP。取值范围：<br><li>TRUE：表示分配公网IP<br><li>FALSE：表示不分配公网IP<br><br>当公网带宽大于0Mbps时，可自由选择开通与否，默认开通公网IP；当公网带宽为0，则不允许分配公网IP。
        :type PublicIpAssigned: bool
        """
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.PublicIpAssigned = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.PublicIpAssigned = params.get("PublicIpAssigned")


class LaunchConfiguration(AbstractModel):
    """符合条件的启动配置信息的集合。

    """

    def __init__(self):
        """
        :param ProjectId: 实例所属项目ID。
        :type ProjectId: int
        :param LaunchConfigurationId: 启动配置ID。
        :type LaunchConfigurationId: str
        :param LaunchConfigurationName: 启动配置名称。
        :type LaunchConfigurationName: str
        :param InstanceType: 实例机型。
        :type InstanceType: str
        :param SystemDisk: 实例系统盘配置信息。
        :type SystemDisk: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        :param DataDisks: 实例数据盘配置信息。
        :type DataDisks: list of DataDisk
        :param LoginSettings: 实例登录设置。
        :type LoginSettings: :class:`tencentcloud.autoscaling.v20180419.models.LimitedLoginSettings`
        :param InternetAccessible: 公网带宽相关信息设置。
        :type InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        :param SecurityGroupIds: 实例所属安全组。
        :type SecurityGroupIds: list of str
        :param AutoScalingGroupAbstractSet: 启动配置关联的伸缩组。
        :type AutoScalingGroupAbstractSet: list of AutoScalingGroupAbstract
        :param UserData: 自定义数据。
        :type UserData: str
        :param CreatedTime: 启动配置创建时间。
        :type CreatedTime: str
        :param EnhancedService: 实例的增强服务启用情况与其设置。
        :type EnhancedService: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        :param ImageId: 镜像ID。
        :type ImageId: str
        :param LaunchConfigurationStatus: 启动配置当前状态。取值范围：<br><li>NORMAL：正常<br><li>IMAGE_ABNORMAL：启动配置镜像异常<br><li>CBS_SNAP_ABNORMAL：启动配置数据盘快照异常<br><li>SECURITY_GROUP_ABNORMAL：启动配置安全组异常<br>
        :type LaunchConfigurationStatus: str
        :param InstanceChargeType: 实例计费类型，CVM默认值按照POSTPAID_BY_HOUR处理。
<br><li>POSTPAID_BY_HOUR：按小时后付费
<br><li>SPOTPAID：竞价付费
        :type InstanceChargeType: str
        :param InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数，若指定实例的付费模式为竞价付费则该参数必传。
        :type InstanceMarketOptions: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param InstanceTypes: 实例机型列表。
        :type InstanceTypes: list of str
        """
        self.ProjectId = None
        self.LaunchConfigurationId = None
        self.LaunchConfigurationName = None
        self.InstanceType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.LoginSettings = None
        self.InternetAccessible = None
        self.SecurityGroupIds = None
        self.AutoScalingGroupAbstractSet = None
        self.UserData = None
        self.CreatedTime = None
        self.EnhancedService = None
        self.ImageId = None
        self.LaunchConfigurationStatus = None
        self.InstanceChargeType = None
        self.InstanceMarketOptions = None
        self.InstanceTypes = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LimitedLoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("AutoScalingGroupAbstractSet") is not None:
            self.AutoScalingGroupAbstractSet = []
            for item in params.get("AutoScalingGroupAbstractSet"):
                obj = AutoScalingGroupAbstract()
                obj._deserialize(item)
                self.AutoScalingGroupAbstractSet.append(obj)
        self.UserData = params.get("UserData")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.ImageId = params.get("ImageId")
        self.LaunchConfigurationStatus = params.get("LaunchConfigurationStatus")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.InstanceTypes = params.get("InstanceTypes")


class LimitedLoginSettings(AbstractModel):
    """描述了实例登录相关配置与信息，出于安全性考虑，不会描述敏感信息。

    """

    def __init__(self):
        """
        :param KeyIds: 密钥ID列表。
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")


class LoginSettings(AbstractModel):
    """描述了实例登录相关配置与信息。

    """

    def __init__(self):
        """
        :param Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：<br><li>Linux实例密码必须8到16位，至少包括两项[a-z，A-Z]、[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? / ]中的特殊符号。<br><li>Windows实例密码必须12到16位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]中的特殊符号。<br><br>若不指定该参数，则由系统随机生成密码，并通过站内信方式通知到用户。
        :type Password: str
        :param KeyIds: 密钥ID列表。关联密钥后，就可以通过对应的私钥来访问实例；KeyId可通过接口DescribeKeyPairs获取，密钥与密码不能同时指定，同时Windows操作系统不支持指定密钥。当前仅支持购买的时候指定一个密钥。
        :type KeyIds: list of str
        :param KeepImageLogin: 保持镜像的原始设置。该参数与Password或KeyIds.N不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为TRUE。取值范围：<br><li>TRUE：表示保持镜像的登录设置<br><li>FALSE：表示不保持镜像的登录设置<br><br>默认取值：FALSE。
        :type KeepImageLogin: bool
        """
        self.Password = None
        self.KeyIds = None
        self.KeepImageLogin = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.KeyIds = params.get("KeyIds")
        self.KeepImageLogin = params.get("KeepImageLogin")


class ModifyAutoScalingGroupRequest(AbstractModel):
    """ModifyAutoScalingGroup请求参数结构体

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param AutoScalingGroupName: 伸缩组名称，在您账号中必须唯一。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超55个字节。
        :type AutoScalingGroupName: str
        :param DefaultCooldown: 默认冷却时间，单位秒，默认值为300
        :type DefaultCooldown: int
        :param DesiredCapacity: 期望实例数，大小介于最小实例数和最大实例数之间
        :type DesiredCapacity: int
        :param LaunchConfigurationId: 启动配置ID
        :type LaunchConfigurationId: str
        :param MaxSize: 最大实例数，取值范围为0-2000。
        :type MaxSize: int
        :param MinSize: 最小实例数，取值范围为0-2000。
        :type MinSize: int
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param SubnetIds: 子网ID列表
        :type SubnetIds: list of str
        :param TerminationPolicies: 销毁策略，目前长度上限为1。取值包括 OLDEST_INSTANCE 和 NEWEST_INSTANCE。
<br><li> OLDEST_INSTANCE 优先销毁伸缩组中最旧的实例。
<br><li> NEWEST_INSTANCE，优先销毁伸缩组中最新的实例。
        :type TerminationPolicies: list of str
        :param VpcId: VPC ID，基础网络则填空字符串。修改为具体VPC ID时，需指定相应的SubnetIds；修改为基础网络时，需指定相应的Zones。
        :type VpcId: str
        :param Zones: 可用区列表
        :type Zones: list of str
        :param RetryPolicy: 重试策略，取值包括 IMMEDIATE_RETRY 和 INCREMENTAL_INTERVALS，默认取值为 IMMEDIATE_RETRY。
<br><li> IMMEDIATE_RETRY，立即重试，在较短时间内快速重试，连续失败超过一定次数（5次）后不再重试。
<br><li> INCREMENTAL_INTERVALS，间隔递增重试，随着连续失败次数的增加，重试间隔逐渐增大，重试间隔从秒级到1天不等。
        :type RetryPolicy: str
        :param ZonesCheckPolicy: 可用区校验策略，取值包括 ALL 和 ANY，默认取值为ANY。在伸缩组实际变更资源相关字段时（启动配置、可用区、子网）发挥作用。
<br><li> ALL，所有可用区（Zone）或子网（SubnetId）都可用则通过校验，否则校验报错。
<br><li> ANY，存在任何一个可用区（Zone）或子网（SubnetId）可用则通过校验，否则校验报错。

可用区或子网不可用的常见原因包括该可用区CVM实例类型售罄、该可用区CBS云盘售罄、该可用区配额不足、该子网IP不足等。
如果 Zones/SubnetIds 中可用区或者子网不存在，则无论 ZonesCheckPolicy 采用何种取值，都会校验报错。
        :type ZonesCheckPolicy: str
        """
        self.AutoScalingGroupId = None
        self.AutoScalingGroupName = None
        self.DefaultCooldown = None
        self.DesiredCapacity = None
        self.LaunchConfigurationId = None
        self.MaxSize = None
        self.MinSize = None
        self.ProjectId = None
        self.SubnetIds = None
        self.TerminationPolicies = None
        self.VpcId = None
        self.Zones = None
        self.RetryPolicy = None
        self.ZonesCheckPolicy = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.AutoScalingGroupName = params.get("AutoScalingGroupName")
        self.DefaultCooldown = params.get("DefaultCooldown")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.ProjectId = params.get("ProjectId")
        self.SubnetIds = params.get("SubnetIds")
        self.TerminationPolicies = params.get("TerminationPolicies")
        self.VpcId = params.get("VpcId")
        self.Zones = params.get("Zones")
        self.RetryPolicy = params.get("RetryPolicy")
        self.ZonesCheckPolicy = params.get("ZonesCheckPolicy")


class ModifyAutoScalingGroupResponse(AbstractModel):
    """ModifyAutoScalingGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDesiredCapacityRequest(AbstractModel):
    """ModifyDesiredCapacity请求参数结构体

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param DesiredCapacity: 期望实例数
        :type DesiredCapacity: int
        """
        self.AutoScalingGroupId = None
        self.DesiredCapacity = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.DesiredCapacity = params.get("DesiredCapacity")


class ModifyDesiredCapacityResponse(AbstractModel):
    """ModifyDesiredCapacity返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLaunchConfigurationAttributesRequest(AbstractModel):
    """ModifyLaunchConfigurationAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param LaunchConfigurationId: 启动配置ID
        :type LaunchConfigurationId: str
        :param ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-8toqc6s3`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>
        :type ImageId: str
        :param InstanceTypes: 实例类型列表，不同实例机型指定了不同的资源规格，最多支持5种实例机型。
启动配置，通过 InstanceType 表示单一实例类型，通过 InstanceTypes 表示多实例类型。指定 InstanceTypes 成功启动配置后，原有的 InstanceType 自动失效。
        :type InstanceTypes: list of str
        :param InstanceTypesCheckPolicy: 实例类型校验策略，在实际修改 InstanceTypes 时发挥作用，取值包括 ALL 和 ANY，默认取值为ANY。
<br><li> ALL，所有实例类型（InstanceType）都可用则通过校验，否则校验报错。
<br><li> ANY，存在任何一个实例类型（InstanceType）可用则通过校验，否则校验报错。

实例类型不可用的常见原因包括该实例类型售罄、对应云盘售罄等。
如果 InstanceTypes 中一款机型不存在或者已下线，则无论 InstanceTypesCheckPolicy 采用何种取值，都会校验报错。
        :type InstanceTypesCheckPolicy: str
        :param LaunchConfigurationName: 启动配置显示名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。
        :type LaunchConfigurationName: str
        :param UserData: 经过 Base64 编码后的自定义数据，最大长度不超过16KB。如果要清空UserData，则指定其为空字符串''
        :type UserData: str
        """
        self.LaunchConfigurationId = None
        self.ImageId = None
        self.InstanceTypes = None
        self.InstanceTypesCheckPolicy = None
        self.LaunchConfigurationName = None
        self.UserData = None


    def _deserialize(self, params):
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.ImageId = params.get("ImageId")
        self.InstanceTypes = params.get("InstanceTypes")
        self.InstanceTypesCheckPolicy = params.get("InstanceTypesCheckPolicy")
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        self.UserData = params.get("UserData")


class ModifyLaunchConfigurationAttributesResponse(AbstractModel):
    """ModifyLaunchConfigurationAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancersRequest(AbstractModel):
    """ModifyLoadBalancers请求参数结构体

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param LoadBalancerIds: 传统负载均衡器ID列表，目前长度上限为1，LoadBalancerIds 和 ForwardLoadBalancers 二者同时最多只能指定一个
        :type LoadBalancerIds: list of str
        :param ForwardLoadBalancers: 应用型负载均衡器列表，目前长度上限为1，LoadBalancerIds 和 ForwardLoadBalancers 二者同时最多只能指定一个
        :type ForwardLoadBalancers: list of ForwardLoadBalancer
        """
        self.AutoScalingGroupId = None
        self.LoadBalancerIds = None
        self.ForwardLoadBalancers = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        if params.get("ForwardLoadBalancers") is not None:
            self.ForwardLoadBalancers = []
            for item in params.get("ForwardLoadBalancers"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self.ForwardLoadBalancers.append(obj)


class ModifyLoadBalancersResponse(AbstractModel):
    """ModifyLoadBalancers返回参数结构体

    """

    def __init__(self):
        """
        :param ActivityId: 伸缩活动ID
        :type ActivityId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ActivityId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.RequestId = params.get("RequestId")


class ModifyScheduledActionRequest(AbstractModel):
    """ModifyScheduledAction请求参数结构体

    """

    def __init__(self):
        """
        :param ScheduledActionId: 待修改的定时任务ID
        :type ScheduledActionId: str
        :param ScheduledActionName: 定时任务名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。同一伸缩组下必须唯一。
        :type ScheduledActionName: str
        :param MaxSize: 当定时任务触发时，设置的伸缩组最大实例数。
        :type MaxSize: int
        :param MinSize: 当定时任务触发时，设置的伸缩组最小实例数。
        :type MinSize: int
        :param DesiredCapacity: 当定时任务触发时，设置的伸缩组期望实例数。
        :type DesiredCapacity: int
        :param StartTime: 定时任务的首次触发时间，取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。
        :type StartTime: str
        :param EndTime: 定时任务的结束时间，取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。<br>此参数与`Recurrence`需要同时指定，到达结束时间之后，定时任务将不再生效。
        :type EndTime: str
        :param Recurrence: 定时任务的重复方式。为标准[Cron](https://zh.wikipedia.org/wiki/Cron)格式<br>此参数与`EndTime`需要同时指定。
        :type Recurrence: str
        """
        self.ScheduledActionId = None
        self.ScheduledActionName = None
        self.MaxSize = None
        self.MinSize = None
        self.DesiredCapacity = None
        self.StartTime = None
        self.EndTime = None
        self.Recurrence = None


    def _deserialize(self, params):
        self.ScheduledActionId = params.get("ScheduledActionId")
        self.ScheduledActionName = params.get("ScheduledActionName")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Recurrence = params.get("Recurrence")


class ModifyScheduledActionResponse(AbstractModel):
    """ModifyScheduledAction返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveInstancesRequest(AbstractModel):
    """RemoveInstances请求参数结构体

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param InstanceIds: CVM实例ID列表
        :type InstanceIds: list of str
        """
        self.AutoScalingGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.InstanceIds = params.get("InstanceIds")


class RemoveInstancesResponse(AbstractModel):
    """RemoveInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunMonitorServiceEnabled(AbstractModel):
    """描述了 “云监控” 服务相关的信息。

    """

    def __init__(self):
        """
        :param Enabled: 是否开启[云监控](https://cloud.tencent.com/document/product/248)服务。取值范围：<br><li>TRUE：表示开启云监控服务<br><li>FALSE：表示不开启云监控服务<br><br>默认取值：TRUE。
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


class RunSecurityServiceEnabled(AbstractModel):
    """描述了 “云安全” 服务相关的信息

    """

    def __init__(self):
        """
        :param Enabled: 是否开启[云安全](https://cloud.tencent.com/document/product/296)服务。取值范围：<br><li>TRUE：表示开启云安全服务<br><li>FALSE：表示不开启云安全服务<br><br>默认取值：TRUE。
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


class ScheduledAction(AbstractModel):
    """描述定时任务的信息

    """

    def __init__(self):
        """
        :param ScheduledActionId: 定时任务ID。
        :type ScheduledActionId: str
        :param ScheduledActionName: 定时任务名称。
        :type ScheduledActionName: str
        :param AutoScalingGroupId: 定时任务所在伸缩组ID。
        :type AutoScalingGroupId: str
        :param StartTime: 定时任务的开始时间。取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。
        :type StartTime: str
        :param Recurrence: 定时任务的重复方式。
        :type Recurrence: str
        :param EndTime: 定时任务的结束时间。取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。
        :type EndTime: str
        :param MaxSize: 定时任务设置的最大实例数。
        :type MaxSize: int
        :param DesiredCapacity: 定时任务设置的期望实例数。
        :type DesiredCapacity: int
        :param MinSize: 定时任务设置的最小实例数。
        :type MinSize: int
        :param CreatedTime: 定时任务的创建时间。取值为`UTC`时间，按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ssZ`。
        :type CreatedTime: str
        """
        self.ScheduledActionId = None
        self.ScheduledActionName = None
        self.AutoScalingGroupId = None
        self.StartTime = None
        self.Recurrence = None
        self.EndTime = None
        self.MaxSize = None
        self.DesiredCapacity = None
        self.MinSize = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ScheduledActionId = params.get("ScheduledActionId")
        self.ScheduledActionName = params.get("ScheduledActionName")
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.StartTime = params.get("StartTime")
        self.Recurrence = params.get("Recurrence")
        self.EndTime = params.get("EndTime")
        self.MaxSize = params.get("MaxSize")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.MinSize = params.get("MinSize")
        self.CreatedTime = params.get("CreatedTime")


class SpotMarketOptions(AbstractModel):
    """竞价相关选项

    """

    def __init__(self):
        """
        :param MaxPrice: 竞价出价，例如“1.05”
        :type MaxPrice: str
        :param SpotInstanceType: 竞价请求类型，当前仅支持类型：one-time，默认值为one-time
        :type SpotInstanceType: str
        """
        self.MaxPrice = None
        self.SpotInstanceType = None


    def _deserialize(self, params):
        self.MaxPrice = params.get("MaxPrice")
        self.SpotInstanceType = params.get("SpotInstanceType")


class SystemDisk(AbstractModel):
    """启动配置的系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。

    """

    def __init__(self):
        """
        :param DiskType: 系统盘类型。系统盘类型限制详见[CVM实例配置](https://cloud.tencent.com/document/product/213/2177)。取值范围：<br><li>LOCAL_BASIC：本地硬盘<br><li>LOCAL_SSD：本地SSD硬盘<br><li>CLOUD_BASIC：普通云硬盘<br><li>CLOUD_PREMIUM：高性能云硬盘<br><li>CLOUD_SSD：SSD云硬盘<br><br>默认取值：LOCAL_BASIC。
        :type DiskType: str
        :param DiskSize: 系统盘大小，单位：GB。默认值为 50
        :type DiskSize: int
        """
        self.DiskType = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")


class TargetAttribute(AbstractModel):
    """负载均衡器目标属性

    """

    def __init__(self):
        """
        :param Port: 端口
        :type Port: int
        :param Weight: 权重
        :type Weight: int
        """
        self.Port = None
        self.Weight = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")