from rest_framework.response import Response
from rest_framework.views import APIView
from ipware import get_client_ip
import json,urllib


class LocationAPI(APIView):
    def get(self,request,courseid,format=None):
        client_ip,is_routable=get_client_ip(request)
        if client_ip is None:
            client_ip="0.0.0.0"
        else:
            if is_routable:
                ip_type="public"
            else:
                ip_type="private"
            print(client_ip,ip_type)
            ip_address=courseid
            url="https://api.ipfind.com/?ip="+ip_address
            respon=urllib.request.urlopen(url)
            data1=json.loads(respon.read())
            data1['client_ip']=client_ip
            data1['ip_type']=ip_type
            return Response(data1)
            
    
        