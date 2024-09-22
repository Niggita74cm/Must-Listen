<template>
  <div id="app">
    <header class="bg-dark">
      <b-navbar class="w-9 mx-auto slim-navbar" type="dark" variant="dark">
        <router-link to="/MainPage" class="navbar-brand d-flex align-items-center">
          <img src="./logo/logo.png" alt="Must Listen Logo" class="logo">
          <span>Must Listen</span>
        </router-link>
        <b-navbar-nav class="ml-auto">
          <b-nav-item>
            <router-link to="/SettingsF" class="text-white">
              <b-icon icon="gear" aria-label="Settings" class="white-icon"></b-icon>
            </router-link>
          </b-nav-item>
        </b-navbar-nav>
        <form class="form-inline d-flex my-2 my-lg-0" @submit.prevent="handleSearch">
          <input class="form-control mr-sm-2" type="search" placeholder="Найти..." aria-label="Search" v-model="searchTerm">
          <router-link :to="{ name: 'SearchResults', query: { NameTrack: searchTerm } }" class="btn btn-outline-light my-2 my-sm-0 ml-auto" type="submit">Поиск</router-link>
        </form>
      </b-navbar>
    </header>
  </div>
</template>

<script>
export default {
  name: 'MenuSidebar',
  data() {
    return {
      searchTerm: '',
    };
  },
  methods: {
    handleSearch() {
      // Обработка логики поиска здесь
      this.$router.push({ name: 'SearchResults', query: { NameTrack: this.searchTerm } });
    },
  },
};
</script>

<style scoped>
.white-icon {
  color: white;
}
</style>
