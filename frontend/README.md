The Waterfall Frontend
======================

Install
-------
Установка dev зависимостей:

- Node.js и npm устанавливаются системным менеджером пакетов. Нужны только для разработки, в продакшн не используются.

Установка зависимостей:
```bash
npm install
```

Build
-----
```bash 
# Build dev config and start a web server 
npm start

# Just build the dist version and copy static files
npm run dist

# Lint all files in src (also automatically done AFTER tests are run)
npm run lint

# Clean up the dist directory
npm run clean

# Just copy the static assets
npm run copy
```