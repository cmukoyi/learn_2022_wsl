#epoch = when your computer thinks time began
import time

# print(time.ctime(0)) 
# print(time.time()) #return current seconds since epoch

# print(time.ctime(time.time()))

# time_object = time.localtime()
# utc_object = time.gmtime()

# print(time_object)
# local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)
# utc_time = time.strftime("%B %d %Y %H:%M:%S",utc_object)
# print(local_time)
# print(utc_time)

time_string = "20 April, 2021"
time_object = time.strptime(time_string,"%d %B , %Y")
print(time_object)