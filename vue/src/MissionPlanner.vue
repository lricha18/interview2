<template>
  <div>
    <!-- justice leage application begins here -->
    <h1 id="jl">Justice League Mission Planner</h1>

    <ul class="roster">
      <h3>Roster:</h3>
      <li v-for="hero in heroes"
          :key="hero.name">

        <!-- to do: conditionally display this span -->
        <span v-if= "hero.chosen">✔ &nbsp;</span>

        <span>{{ hero.name }}&nbsp;</span>
        <span class="edit"
              @click="editHero(hero)">edit</span>
      </li>
      <br>
      <input type="text"
             placeholder="new name"
             v-model="newName"
             v-if="isEdit"
             @keyup.enter="changeName"
             @blur="clear">
      <br>
      <span v-if="isEdit">enter to submit, click outside the box to cancel</span>
    </ul>
    <ChosenHeroes ref="chosenHeroes" :heroes="heroes"/>
  </div>
</template>

<script>
import ChosenHeroes from "./components/ChosenHeroes.vue";

export default {
  components: {
    ChosenHeroes
  },
  data() {
    return {
      heroes: [
        { name: "Superman", chosen: false },
        { name: "Batman", chosen: false},
        { name: "Aquaman", chosen: false },
        { name: "Wonder Woman", chosen: false },
        { name: "Green Lantern", chosen: false },
        { name: "Martian Manhunter", chosen: false },
        { name: "Flash", chosen: false }
      ],
      newName: "",
      isEdit: false,
      heroToModify: null
    };
  },
  methods: {
    editHero(hero) {
      this.isEdit = true;
      this.newName = hero.name;
      this.heroToModify = hero;
    },

    changeName() {
      var oldName = this.heroToModify.name;
      this.$refs.chosenHeroes.propogateName(oldName, this.newName);
      this.heroToModify.name = this.newName;
      this.isEdit = false;
    },

    clear() {
      this.heroToModify = null;
      this.newName = "";
      this.isEdit = false;
    }
  }
};
</script>

<style scoped>
ul.roster {
  text-align: left;
}
.edit {
  color: blue;
  text-decoration: underline;
}
.edit:hover {
  cursor: pointer;
}
</style>
