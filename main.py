from aliyunsdkcore import client
from aliyunsdkafs.request.v20180112 import AuthenticateSigRequest
from aliyunsdkcore.profile import region_provider
region_provider.add_endpoint('afs', 'cn-hangzhou', 'afs.aliyuncs.com')
import os

accessKey = os.environ['ACCESS_KEY']
accessSecret = os.environ['ACCESS_SECRET']

print("ACCESS_KEY:", accessKey)
print("ACCESS_SECRET:", accessSecret)
print()

def lambda_handler(event, context):
# YOUR ACCESS_KEY、YOUR ACCESS_SECRET请替换成您的阿里云accesskey id和secret
    clt = client.AcsClient(accessKey, accessSecret, 'cn-hangzhou')
    request = AuthenticateSigRequest.AuthenticateSigRequest()

    sessionID = event['sessionID']
    print("sessionID:", sessionID)

    sig = event['sig']
    print("sig:", sig)

    token = event['token']
    print("token:", token)

    scene = event['scene']
    print("scene:", scene)

    appKey = event['appKey']
    print("appKey:", appKey)

    remoteIP = event['remoteIP']
    print("remoteIP:", remoteIP)
    print()

#必填参数：从前端获取，不可更改
    request.set_SessionId(sessionID)
#必填参数：从前端获取，不可更改，android和ios只变更这个参数即可，下面参数不变保留xxx
    request.set_Sig(sig)
#必填参数：从前端获取，不可更改
    request.set_Token(token)
#必填参数：从前端获取，不可更改
    request.set_Scene(scene)
#必填参数：后端填写
    request.set_AppKey(appKey)
#必填参数：后端填写
    request.set_RemoteIp(remoteIP)

    result = clt.do_action_with_exception(request)#返回code 100表示验签通过，900表示验签失败
    print(result)
    return result
