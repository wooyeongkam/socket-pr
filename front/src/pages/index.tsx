import { useState } from "react"
import type { NextPage } from "next"

import { Bell, BellBadge } from "@/components/Bells"
import styles from "../styles/Home.module.css"
import { socket } from "@/apis/socket"

const Home: NextPage = () => {
  const [onAir, setOnAir] = useState(false)
  const [connected, setConnected] = useState(false)

  const handleClick = () => {
    socket.on("connect", () => {
      setConnected(true)
    })
  }

  return (
    <div className={styles.box}>
      <button className={styles.button} onClick={handleClick}>
        {onAir ? <BellBadge /> : <Bell />}
      </button>
      <p>{connected}</p>
    </div>
  )
}

export default Home
