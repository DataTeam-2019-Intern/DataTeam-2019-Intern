const http = require("http");
const socket = require("socket.io");
 
const server = http.createServer((request, response) => {
     response.end("...");
});
server.listen(1234);
//1234 portuna gelecek olan tüm istekleri socket tarafından dinlememiz gerekmektedir.
const io = socket.listen(server);

io.sockets.on("connection", socket => {
    //Server'a bir client bağlandığı zaman "connection" isimli olay tetiklenecektir. socket parametresi ise bağlantı yapan client'ın bilgisini içermektedir.
    console.log("User connection", socket.client.id);
});