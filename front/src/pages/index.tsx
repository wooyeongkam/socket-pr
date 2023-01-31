import { useState } from "react"
import type { NextPage } from "next"

import { Bell, BellBadge } from "@/components/Bells"
import styles from "../styles/Home.module.css"

const Home: NextPage = () => {
  const [onAir, setOnAir] = useState(false)

  const handleClick = () => {
    setOnAir((prev) => !prev)
  }

  return (
    <div className={styles.box}>
      <button className={styles.button} onClick={handleClick}>
        {onAir ? <BellBadge /> : <Bell />}
      </button>
    </div>
  )
}

export default Home
