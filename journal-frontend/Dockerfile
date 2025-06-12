# frontend.Dockerfile
# Use an official Node.js image
FROM node:18-alpine

# Set working directory inside the container
WORKDIR /app

# Copy only the package files first (for layer caching)
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the source code
COPY . .

# Expose the development port
EXPOSE 3000

# Start the dev server
CMD ["npm", "start"]
