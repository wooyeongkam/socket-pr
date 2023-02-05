import { useEffect, useState } from 'react';
import type { NextPage } from 'next';

import { Bell, BellBadge } from '@/components/Bells';
import styles from '../styles/Home.module.css';
import { socket } from '@/apis/socket';

const Home: NextPage = () => {
  const [onAir, setOnAir] = useState(false);
  const [alerts, setAlerts] = useState<string[]>([]);

  const handleClick = () => {
    if (onAir) {
      setOnAir(false);
      socket.emit('alerts');
      return;
    }

    if (socket.hasListeners('alerts')) {
      socket.off('alerts');
      setAlerts([]);
    }
  };

  useEffect(() => {
    // badge namespace connect and emit new_alert
    socket.on('connect', () => {
      console.log('badge connect');
      socket.emit('new_alert');
    });

    // on new_alert event
    socket.on('new_alert', (data: true) => {
      console.log('new_alert', data);
      if (!onAir) {
        setOnAir(true);
      }
    });

    // on alerts event
    socket.on('alerts', (data: string[]) => {
      console.log('alerts', data);
      setAlerts(data);
    });
  }, []);

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
  );
};

export default Home;
