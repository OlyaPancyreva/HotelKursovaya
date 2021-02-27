<template>
<!--  отрисовка карусели на главной странице  -->
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="3000"
      controls
      fade
      indicators
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <b-carousel-slide>
        <template v-slot:img>
          <img
            class="d-block img-fluid w-100"
            src="../assets/1.jpg"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>
      <b-carousel-slide>
        <template v-slot:img>
          <img
            class="d-block img-fluid w-100"
            src="../assets/2.jpg"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>
      <b-carousel-slide>
        <template v-slot:img>
          <img
            class="d-block img-fluid w-100"
            src="../assets/3.jpg"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>
      <b-carousel-slide>
        <template v-slot:img>
          <img
            class="d-block img-fluid w-100"
            src="../assets/4.jpg"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>
      <b-carousel-slide>
        <template v-slot:img>
          <img
            class="d-block img-fluid w-100"
            src="../assets/5.jpg"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>


    </b-carousel>
  </div>
</template>

<script>
  export default {
    name: "Carousel",
    data() {
      return {
        slide: 0,
        sliding: null
      }
    },
    methods: {
      onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      }
    }
  }
</script>

<style scoped>

</style>
