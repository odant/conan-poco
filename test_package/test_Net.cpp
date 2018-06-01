// Test for Poco Conan package
// Dmitriy Vetutnev, Odant, 2018


#include <Poco/Net/ServerSocket.h>
#include <Poco/Net/SocketStream.h>


#include <iostream>
#include <cstdlib>
#include <thread>
#include <chrono>
#include <sstream>


using namespace Poco::Net;


auto server = [](const SocketAddress& addr) {

    std::cout << "Start server on " << addr.toString() \
              << ", thread ID: " << std::hex << std::showbase << std::this_thread::get_id() << std::dec \
              << std::endl;

    ServerSocket listener{addr};
    StreamSocket socket = listener.acceptConnection();

    char buffer[64] = {0};
    const int length = socket.receiveBytes(buffer, sizeof(buffer));
    std::cout << "Server received " << length << " bytes, data: ";
    std::cout.write(buffer, length);
    std::cout << std::endl;

    const char* response = "Pong";
    socket.sendBytes(response, static_cast<int>(std::strlen(response)));
};


int main(int, char**) {

    std::cout << "Main thread ID: " << std::hex << std::showbase << std::this_thread::get_id() << std::dec << std::endl;

    const SocketAddress addr{"127.0.0.1", 9758};

    std::thread server_thread{server, addr};
    std::this_thread::sleep_for(std::chrono::milliseconds{100});


    std::cout << "Connect to server..." << std::endl;
    StreamSocket socket{addr};
    SocketStream stream{socket};
    stream << "Ping";
    stream.flush();

    std::this_thread::sleep_for(std::chrono::milliseconds{100});

    std::stringstream buffer;
    stream >> buffer.rdbuf();
    std::cout << "Client received " << buffer.str().length() << " bytes, data: " << buffer.str() << std::endl;


    server_thread.join();

    return EXIT_SUCCESS;
}

