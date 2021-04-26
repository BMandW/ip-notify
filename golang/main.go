package main

import (
	"fmt"
	"net"
	"os"
	"strings"
)

func main() {
	updLn, err := net.ListenPacket("udp", "0.0.0.0:37001")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	buf := make([]byte, 64)

	fmt.Println("Start.")
	for {
		n, addr, err := updLn.ReadFrom(buf)
		if err != nil {
			fmt.Println(err)
			os.Exit(2)
		}
		ip := strings.Split(addr.String(), ":")[0]
		fmt.Printf("Receive Packet from %s %s\n", ip, string(buf[:n]))
	}

}
