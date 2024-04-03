
<template>
  <div class="questionnaire">
    <div class="title">
      <h2 v-if="!editingTitle" @click="changeDetails">{{ questionnaire.name }}</h2>
      <input class="textfield" v-else type="text" v-model="editedName" @keyup.enter="finishEditingTitle" @blur="finishEditingTitle">
      <input v-if="!editingTitle" type="button" value="Editer" @click="startEditingTitle">
      <input v-else type="button" value="Sauvegarder" @click="finishEditingTitle">
    </div>
    <div v-if="details" class="questions">
      <li v-for="question in questionnaire.questions">
        <h3 v-if="!editingQuestion||question.id!=editedQuestion.id" id="{{ question.id }}" @click="startEditingQuestion(question)">{{ question.title }}</h3>
        <input v-else-if="question.id==editedQuestion.id" type="text" id="{{ question.id }}" class="textfield" v-model="editedQuestion.title" @keyup.enter="finishEditingQuestion(question)" @blur="finishEditingQuestion">
        <input type="button" value="Supprimer Question" class="suppr" @click="supprQuestion(question.id)">
        <p>Les choix : </p>
        <ul>
          <li>
            <p v-if="!editingChoix||question.id!=editedQuestion.id" @click="startEditingChoix(question)">{{ question.choix1 }}</p>
            <input class="textfieldsmall" v-else type="text" v-model="editedChoix1" @keyup.enter="finishEditingChoix" @blur="finishEditingChoix">
          </li>
          <li>
            <p v-if="!editingChoix||question.id!=editedQuestion.id" @click="startEditingChoix(question)">{{ question.choix2 }}</p>
            <input class="textfieldsmall" v-else type="text" v-model="editedChoix2" @keyup.enter="finishEditingChoix" @blur="finishEditingChoix">
          </li>
          <li>
            <p v-if="!editingChoix||question.id!=editedQuestion.id" @click="startEditingChoix(question)">{{ question.choix3 }}</p>
            <input class="textfieldsmall" v-else type="text" v-model="editedChoix3" @keyup.enter="finishEditingChoix" @blur="finishEditingChoix">
          </li>
          <li>
            <p v-if="!editingChoix||question.id!=editedQuestion.id" @click="startEditingChoix(question)">{{ question.choix4 }}</p>
            <input class="textfieldsmall" v-else type="text" v-model="editedChoix4" @keyup.enter="finishEditingChoix" @blur="finishEditingChoix">
          </li>
        </ul>
        <p v-if="question.question_type=='simple'">La bonne réponse : {{ question.reponse }}</p>
        <p v-else>Les bonnes réponses : {{ question.reponse1 }}, {{ question.reponse2 }}</p>
      </li>
    <button class="add" v-if="details" @click="addQuestion(questionnaire.id)">Add Question</button>
    <button v-if="details" class="suppr" @click="supprQuestionnaire">Supprimer Questionnaire</button>
    </div>
  </div>
</template>

<script>

export default {
  props: ['questionnaire'],
  data() {
    return {
      details: false,
      editingTitle: false,
      editedName: this.questionnaire.name,
      editingQuestion: false,
      editedQuestion: "",
      editingChoix: false,
      editedChoix1: "",
      editedChoix2: "",
      editedChoix3: "",
      editedChoix4: "",
    };
  },
  methods: {
    supprQuestionnaire() {
      this.$emit('remove', { id: this.questionnaire.id });
    },
    changeDetails(){
      this.details = !this.details;
    },
    startEditingTitle() {
      this.editingTitle = true;
    },
    finishEditingTitle() {
      this.editingTitle = false;
      this.$emit('edit', { id: this.questionnaire.id, title: this.editedName });
    },
    startEditingQuestion(question) {
      this.editingQuestion = true;
      this.editedQuestion = question;
    },
    finishEditingQuestion() {
      this.editingQuestion = false;
      this.$emit('edit-question', { id: this.editedQuestion.id, title: this.editedQuestion.title });
    },
    addQuestion(id){
      this.$emit('add-question', { id: id })
    },
    supprQuestion(id){
      this.$emit("remove-question", {id: id})
    },
    startEditingChoix(question){
      editedQuestion = question;
      this.editingChoix = true;
    },
    finishEditingChoix(){
      this.editingChoix = false;
    },
  },
  emits: ['remove', 'edit', 'edit-question', 'add-question', 'remove-question'] 
}
</script>

<style scoped>


.questionnaire{
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

button, input {
  background-color: lightgray;
  color: black;
  border: none;
  padding: 5px;
  margin-right: 10px;
  cursor: pointer;
}

.suppr{
  
  background-color: red;
  color: white;
}

.textfield{
  font-size: larger;
  width:15em;
}

.textfieldsmall{
  font-size: large;
  width: 13em;
}

input{
  max-height: 3em;
  margin: auto;
  margin-left: 3em;
}

.title{
  display: flex;
  flex-wrap: nowrap;
  flex-basis: 100%;
  
}


ul{
  list-style: none;
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  justify-content: center;
}

li{
  margin: 20px;
  align-items: center;
  justify-content: center;
}

h2{
  padding: 1em;
  background-color: lightgray;
  border-radius: 20px;
  cursor: pointer;
}

ul{
  display: flex;
  flex-wrap: wrap;
}

li{
  flex-basis: 100%;
  flex-grow: 1;
}

.title>h2, .textfield{
  flex-basis: 100%;
}


</style>