<template>
  <div>
    <vue-typer
      :text="txtMessages"
      :repeat="Infinity"
      :shuffle="false"
      initial-action="typing"
      :pre-type-delay="350"
      :type-delay="70"
      :pre-erase-delay="1200"
      :erase-delay="70"
      erase-style="backspace"
      :erase-on-complete="true"
      caret-animation="blink"
    ></vue-typer>
  </div>
</template>

<script>
import { VueTyper } from "vue-typer";
export default {
  name: "TextTyping",
  props: {
    txtMessages: Array,
  },
  components: {
    VueTyper,
  },
};
</script>

<style lang="scss">
.vue-typer {
  font-size: 2rem;
  font-weight: 400;
  color: #fff;
  opacity: 0.8;

  .custom.char {
    color: #fff;
    /* Styles for each character
       e.g. color, background-color */

    &.typed {
      color: #fff;
      /* Styles specific to typed characters
         i.e. characters to the left of the caret */
    }
    &.selected {
      color: #fff;
      /* Styles specific to selected characters
         i.e. characters to the right of the caret while VueTyper's
              'eraseStyle' is set to a selection-based style */
    }
    &.erased {
      color: #fff;
      /* Styles specific to erased characters
         i.e. characters to the right of the caret while VueTyper's
              'eraseStyle' is set to a non-selection-based style */
    }
  }
  .custom.caret {
    background-color: #fff;
  }
}
@media screen and (max-width: 992px) {
  .vue-typer {
    font-size: 1.8rem;
  }
}

/* On screens that are 600px or less, set the background color to olive */
@media screen and (max-width: 600px) {
  .vue-typer {
    font-size: 1.3rem;
  }
}
</style>