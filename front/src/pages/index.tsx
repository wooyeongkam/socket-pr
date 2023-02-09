import { useEffect, useState } from "react"
import type { NextPage } from "next"

import { Bell, BellBadge } from "@/components/Bells"
import styles from "../styles/Home.module.css"
import { socket } from "@/apis/socket"

const Home: NextPage = () => {
  const [onAir, setOnAir] = useState(false)
  const [alerts, setAlerts] = useState<string[]>([])

  const handleClick = () => {}

  useEffect(() => {
    // badge namespace connect and emit new_alert

    // on new_alert event

    // on alerts event

    return () => {
      socket.disconnect()
    }
  }, [])

  return (
    <div className={styles.box}>
      <button className={styles.button} onClick={handleClick}>
        {onAir ? <BellBadge /> : <Bell />}
      </button>
      <div className={styles.list}>
        {alerts.map((alert, index) => (
          <div key={alert.length + index}>{alert}</div>
        ))}
      </div>
    </div>
  )
}

export default Home
