<script>
export default {
  data() {
    return {
      data: {},
      form: {},
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await fetch('http://localhost:8000/pokemon/Charizard');
        if (!response.ok) {
          throw new Error('Erreur lors de la récupération des données');
        }
        const data = await response.json();
        this.data = data;
        this.form = data.forms[0];
      } catch (error) {
        console.error('Erreur:', error);
      }
    },
  },
};
</script>



<template>
    <div hidden>
        <pre>{{ data }}</pre>
    </div>
    <div>
      <h1>Données récupérées :</h1>
      <hr>
      <h2>{{ data.name }}</h2>
      <hr>
      <pre>{{ form.types }}</pre>
    </div>
  </template>
  

  
  <style scoped>
  
  </style>