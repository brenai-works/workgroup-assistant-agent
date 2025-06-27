# workgroup_assistant_api_client.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_login_post**](DefaultApi.md#execute_login_post) | **POST** /execute-login | Submit a login with user credential payload for group member with existing AI service agent
[**execute_logout_post**](DefaultApi.md#execute_logout_post) | **POST** /execute-logout | Load logout payload as group member for existing AI service agent
[**execute_signup_post**](DefaultApi.md#execute_signup_post) | **POST** /execute-signup | Commit a new sign-up application payload for group member with new AI service agent onto Researcher Hub
[**load_login_post**](DefaultApi.md#load_login_post) | **POST** /load-login | Load login payload as group member for existing AI service agent
[**load_members_profile_post**](DefaultApi.md#load_members_profile_post) | **POST** /load-members-profile | Get member&#39;s profile and voting preferences of AI service agent
[**load_signup_post**](DefaultApi.md#load_signup_post) | **POST** /load-signup | Load sign-up application payload as group member for new AI service agent
[**load_workgroup_post**](DefaultApi.md#load_workgroup_post) | **POST** /load-workgroup | Get workgroup for AI service agent


# **execute_login_post**
> execute_login_post(name, password, inviter_default_app_id=inviter_default_app_id, inviter_user_role=inviter_user_role)

Submit a login with user credential payload for group member with existing AI service agent

### Example
```python
from __future__ import print_function
import time
import workgroup_assistant_api_client
from workgroup_assistant_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = workgroup_assistant_api_client.DefaultApi()
name = 'name_example' # str | 
password = 'password_example' # str | 
inviter_default_app_id = 'inviter_default_app_id_example' # str |  (optional)
inviter_user_role = 'inviter_user_role_example' # str |  (optional)

try:
    # Submit a login with user credential payload for group member with existing AI service agent
    api_instance.execute_login_post(name, password, inviter_default_app_id=inviter_default_app_id, inviter_user_role=inviter_user_role)
except ApiException as e:
    print("Exception when calling DefaultApi->execute_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **password** | **str**|  | 
 **inviter_default_app_id** | **str**|  | [optional] 
 **inviter_user_role** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_logout_post**
> execute_logout_post()

Load logout payload as group member for existing AI service agent

### Example
```python
from __future__ import print_function
import time
import workgroup_assistant_api_client
from workgroup_assistant_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = workgroup_assistant_api_client.DefaultApi()

try:
    # Load logout payload as group member for existing AI service agent
    api_instance.execute_logout_post()
except ApiException as e:
    print("Exception when calling DefaultApi->execute_logout_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_signup_post**
> execute_signup_post(avatar, name, email, password, slackname, researchgate, default_app_id, default_app_description)

Commit a new sign-up application payload for group member with new AI service agent onto Researcher Hub

### Example
```python
from __future__ import print_function
import time
import workgroup_assistant_api_client
from workgroup_assistant_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = workgroup_assistant_api_client.DefaultApi()
avatar = 'avatar_example' # str | 
name = 'name_example' # str | 
email = 'email_example' # str | 
password = 'password_example' # str | 
slackname = 'slackname_example' # str | 
researchgate = 'researchgate_example' # str | 
default_app_id = 'default_app_id_example' # str | 
default_app_description = 'default_app_description_example' # str | 

try:
    # Commit a new sign-up application payload for group member with new AI service agent onto Researcher Hub
    api_instance.execute_signup_post(avatar, name, email, password, slackname, researchgate, default_app_id, default_app_description)
except ApiException as e:
    print("Exception when calling DefaultApi->execute_signup_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatar** | **str**|  | 
 **name** | **str**|  | 
 **email** | **str**|  | 
 **password** | **str**|  | 
 **slackname** | **str**|  | 
 **researchgate** | **str**|  | 
 **default_app_id** | **str**|  | 
 **default_app_description** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_login_post**
> load_login_post(id, inviteremail=inviteremail, inviter_default_app_id=inviter_default_app_id, inviter_user_role=inviter_user_role)

Load login payload as group member for existing AI service agent

### Example
```python
from __future__ import print_function
import time
import workgroup_assistant_api_client
from workgroup_assistant_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = workgroup_assistant_api_client.DefaultApi()
id = 56 # int | 
inviteremail = 'inviteremail_example' # str |  (optional)
inviter_default_app_id = 'inviter_default_app_id_example' # str |  (optional)
inviter_user_role = 'inviter_user_role_example' # str |  (optional)

try:
    # Load login payload as group member for existing AI service agent
    api_instance.load_login_post(id, inviteremail=inviteremail, inviter_default_app_id=inviter_default_app_id, inviter_user_role=inviter_user_role)
except ApiException as e:
    print("Exception when calling DefaultApi->load_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **inviteremail** | **str**|  | [optional] 
 **inviter_default_app_id** | **str**|  | [optional] 
 **inviter_user_role** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_members_profile_post**
> load_members_profile_post(id)

Get member's profile and voting preferences of AI service agent

### Example
```python
from __future__ import print_function
import time
import workgroup_assistant_api_client
from workgroup_assistant_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = workgroup_assistant_api_client.DefaultApi()
id = 56 # int | 

try:
    # Get member's profile and voting preferences of AI service agent
    api_instance.load_members_profile_post(id)
except ApiException as e:
    print("Exception when calling DefaultApi->load_members_profile_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_signup_post**
> load_signup_post(id, inviteremail=inviteremail)

Load sign-up application payload as group member for new AI service agent

### Example
```python
from __future__ import print_function
import time
import workgroup_assistant_api_client
from workgroup_assistant_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = workgroup_assistant_api_client.DefaultApi()
id = 56 # int | 
inviteremail = 'inviteremail_example' # str |  (optional)

try:
    # Load sign-up application payload as group member for new AI service agent
    api_instance.load_signup_post(id, inviteremail=inviteremail)
except ApiException as e:
    print("Exception when calling DefaultApi->load_signup_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **inviteremail** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_workgroup_post**
> load_workgroup_post(id, default_app_id)

Get workgroup for AI service agent

### Example
```python
from __future__ import print_function
import time
import workgroup_assistant_api_client
from workgroup_assistant_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = workgroup_assistant_api_client.DefaultApi()
id = 56 # int | 
default_app_id = 'default_app_id_example' # str | 

try:
    # Get workgroup for AI service agent
    api_instance.load_workgroup_post(id, default_app_id)
except ApiException as e:
    print("Exception when calling DefaultApi->load_workgroup_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **default_app_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

