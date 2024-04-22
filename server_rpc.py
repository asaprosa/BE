# from xmlrpc.server import SimpleXMLRPCServer
# import math


# def factorial(n):
#     # return math.factorial(n)
#     return n*n


# server = SimpleXMLRPCServer(("localhost", 8000))
# print("Listening on port 8000...")
# server.register_function(factorial, "factorial")
# server.serve_forever()

from xmlrpc.server import SimpleXMLRPCServer
import math

def factorial(n):
    return math.factorial(n)

server = SimpleXMLRPCServer(("localhost", 3000))
print("Listening on port 3000...")

# Register the factorial function with the server
server.register_function(factorial, "factorial")

# Start the server
server.serve_forever()
