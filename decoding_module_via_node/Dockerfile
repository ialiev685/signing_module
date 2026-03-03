FROM node:22-alpine

RUN corepack enable

WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

COPY . .

EXPOSE 3000

RUN yarn build

CMD ["node", "dist/index.js"]