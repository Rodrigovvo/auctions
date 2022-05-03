<template>

    <section>
        <section class="oferta">
            <h3> <span>Oferta de Frete nº {{offer.id}}</span> </h3>
            
            <p><span>Cliente: {{clientOffer.name }}</span></p>
            <p>
              <span>De: {{offer.from}}</span> 
              <span> - </span> 
              <span>Para: {{offer.to}}</span>
            </p>
            <p><span>Valor inicial: {{offer.initial_value}}</span></p>
            <p><span>Quantidade: {{offer.amount}}  {{offer.amount_type}}</span></p>
            
        </section>
        
        <hr>

        <section>
          <form @submit.prevent="submitForm">
            <div class="text-align-center">
              <h4>Cadastro de Lances</h4>
            </div>
            <div class="form-group row">
              <InputProvider :source="bid"/>
              <input type="text" class="form-control col-3 mx-2" placeholder="Valor" v-model="bid.value">
              <input type="number" class="form-control col-3 mx-2" placeholder="Quantidade" v-model="bid.amount">
              <button class="btn btn-success">Enviar</button>
            </div>
          </form>
        </section>

        <hr>
        <Pagination :source="data" @navigate="navigate"/>
        <div class="table-responsive">
          <table class="table table-hover">
            <thead>
              <th>Id</th>
              <th>Provedor</th>
              <th>Valor</th>
              <th>Quatidade</th>
            </thead>
            <tbody>
              <tr v-for="bid in bids" :key="bid.id" @click="$data.bid = bid">
                <td>{{  bid.id }}</td>
                <td>{{  bid.id_provider.name }} </td>
                <td>{{  bid.value  }}</td>
                <td>{{  bid.amount  }}</td>
                <td> <button class="btn btn-danger btn-sm mx-1" @click="showModal">x</button> </td>
              </tr>
            </tbody>
          </table>
        </div>

        <Modal v-show="isModalVisible" @close="closeModal">

          <template v-slot:header>
            Importante !
          </template>

          <template v-slot:body>
            Deseja realmente excluir este lance ? 
          </template>

          <template v-slot:footer>
            <button class="btn btn-danger btn-sm mx-1" @click="deleteBid(bid)">Sim</button>
          </template>
        </Modal>
    </section>
    
</template>

<script>
import Pagination from './Pagination.vue'
import InputProvider from './inputs/InputProvider.vue'
import Modal from './modals/Modal.vue';

export default {
  components: { 
    Pagination,
    InputProvider,
    Modal
    },

    name: 'Bids',

    props: [
        'source'
    ],


  data () {
    return {
      offer:[],
      clientOffer: [],
      bids: [],
      data: [],
      customers: [],
      bid: {
        'id_provider': '',
        'id_offer': this.$route.params.id,
        'amount': '',
        'value': '',
      },
      isModalVisible: false,
    }
  },

  async created () {
    await this.getBids()
    await this.getOffer()
  },

  methods: {
    handleErrors (response) {
      if (!response.ok) throw new Error(response.status)
      return response
    },

    navigate (page) {
      this.getBids(page)
    },

    errorMessage (error) {
      window.alert("Ocorreu um erro com sua solicitação." + error)
    },

    async getOffer () {
      var response = await fetch(`http://localhost:8000/api/v1/offers/`+this.$route.params.id)
      this.offer = await response.json()
      this.clientOffer = this.offer.id_customer
    },

    async getBids (page = 1) {
      var response = await fetch('http://localhost:8000/api/v1/offers/'+this.$route.params.id+"/bids/?page="+page)
      this.data = await response.json()
      this.bids = this.data.results 
    },

    async submitForm () {
      if (this.bid.id === undefined) {
        this.createBid()
      } else {
        this.editBid()
      }
    },

    async createBid () {
      var response = await fetch('http://localhost:8000/api/v1/bids/', {
        method: 'post',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.bid)
      }).then(
        this.handleErrors
      ).then(
        response => {
          return response
        }
      ).catch(
        error => this.errorMessage(error)
      )
      this.bids.push(await response.json())
      this.getBids()
    },

    async editBid () {
      await this.getBids()
      await fetch(`http://localhost:8000/api/v1/bids/${this.bid.id}/`, {
        method: 'put',
        headers: {
          'Content-type': 'application/json'
        },
        
        body: JSON.stringify(this.bid)
      }).then(
        this.handleErrors
      ).then(
        response => {
          return response
        }
      ).catch(
        error => this.errorMessage(error)
      )

      this.bids = {}
      await this.getBids()
    },

    async deleteBid (bid) {
      await this.getBids()
      await fetch(`http://localhost:8000/api/v1/bids/${bid.id}/`, {
        method: 'delete',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.bid)
      }).then(
        this.handleErrors
      ).then(
        response => {
          return response
        }
      ).catch(
        error => this.errorMessage(error)
      )

      this.bids = {}
      await this.getBids()
      this.closeModal()
    },
    showModal() {
        this.isModalVisible = true;
      },
    closeModal() {
      this.isModalVisible = false;
    }
  }
}
</script>

<style scoped>
.bids {
  padding: 5px 0;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>
