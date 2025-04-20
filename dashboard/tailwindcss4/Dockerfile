FROM ubuntu:latest
LABEL authors="kacper-talaga"

ENTRYPOINT ["top", "-b"]

# Stage 1: Build the Vite app
FROM node:18-alpine AS builder
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy source & build
COPY . .
RUN npm run build

# Stage 2: Serve with nginx
FROM nginx:stable-alpine
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

