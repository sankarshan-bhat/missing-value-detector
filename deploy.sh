
echo "Building new Docker image..."
docker build -t apache_dmv .

echo "Running container..."
docker run -dit --name dmv -p 8080:80 apache_dmv

echo "All done!"
