
import Vue from "vue";
import App from "./App.vue";
import TypeIt from "typeit";

Vue.config.productionTip = false;

new Vue({
  render: h => h(App)
}).$mount("#app");

new TypeIt("#inner-demo-2", {
  speed: 100,
  lifelike: true,
  cursor: true,
  cursorSpeed: 300,
  loop: true
})
  .pause(1000)
  .type('<span style="font-family: Segoe UI Emoji">👋</span>', {
    html: true
  })
  .type("&nbspHi&nbspI'm&nbspAhamed Careem")
  .pause(750)
  .delete(6, { deleteSpeed: 130 })
  .pause(500)
  .type("I'm&nbspFrom Sri Lanka")
  .pause(500)
  .type(".")
  .move("END")
  .pause(1000)
  .go();
