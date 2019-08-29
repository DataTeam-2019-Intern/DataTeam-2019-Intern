const http = require("http");
const socket = require("socket.io");
 
const server = http.createServer((request, response) => {
     response.end("...");
});
server.listen(1234);

const io = socket.listen(server);
io.sockets.on("connection", socket => {


      console.log("User connection", socket.client.id);
     console.log(i+"."+"User bağlandı");
   
    socket.on("disconnect", () => {
        console.log("User disconnect");
    });
    socket.on("sendMessageToServer", () => {
        console.log("sendMessageToServer tetiklendi.");
   });
   socket.emit("sendMessageToClient");
});