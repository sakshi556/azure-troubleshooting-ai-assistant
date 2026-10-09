status_code = 403
error_message = "AuthorizationFailure"
service = "Azure Storage"
print(status_code)
print(error_message)
print(service)
print (type(service))
error=[1,2,3]
print(error)

statuscode=404
if statuscode == 403:
    print("Access denied")
else:
     print("Access granted")

statuslist=[1,2,3,4]
for statu2 in statuslist:
        print(statu2)
def set():
     sa=8
     ty=2
     print(sa+ty)

set()
try:
    status_code = int("403abc")
    print(status_code)

except:
    print("Invalid status code")

ollamaollama