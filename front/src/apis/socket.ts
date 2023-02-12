import { Manager } from "socket.io-client"

const manager = new Manager("http://localhost:8080", {
  transports: ["websocket"],
  autoConnect: false,
  path: "/ws/socket.io",
})

export const socket = manager.socket("/badge")
