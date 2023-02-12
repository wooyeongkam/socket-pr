// useEffect(() => {
//   // on alerts event
//   socket.on('alerts', (data: string[]) => {
//     console.log('alerts', data);
//     setAlerts(data);
//   });

//   // emit alerts event
//   socket.emit('alerts');

//   return () => {
//     // emit alerts_terminate
//     // off alerts event
//     socket.emit('alerts_terminate');
//     socket.off('alerts');
//   };
// }, []);

// useEffect(() => {
//   // badge namespace socket connect
//   socket.connect()

//   // badge namespace connect event
//   socket.on("connect", () => {
//     console.log("badge connect")
//   })

//   // on new_alert event
//   socket.on("new_alert", (data: true) => {
//     console.log("new_alert", data)
//     if (isOpenList) return

//     setOnAir(data)
//   })

//   return () => {
//     // badge namespace socket disconnect
//     socket.disconnect()
//   }
// }, [])
