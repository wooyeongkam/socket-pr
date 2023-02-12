import { useEffect, useState } from "react"
import type { NextPage } from "next"

import { socket } from "@/apis/socket"
import { Bell, BellBadge } from "@/components/bells"
import { AlertList } from "@/components/alert-list"
import styles from "../styles/Home.module.css"

const Home: NextPage = () => {
  const [onAir, setOnAir] = useState(false)
  const [isOpenList, setIsOpenList] = useState(false)

  const handleClick = () => {
    setOnAir(false)
    setIsOpenList((value) => !value)
  }

  useEffect(() => {
    // badge namespace socket connect

    // badge namespace connect event

    // on new_alert event

    return () => {
      // badge namespace socket disconnect
    }
  }, [])

  return (
    <div className={styles.box}>
      <button className={styles.button} onClick={handleClick}>
        {onAir ? <BellBadge /> : <Bell />}
      </button>
      {isOpenList && <AlertList />}
    </div>
  )
}

export default Home
