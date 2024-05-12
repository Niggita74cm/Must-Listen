# vue-music

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### Что где как? передача данных требуется в данных файлах
* /src/components/AuthUserForm.vue - авторизация пользователя, там надо передавать креды
* /src/components/MusicPage.vue - там информация о треке, комментарии оценки и тд и тп
* /src/components/RegistrUserForm.vue - регистрация, там нет коментов, но там и так понятно
* /src/components/SearchResults.vue - нужны результаты поиска
* /src/components/MainPage.vue - сортировка на главное странице