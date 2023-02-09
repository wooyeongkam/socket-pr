import { Manager } from "socket.io-client"

const manager = new Manager("http://localhost:8080", {
  transports: ["websocket"],
})

export const socket = manager.socket("/badge")
