import platform
import os
import socket
import sys

print (f"\n Machine Type: {platform.machine()}")
print (f"\n Processor Type: {platform.architecture()}")

socket.setdefaulttimeout(50)
print (f"\n Default Timeout for socket: {socket.getdefaulttimeout()}")

print (f"\n OS Type: {os.name}")
print (f"\n OS Name: {platform.system()}")
print (f"\n Current PID: {os.getpid()}")

file_name = "fdpractice.txt"
file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
file_object_TextIO = os.fdopen(file_handle, "w+")
file_object_TextIO.write("Hello World")
file_object_TextIO.flush()

pid = 0
if pid == 0:
    print (f"\n [Child PID: {os.getpid()}], [Parent PID: {os.getppid()}]")
    os.leek(file_handle,0,0)
    print (f"\n[Child PID: {os.getpid()}], File contents: {os.read(file_handle, 100).decode()}")
    os.close(file_handle)
    sys.exit(0)
else:
    print(f"\n[Parent PID: {os.getpid()}], [Child PID: {pid}]")
    print("Wait for the child process to terminate...")
    os.waitpid(pid,0)
    print("child finished")
    file_object_TextIO.close()
    sys.exit(0)
