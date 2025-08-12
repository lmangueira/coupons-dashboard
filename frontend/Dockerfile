FROM node:24-alpine as build-stage

WORKDIR /app

COPY package*.json ./
# COPY quasar.config.js ./
COPY . .

RUN npm install
RUN npm install -g @quasar/cli

RUN quasar build

FROM nginx:stable-alpine as production-stage

COPY --from=build-stage /app/dist/spa /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
