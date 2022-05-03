<template>

        <select class="form-select col-3 mx-2" v-model="source.id_provider" >
            <option v-for="item in itens" :key="item.id" v-bind:value="item.id">{{item.name}}</option>
        </select>

</template>

<script>
  
export default {
    
    name: 'InputProvider',
    
    data () {
    return {
      itens: [],
    }
  },
    
    props: [
        'source'
    ],
    

    async created () {
        await this.getPersons()
    },

    methods: {
    async getPersons () {
      var response = await fetch('http://localhost:8000/api/v1/persons/get-persons')
      this.itens = await response.json()
    },

    }

}
</script>

<style>

</style>