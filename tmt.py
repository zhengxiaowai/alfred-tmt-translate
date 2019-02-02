#!/bin/evn python
# coding=utf-8

import json
import re

from workflow import Workflow
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.tmt.v20180321 import tmt_client, models


class ICON(object):
    DEFAULT = 'icon.png'
    SOUND = 'sound.png'
    G_TRANSLATE = 'gtranslate.png'


class TMTConfig(object):
    ENDPOINT = "tmt.tencentcloudapi.com"


def create_tmt_client(tc_config):
    cred = credential.Credential(tc_config.KEY, tc_config.SECRET)
    http_profile = HttpProfile()
    http_profile.endpoint = TMTConfig.ENDPOINT

    client_profile = ClientProfile()
    client_profile.httpProfile = http_profile
    client = tmt_client.TmtClient(cred, "ap-beijing", client_profile)
    return client


def translate_text(client, text, target):
    req = models.TextTranslateRequest()
    params = {
        "SourceText": text.encode("utf8"),
        "Source": "auto",
        "Target": target,
        "ProjectId": 0
    }
    req.from_json_string(json.dumps(params))
    resp = client.TextTranslate(req)

    return resp.TargetText


def is_chinese(text):
    return len(re.findall(ur'[\u4e00-\u9fff]+', text)) == 0


def main(text, tc_config):
    wf = Workflow()
    try:
        client = create_tmt_client(tc_config)

        text = text.decode('utf8')
        target = 'zh' if is_chinese(text) else 'en'
        result = translate_text(client, text, target)
    except Exception as err:
        result = err
        target = 'unknown'

    wf.add_item(
        title=unicode(result),
        subtitle=u"复制到剪切板",
        valid=True,
        arg=unicode(result),
        icon=ICON.DEFAULT
    )

    if target == 'en':
        wf.add_item(
            title=unicode(result),
            subtitle=u"ctrl 听发音",
            valid=True,
            arg=unicode(result),
            icon=ICON.SOUND
        )

    wf.send_feedback()
