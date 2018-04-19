// Test for Poco Conan package
// Dmitriy Vetutnev, Odant, 2018


#include <Poco/SharedPtr.h>
#include <Poco/AutoPtr.h>
#include <Poco/Net/SecureServerSocket.h>
#include <Poco/Net/SecureStreamSocket.h>
#include <Poco/Net/SocketStream.h>
#include <Poco/Net/SSLManager.h>
#include <Poco/Net/AcceptCertificateHandler.h>


#include <iostream>
#include <cstdlib>
#include <thread>
#include <chrono>
#include <sstream>


using namespace Poco;
using namespace Poco::Net;


auto server = [](const SocketAddress& addr) {

    std::cout << "Start server on " << addr.toString() \
              << ", thread ID: " << std::hex << std::showbase << std::this_thread::get_id() << std::dec \
              << std::endl;

    SecureServerSocket listener{addr};
    StreamSocket socket = listener.acceptConnection();

    char buffer[64] = {0};
    const int length = socket.receiveBytes(buffer, sizeof(buffer));
    std::cout << "Server received " << length << " bytes, data: ";
    std::cout.write(buffer, length);
    std::cout << std::endl;

    const char* response = "Pong";
    socket.sendBytes(response, std::strlen(response));
};


int main(int, char**) {

    std::cout << "Main thread ID: " << std::hex << std::showbase << std::this_thread::get_id() << std::dec << std::endl;

    {
        std::cout << "Initialize client TLS context..." << std:: endl;
        const bool isServer = false;
        SharedPtr<InvalidCertificateHandler> certHandler = new AcceptCertificateHandler(isServer);
        AutoPtr<Context> context = new Context(Context::CLIENT_USE, "certificate.pem", Context::VERIFY_RELAXED);
        SSLManager::instance().initializeClient(nullptr, certHandler, context);
    }
    {
        std::cout << "Initialize server TLS context..." << std:: endl;
        const bool isServer = true;
        SharedPtr<InvalidCertificateHandler> certHandler = new AcceptCertificateHandler(isServer);
        AutoPtr<Context> context = new Context(Context::SERVER_USE, "key.pem", "certificate.pem", "certificate.pem", Context::VERIFY_RELAXED);
        SSLManager::instance().initializeServer(nullptr, certHandler, context);
    }


    const SocketAddress addr{"127.0.0.1", 49758};

    std::thread server_thread{server, addr};
    std::this_thread::sleep_for(std::chrono::milliseconds{100});


    std::cout << "Connect to server..." << std::endl;
    SecureStreamSocket socket{addr};
    std::cout << "Server hostname: " << socket.getPeerHostName() << std::endl;
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

