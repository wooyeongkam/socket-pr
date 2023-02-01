import { Manager } from "socket.io-client"

const manager = new Manager("http://localhost:3001")

export const socket = manager.socket("/chat?username=KAM")
