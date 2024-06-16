

# Włączenie przekazywania pakietów między interfejsami
echo "1" > /proc/sys/net/ipv4/ip_forward

# Konfiguracja iptables do masqueradingu (eth0 jako WAN)
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# Zezwolenie na przekazywanie pakietów przychodzących z interfejsu eth0
iptables -A FORWARD -i eth0 -j ACCEPT

