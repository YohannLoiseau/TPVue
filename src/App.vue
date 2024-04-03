<template>
  <div id="app">
    <h1>Les questionnaires</h1>
    <ul>
      <Questionnaire v-for="questionnaire in questionnaires" :questionnaire="questionnaire" :key="questionnaire.id" @remove="removeQuestionnaire" @edit="updateQuestionnaire" @edit-question="updateQuestion" @add-questionnaire="addQuestionnaire" @add-question="addQuestion" @remove-question="removeQuestion"/>
    </ul>
    <input type="button" value="Add questionnaire" @click="this.addQuestionnaire('Editez le questionnaire')">
  </div>
</template>

<script>
import Questionnaire from './components/Questionnaire.vue';

export default {
  data() {
    return {
      questionnaires: []
    };
  },
  components: {
    Questionnaire
  },
  mounted() {
    this.loadQuestionnaires();
  },
  methods: {
    async loadQuestionnaires() {
      
      try {
        const response = await fetch('http://127.0.0.1:5000/questionnaires', {
          method: 'GET'
        });
        const data = await response.json();
        this.questionnaires = data;
        console.log('Questionnaires loaded:', this.questionnaires);
      } catch (error) {
        console.error('Error loading questionnaires:', error);
      }
    },
    async removeQuestionnaire(QuestionnaireId){
      try {
        await fetch(`http://127.0.0.1:5000/questionnaires/${QuestionnaireId['id']}`, {
          method: 'DELETE'
        });
        this.questionnaires = this.questionnaires.filter(questionnaire => questionnaire.id !== QuestionnaireId);
        this.loadQuestionnaires();
      } catch (error) {
        console.error('Error removing questionnaire:', error);
      }
    },

    async updateQuestion(updatedQuestion){
      try {
        await fetch(`http://127.0.0.1:5000/questions/${updatedQuestion.id}/${updatedQuestion.title}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(updatedQuestion)
        });
        console.log('Question updated:', updatedQuestion);
        this.loadQuestionnaires();
      } catch (error) {
        console.error('Error updating question:', error);
      }
    },

    async updateQuestionnaire(updatedQuestionnaire){
      try {
        await fetch(`http://127.0.0.1:5000/questionnaires/${updatedQuestionnaire.id}/${updatedQuestionnaire.title}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(updatedQuestionnaire)
        });
        console.log('Questionnaire updated:', updatedQuestionnaire);
      
        this.loadQuestionnaires();
        /*if (questionnaireIndex !== -1) {
          this.$set(this.questionnaires, questionnaireIndex, updatedQuestionnaire);
        }*/
      } catch (error) {
        console.error('Error updating questionnaire:', error);
      }
    },

    async addQuestionnaire(questionnaire){
      try {
        await fetch(`http://127.0.0.1:5000/questionnaires/${questionnaire}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
        });
      
        this.loadQuestionnaires();
        /*if (questionnaireIndex !== -1) {
          this.$set(this.questionnaires, questionnaireIndex, updatedQuestionnaire);
        }*/
      } catch (error) {
        console.error('Error updating questionnaire:', error);
      }
    },

    async addQuestion(questionnaire){
      try {
        await fetch(`http://127.0.0.1:5000/questionnaires/${questionnaire.id}/questions`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
        });
      
        this.loadQuestionnaires();
        /*if (questionnaireIndex !== -1) {
          this.$set(this.questionnaires, questionnaireIndex, updatedQuestionnaire);
        }*/
      } catch (error) {
        console.error('Error updating questionnaire:', error);
      }
    },

    async removeQuestion(question){
      try {
        await fetch(`http://127.0.0.1:5000/questions/${question.id}`, {
          method: 'DELETE'
        });
        this.loadQuestionnaires();
      } catch (error) {
        console.error('Error removing questionnaire:', error);
      }
    },
  }
};
</script>


<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

.app {
  display: flex;
}

input {
  border: none;
  padding: 5px;
  margin-right: 10px;
  cursor: pointer;
  background-color: lightgray;
  color: black;
}
</style>
