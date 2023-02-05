import { Manager } from "socket.io-client"

const manager = new Manager("http://localhost:8080")

export const socket = manager.socket("/badge")
