const http = require("http");
const socket = require("socket.io");
 
const server = http.createServer((request, response) => {
     response.end("...");
});
server.listen(1234);
// We need to listen all requests which will come from 1234 port via socket. 
const io = socket.listen(server);

io.sockets.on("connection", socket => {
    // Connection will be triggered when client has been connected to the server. Socket parameter included client infos who is connected to the server.
 console.log("User connection", socket.client.id);
});
