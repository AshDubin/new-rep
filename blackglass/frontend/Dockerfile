FROM node:18-alpine
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install && npm install -g serve
COPY . .
RUN npm run build
CMD ["serve", "-s", "dist"]
