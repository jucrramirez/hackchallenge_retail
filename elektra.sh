url="$1"

lynx -dump -listonly "$url" | grep "p$" | head -n1 | awk '{print $2}'
