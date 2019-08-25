url="$1"

lynx -dump -listonly "$url" | grep "articulo" | head -n1 | awk '{print $2}'