# Connect to Heroku
# heroku login

# Heroku container login
# heroku container:login

# Create Heroku app
# heroku create streamlit-isen-g1


# Build Image MAC ARM
#docker buildx build --platform linux/amd64 -t streamlit-isen  .

# Build Image 
docker build -t fastapi .

# Tag Image to Heroku app
docker tag fastapi registry.heroku.com/api-isen-g1/web

# Push Image to Heroku
docker push registry.heroku.com/api-isen-g1/web

# Release Image to Heroku
heroku container:release web -a api-isen-g1

# Open Heroku app
heroku open -a api-isen-g1

# Logs
heroku logs --tail -a api-isen-g1