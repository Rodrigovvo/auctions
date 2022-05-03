<template>
  <div>
        <div class="pagination-row">

            <span v-for="page in pages" :key="page" :class="{active: source.current_page == page }">
                <button class="pagination-index" @click="navigate($event, page)">{{page}}</button>
            </span>

        </div>
      <slot />
  </div>
</template>

<script>
import { watch } from '@vue/runtime-core'
export default {
    data () {
        return {
            pages: []
        }
    },

    props: [
        'source'
    ],
    
    watch: {
        source () {
            var data = this.source.number_of_pages
            this.pages = Array.from(Array(data).keys()).map(x => x + 1)
        }
    },

    methods: {
        navigate (event, page) {
            event.preventDefault()
            this.$emit('navigate', page)

        }
    }
}
</script>

<style scoped>
.pagination-row{
    padding: 5px 0;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
.pagination-index{
    padding: 8px;
    margin: 2px;
    border: None;
    font-size: 1em;
    cursor: pointer;
}
.active {
    background-color: rgb(173, 175, 241);
    border: 3px;
    border-radius: 2px;
}
</style>
