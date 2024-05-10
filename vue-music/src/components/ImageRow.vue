<template>
    <div class="carousel-container">
      <vue-slick-carousel
        :arrows="false"
        :dots="false"
        :infinite="true"
        :slidesToShow="3"
        :slidesToScroll="1"
        :autoplay="true"
        :autoplaySpeed="2000"
        :speed="500"
        :vertical="true"
        :verticalSwiping="true"
        :pauseOnHover="false"
      >
      <div v-for="image in images" :key="image.id">
        <a :href="image.link" target="_blank" rel="noopener noreferrer">
          <img :src="image.url" :alt="image.alt" class="carousel-image">
        </a>
      </div>
      </vue-slick-carousel>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        images: [
          { id: 1, url: 'https://avatars.yandex.net/get-music-content/41288/5c92aeb1.a.3555472-1/m1000x1000', alt: 'Image 1', link: 'https://music.yandex.ru/album/3555472' },
          { id: 2, url: 'https://avatars.yandex.net/get-music-content/5485872/98a66686.a.19739328-1/m1000x1000', alt: 'Image 2', link: 'https://music.yandex.ru/album/19739328' },          
          { id: 3, url: 'https://avatars.yandex.net/get-music-content/2789402/e7f49d85.a.1177207-2/m1000x1000', alt: 'Image 3', link: 'https://music.yandex.ru/album/1177207' },
          { id: 4, url: 'https://avatars.yandex.net/get-music-content/103235/bc8ead69.a.5905756-1/m1000x1000', alt: 'Image 4', link: 'https://music.yandex.ru/album/5905756' },
          { id: 5, url: 'https://avatars.yandex.net/get-music-content/2480468/69048685.a.3952720-2/m1000x1000', alt: 'Image 5', link: 'https://music.yandex.ru/album/3952720' },
          { id: 6, url: 'https://avatars.yandex.net/get-music-content/10103188/54e44017.a.4924440-3/m1000x1000', alt: 'Image 6', link: 'https://music.yandex.ru/album/4924440' },
          { id: 7, url: 'https://avatars.yandex.net/get-music-content/5853241/80984e8a.a.29760999-1/m1000x1000', alt: 'Image 7', link: 'https://music.yandex.ru/album/29760999' },
          { id: 8, url: 'https://avatars.yandex.net/get-music-content/10641165/68569b6f.a.5838243-2/m1000x1000', alt: 'Image 8', link: 'https://music.yandex.ru/album/5838243' },
          { id: 9, url: 'https://avatars.yandex.net/get-music-content/4399834/0415f8b8.a.17439837-1/m1000x1000', alt: 'Image 9', link: 'https://music.yandex.ru/album/17439837' },
          { id: 10, url: 'https://avatars.yandex.net/get-music-content/32236/980ee6b2.a.3226577-1/m1000x1000', alt: 'Image 10', link: 'https://music.yandex.ru/album/3226577' },
          { id: 11, url: 'https://avatars.yandex.net/get-music-content/4399644/7c3349cf.a.13535624-1/m1000x1000', alt: 'Image 11', link: 'https://music.yandex.ru/album/13535624' },
          { id: 12, url: 'https://avatars.yandex.net/get-music-content/7852894/6ca905b5.a.25573804-1/m1000x1000', alt: 'Image 12', link: 'https://music.yandex.ru/album/25573804'  },         
          { id: 13, url: 'https://avatars.yandex.net/get-music-content/10139807/520d664e.a.28719429-1/m1000x1000', alt: 'Image 13', link: 'https://music.yandex.ru/album/28719429' },
          { id: 14, url: 'https://avatars.yandex.net/get-music-content/4477012/980d81b3.a.19332695-1/m1000x1000', alt: 'Image 14', link: 'https://music.yandex.ru/album/19332695' },
          { id: 15, url: 'https://avatars.yandex.net/get-music-content/6447985/73838729.a.23211206-1/m1000x1000', alt: 'Image 15', link: 'https://music.yandex.ru/album/23211206' },
          { id: 16, url: 'https://avatars.yandex.net/get-music-content/97284/db815f7b.a.5600810-1/m1000x1000', alt: 'Image 16', link: 'https://music.yandex.ru/album/5600810' },          
          { id: 17, url: 'https://avatars.yandex.net/get-music-content/6447985/458c45a5.a.22820453-1/m1000x1000', alt: 'Image 17', link: 'https://music.yandex.ru/album/22820453' },
          // Добавьте остальные изображения, если нужно
        ]
      }
    }
  }
  </script>
  
  <style scoped>
  .carousel-container {
    width: 100%;
    overflow: hidden;
  }
  
  .carousel-image {
    max-width: 100%;
    max-height: 300px;
    object-fit: cover;
  }




  </style>
  