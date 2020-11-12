<template>
  <div>
    <!-- :align-top="alignTop" -->
    <v-timeline :dense="dense" dark>
      <v-timeline-item
      v-for="(timeline, i) in timelinesData"
        :key="i"
        :icon="timeline.icon"
        dark
        fill-dot
        
      >
        <h1 class="hobby_head">{{ timeline.title }}</h1>
                <p class="hobby_paragraph">
                  {{ timeline.subtitle }}
                </p>
      </v-timeline-item>
    </v-timeline>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dense: true,
      timelinesData: [
        {
          title: "Web Development",
          subtitle:
            "I love to code and making my own snippets both frontend and backend for fast development.",
          icon: "mdi-code-braces",
          color: 'red lighten-2',
        },
        {
          title: "Graphic Design",
          subtitle: "I always make quality design on my works.",
          icon: "mdi-brush",
          color: 'purple darken-1',
        },
        {
          title: "Photography",
          subtitle:
            "As a hobby, I love to capture random and special moments, but I often capture nature specifically sunrises, sunsets, animals, and more things that I find interesting.",
          icon:"mdi-camera",
          color: 'green lighten-1',
        },
        {
          title: "Videography",
          subtitle:"I love to travel and documenting my travel experiences",
          icon:"mdi-video",
          color: 'indigo',
        },
      ],
    }; 
  },
};
</script>

<style>
.hobby_head{
  font-size: 25px;
  font-weight: 700;
  color: white;
}
.hobby_paragraph{
  font-size: 16px;
  font-weight: 500;
  color: white;
}
</style>