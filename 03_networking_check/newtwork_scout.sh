#/bin/bash
Target="127.0.0.1"

for Port in 22 80 443 3000
do 
     nc -z -w 1 $Target $Port
    if [ $? -eq 0 ]; then
      echo "Port $Port: OPEN (Welcome!)"
      echo "$(date) - Port $PORT: OPEN"
    else 
       echo "Port $Port: CLOSED(locked)"
    fi
done 
