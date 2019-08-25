url="$1"

lynx -dump -listonly "$url" | grep -v "/gp/" | grep "/dp/" | head -n1 | awk '{print $2}'