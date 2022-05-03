<template>

        <select class="form-select  col-3 mx-2" v-model="source.amount_type" >
            <option v-for="item in itens" :key="item.id" v-bind:value="item.id">{{item.name}}</option>
        </select>

</template>

<script>
  
export default {
    
    name: 'InputAmountType',
    
    data () {
    return {
      itens: [
        {
        'id': 'TON',
        'name': "Toneladas"
        },
        {
        'id': 'KG',
        'name': "Quilos"
        },
      ],
    }
  },
    
    props: [
        'source'
    ],
    
}
</script>

<style>

</style>