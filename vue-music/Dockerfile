FROM node:lts-alpine

WORKDIR /media/linux_anvi/18C0ED51C0ED3622/bip/Must-Listen/


RUN npm install -g http-server

COPY package*.json ./
RUN npm install
COPY . .
#RUN npm run serve
CMD ["npm", "run", "serve"]

