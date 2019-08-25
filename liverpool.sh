url="$1"

lynx -dump -listonly "$url" | grep "url?q=http" | grep -P "/\d+&" | head -n1 | awk '{print $2}' | while read algo; do algo="${algo#*=}"; echo "${algo%%&*}" ; done