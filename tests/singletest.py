from __future__ import print_function
import time
import workgroup_assistant_api_client
from workgroup_assistant_api_client.rest import ApiException
from workgroup_assistant_api_client.configuration import Configuration
from pprint import pprint

# create an instance of the API class
configuration = Configuration()
<<<<<<< Updated upstream
docker_container = "localhost"
server_port = "4042"
=======
host_container = "localhost"
server_port = "9504"
server_port_mock = "4042"
>>>>>>> Stashed changes
namespace = '/v1/gss'
configuration.host = 'http://' + docker_container + ':' + server_port + '' + namespace
api_instance = workgroup_assistant_api_client.DefaultApi(workgroup_assistant_api_client.ApiClient(configuration))
name = "testuser" # object | 
password = "testpass" # object | 
inviter_default_app_id = "" # object |  (optional)
inviter_user_role = "" # object |  (optional)

try:
    # Submit a login with user credential payload for group member with existing AI service agent
    api_instance.execute_login_post(name=name, password=password, inviter_default_app_id=inviter_default_app_id, inviter_user_role=inviter_user_role)
except ApiException as e:
    print("Exception when calling DefaultApi->execute_login_post: %s\n" % e)