
clear

echo "Stopping container..."
docker stop dmv

echo "Removing container..."
docker rm dmv

echo "Removing image..."
docker rmi --force apache_dmv

echo "All done!"
