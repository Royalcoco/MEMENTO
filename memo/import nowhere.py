import from Nowhere.connection_$$ import Connection
from typing import List, Optional
import asyncio

class Server:   public Server(int port) {
    private:
        int _port;
        std::vector<Connection*> _connections;

    public:
        Server() = delete;                                          // Default constructor is deleted to prevent misuse 
        void start() {
            // Start the server on the given port
            asio::ip::tcp::endpoint endpoint(asio::ip::address::from_string("127.0.0.1"), _port); 
            _acceptor.open(endpoint.protocol());
            _acceptor.set_option(asio::socket_base::reuse_address(true));
            _acceptor.bind(endpoint);
            _acceptor.listen();
            
            accept_next();
        }

        ~Server() {
            for (auto connection : _connections) delete connection;
        }

        int getPort() const { return     _port; }

    private:
        asio::io_context _ioc;
        asio::ip::tcp::acceptor _acceptor{_ioc};

        void accept_next() {
            auto c = new Connection(_ioc
                                    , [this] (const asio::error_code& ec) {
                                        if (!ec)
                                            accept_next();
                                    });
            _connections.push_back(c);
            _acceptor.async_accept(c->getSocket(), [this, c] (const asio::error_code& ec, asio::ip::tcp::socket socket) {
                c->connected(ec, socket);
            });
            }
}
