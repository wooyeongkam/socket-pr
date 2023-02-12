import { socket } from "@/apis/socket"
import { useEffect, useState } from "react"

export const AlertList = () => {
  const [alerts, setAlerts] = useState<string[]>([])

  useEffect(() => {
    // on alerts event

    // emit alerts event

    return () => {
      // emit alerts_terminate
      // off alerts event
    }
  }, [])

  return <div>{alerts.length !== 0 && alerts.map((alert) => <div key={alert}>{alert}</div>)}</div>
}
