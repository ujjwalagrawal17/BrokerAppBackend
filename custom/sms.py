import requests
from .models import keys

def send_sms(mobile,msg,sender="Broker"):
	authkey=str(keys.objects.get(key="msg91").value)
	url='http://api.msg91.com/api/sendhttp.php?authkey='+authkey+'&mobiles='
	url+=mobile
	url+='&message='+msg
	url+='&sender='+sender+'&route=4'
	print url
	print requests.request("GET",url)
	
	

